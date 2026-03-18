import requests
from geopy.geocoders import Nominatim
from deep_translator import GoogleTranslator
from tkinter import messagebox
class API:
    def __init__(self):
        self.titulo = self.resumo = self.capital = self.populacao = ""
        self.bandeira = self.moeda = self.temp = self.vento = self.esta_chovendo = ""

    def gerar_dados(self,pais):
        tema = pais
        tema_url = tema.replace(" ", "_")
        dominio = "https://pt.wikipedia.org"
        caminho = "/api/rest_v1/page/summary/"
        url_final = dominio + caminho + tema_url

        headers = {"User-Agent": "ConsultaEscola/1.0"}

        try:
            response = requests.get(url_final, headers=headers, timeout=10)

            if response.status_code == 200:
                dados = response.json()
                self.titulo = (f"{dados.get('title')}")
                self.resumo = (f"Resumo: {dados.get('extract')}")
            else:
                messagebox.showerror("Erro",f"Erro na API ({response.status_code}): {response.text}")

        except Exception as e:
            messagebox.showerror("Erro", f"Erro de conexão detalhado: {e}")

        geolocator = Nominatim(user_agent="teste_escola_clima")
        theme = geolocator.geocode(tema)

        if theme:
            url_base = "https://api.open-meteo.com/v1/forecast"
            config = {
                "latitude": theme.latitude,
                "longitude": theme.longitude,
                "current_weather": "true"
            }
            
            try:
                r = requests.get(url_base, params=config)
                
                if r.status_code == 200:
                    dados = r.json()
                    clima_atual = dados['current_weather']
                    
                    self.temp = clima_atual['temperature']
                    self.vento = clima_atual['windspeed']
                    codigo_clima = clima_atual['weathercode']

                    # Lógica para verificar se está chovendo baseada no 'weathercode'
                    # Códigos de 61 a 67 e 80 a 82 indicam chuva
                    self.esta_chovendo = "Sim" if codigo_clima >= 61 else "Não"

                else:
                    messagebox.showerror("Erro",f"Erro na API: {r.status_code}")
            except Exception as e:
                messagebox.showerror("Erro", f"Erro de conexão: {e}")
        else:
            messagebox.showerror("Local não encontrado.")

        traducao_texto = GoogleTranslator(source='auto', target = 'en').translate(tema)
        partes_url = [
            "https://restcountries.com",
            "v3.1",
            "name",
            traducao_texto
        ]
        url_final = "/".join(partes_url) + "?fullText=true"

        try:
            response = requests.get(url_final, timeout=10)

            if response.status_code == 200:
                dados = response.json()[0]
                
                self.capital = (f"Capital: {dados.get('capital', ['N/A'])[0]}")
                self.populacao = (f"População: {dados.get('population'):,} habitantes")
                bandeira_url = dados.get('flags', {}).get('png')
                
                self.imagem_bytes = None

                if bandeira_url:
                    try:
                        # Baixa a imagem de fato
                        img_res = requests.get(bandeira_url, timeout=10)
                        if img_res.status_code == 200:
                            self.imagem_bytes = img_res.content
                    except:
                        self.imagem_bytes = None

                self.moeda = (f"Moeda: {list(dados.get('currencies', {}).values())[0]['name']}")
            else:
                messagebox.showerror("Erro",f"Erro {response.status_code}: Verifique se o nome '{tema}' está em inglês.")

        except Exception as e:
            messagebox.showerror("Erro", f"Erro de conexão detalhado: {e}")

        return {
            "titulo": self.titulo,
            "capital": self.capital,
            "populacao": self.populacao,
            "bandeira": self.imagem_bytes,
            "moeda": self.moeda,
            "temp": self.temp,
            "vento": self.vento,
            "chuva": self.esta_chovendo,
            "resumo": self.resumo
        }