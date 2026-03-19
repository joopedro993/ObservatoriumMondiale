from tkinter import *
import tkinter as tk
from tkinter import messagebox
import customtkinter as ctk
import requests
from apis import API
from PIL import Image, ImageTk
import io 
from repositorio import Repositorio

apis = API()
repositorio = Repositorio()

class Funcional:
    def __init__(self):
        
        pass

    def limpar_tela(self):
        for widget in self.janela.winfo_children():
            widget.destroy()

    def get_dados(self, dado):
        self.dados = apis.gerar_dados(dado)
        
    def criar_janela(self,cpf):
        self.cpf_cliente = cpf
        def functions(dado):
            self.get_dados(dado)
            self.pesquisa()
        
        def delete():
            repositorio.deletar_histórico(self.cpf_cliente)
            messagebox.showinfo("Histórico", "Histórico apagado com sucesso.")

        self.janela = tk.Toplevel()
        self.janela.resizable(0,0)
        self.janela.config(bg = "#ffffff")
        self.janela.title("Observatorium Mondiale")
        
        larg_tela = self.janela.winfo_screenwidth()
        alt_tela = self.janela.winfo_screenheight()
        pos_x = ((larg_tela // 2) - (1920 // 2))
        pos_y = (alt_tela // 2) - (1080 // 2)
        self.janela.geometry(f"{1920}x{1080}+{pos_x}+{pos_y}")

        self.janela.overrideredirect(True)
        
        self.fileImage = PhotoImage(file="assets/TerraBig.png")
        labelImage = Label(self.janela, image=self.fileImage, bg="#ffffff")
        labelImage.place(x=500, y=380) 

        observatorio_label = Label(self.janela, text="Observatorium Mondiale", font=("Calibri", 48, "bold"), bg="#ffffff", fg="#333333")
        observatorio_label.pack()

        bemvindo_label = Label(self.janela, text="Digite algum país para ver suas informações e sua história!", wraplength=720, font=("Calibri", 28, "bold"), bg="#ffffff", fg="#7E7C7C")
        bemvindo_label.pack(pady=10)

        questEntry = ctk.CTkEntry(self.janela, fg_color="#333333", border_color="#7E7C7C", placeholder_text="Digite...", placeholder_text_color="#7E7C7C", justify= CENTER, width= 680, font= ("Calibri", 24), text_color= "white")
        questEntry.pack()

        questButton = ctk.CTkButton(self.janela, text="Pesquisar", width=200, height=50, border_width=0, corner_radius=10, font=("Calibri", 20), fg_color="#4E4D4D", hover_color="#333333", command = lambda: functions(questEntry.get()))
        questButton.pack(pady= 30)  

        boxFuncional = Frame(self.janela, bg= "white")
        boxFuncional.pack()
        sairButton = ctk.CTkButton(boxFuncional, text="Sair", width=200, height=50, border_width=0, corner_radius=10, font=("Calibri", 20), fg_color="#4E4D4D", hover_color="#333333", command= quit)
        sairButton.pack(side = LEFT, padx = 10)

        deleteButton = ctk.CTkButton(boxFuncional, text="Deletar", width=200, height=50, border_width=0, corner_radius=10, font=("Calibri", 20), fg_color="#4E4D4D", hover_color="#333333", command= delete)
        deleteButton.pack(side =LEFT, padx = 10)

    def pesquisa(self):
        def historico():
            repositorio.salvar_historico(self.dados["titulo"], self.cpf_cliente)

        historico()
        self.limpar_tela()

        if self.dados.get("bandeira"):
            arquivo_memoria = io.BytesIO(self.dados["bandeira"])
            imagem = Image.open(arquivo_memoria)
            imagem = imagem.resize((480, 320), Image.LANCZOS)
            self.imagem_tk = ImageTk.PhotoImage(imagem)


        frame_pesquisa = tk.Frame(self.janela, bg="#ffffff")
        frame_pesquisa.pack(fill="both", expand=True)

        titulo = Label(frame_pesquisa, text=str(self.dados["titulo"]), font=("Calibri", 56, "bold"), fg="#333333", bg = "white")
        titulo.pack(anchor = W, padx = 85,pady = 20)

        boxBig = Frame(frame_pesquisa, bg= "white")
        boxBig.pack(anchor=W, padx = 32,pady=10)

        boxGeo = Frame(boxBig, bg= "white")
        boxGeo.pack( padx = 10,pady=20, side= LEFT)

        Label(boxGeo, text = "Dados Geográficos", font= ("Calibri", 32, "bold"), fg="#333333", bg = "white").pack(anchor = W,pady=20)
        
        Label(boxGeo, text=str(self.dados["capital"]), font=("Calibri", 24, "bold"), fg="#333333", bg = "white", justify=LEFT).pack(anchor = W)
        Label(boxGeo, text=str(self.dados["moeda"]), font=("Calibri", 24, "bold"), fg="#333333", bg = "white", justify=LEFT).pack(anchor= W)
        Label(boxGeo, text=str(self.dados["populacao"]), font=("Calibri", 24, "bold"), fg="#333333", bg = "white", justify=LEFT).pack(anchor=W)

        bandeiraImage = Label(self.janela, image=self.imagem_tk, bg="#ffffff")
        bandeiraImage.place(x=1260, y=20)
        
        labelImage = Label(self.janela, image=self.fileImage, bg="#ffffff")
        labelImage.place(x=1280, y=420) 

        boxClima = Frame(boxBig, bg= "white")
        boxClima.pack(padx = 10,pady=20, side= LEFT)

        Label(boxClima, text="Dados Climáticos", font=("Calibri", 32, "bold"), fg="#333333", bg = "white").pack(anchor=W,pady=20)

        Label(boxClima, text=f"🌡️Temperatura média atual: {str(self.dados["temp"])}°C", font=("Calibri", 24, "bold"), fg="#333333", bg = "white", justify=LEFT).pack(anchor = W)
        Label(boxClima, text=f"💨      Velocidade Média do Vento: {str(self.dados["vento"])}Km/h", font=("Calibri", 24, "bold"), fg="#333333", bg = "white", justify=LEFT).pack(anchor= W)
        Label(boxClima, text=f"🌦️Está chovendo na maior parte do país? {str(self.dados["chuva"])}", font=("Calibri", 24, "bold"), fg="#333333", bg = "white", justify=LEFT).pack(anchor=W)
        
        Label(frame_pesquisa, text="📜Uma Breve História", font=("Calibri", 32, "bold"), fg="#333333", bg = "white").pack(anchor=W, padx = 32,pady=20)

        Label(frame_pesquisa, text=str(self.dados["resumo"]), font=("Calibri", 20, "bold"), fg="#333333", bg = "white", justify=LEFT, wraplength=1120).pack(anchor=W, padx = 32)

        sairButton = ctk.CTkButton(self.janela, text= "Sair", width= 200, height= 50, border_width= 0, corner_radius= 10, font= ("Calibri", 20), fg_color="#4E4D4D", hover_color="#333333", command= lambda: self.criar_janela(self.cpf_cliente))
        sairButton.pack(anchor= W, side= BOTTOM, padx= 80, pady= 30)