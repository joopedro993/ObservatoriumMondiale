from tkinter import *
import tkinter as tk
from tkinter import messagebox
import customtkinter as ctk
import requests
from apis import API
from PIL import Image, ImageTk
import io

apis = API()

class Funcional:
    def __init__(self):
        pass

    def limpar_tela(self):
        for widget in self.janela.winfo_children():
            widget.destroy()

    def get_dados(self, dado):
        self.dados = apis.gerar_dados(dado)
        
    def criar_janela(self):
        def functions(dado):
            self.get_dados(dado)
            self.pesquisa()
            
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

        sairButton = ctk.CTkButton(self.janela, text="Sair", width=200, height=50, border_width=0, corner_radius=10, font=("Calibri", 20), fg_color="#4E4D4D", hover_color="#333333", command= quit)
        sairButton.pack()

    def pesquisa(self):

        self.limpar_tela()

        if self.dados.get("bandeira"):
            arquivo_memoria = io.BytesIO(self.dados["bandeira"])
            imagem = Image.open(arquivo_memoria)
            imagem = imagem.resize((300, 200), Image.LANCZOS)
            self.imagem_tk = ImageTk.PhotoImage(imagem)


        frame_login = tk.Frame(self.janela, bg="#ffffff")
        frame_login.pack(fill="both", expand=True)

        titulo = Label(frame_login, text=str(self.dados["titulo"]), font=("Calibri", 48, "bold"), fg="#333333", bg = "white")
        titulo.pack(anchor = W, padx = 85)
        
        Label(frame_login, text=str(self.dados["capital"]), font=("Calibri", 28, "bold"), fg="#333333", bg = "white").pack(anchor = W)
        Label(frame_login, text=str(self.dados["moeda"]), font=("Calibri", 28, "bold"), fg="#333333", bg = "white").pack(anchor= W)
        Label(frame_login, text=str(self.dados["populacao"]), font=("Calibri", 28, "bold"), fg="#333333", bg = "white").pack(anchor=W)

        bandeiraImage = Label(self.janela, image=self.imagem_tk, bg="#ffffff")
        bandeiraImage.pack()
        
        labelImage = Label(self.janela, image=self.fileImage, bg="#ffffff")
        labelImage.place(x=1280, y=420) 

        boxCpf = Frame(frame_login, bg= "white")
        boxCpf.pack(anchor= W, padx= 50)
                
        cpfText = Label(boxCpf, text= "CPF:", fg= "#7E7C7C", bg= "white", font= ("Calibri",24, "bold"))
        cpfText.pack()
        
        cpfEntry = ctk.CTkEntry(boxCpf, fg_color="#333333", border_color="#333333", placeholder_text="CPF", placeholder_text_color="#7E7C7C", justify= CENTER, width= 250, font= ("Calibri", 24), text_color= "white")
        cpfEntry.pack()
        
        boxSenha = Frame(frame_login, bg= "white")
        boxSenha.pack(anchor= W, padx=50)
                
        senhaText = Label(boxSenha, text= "Senha:", fg= "#7E7C7C", bg= "white", font= ("Calibri",24, "bold"))
        senhaText.pack()
        
        senhaEntry = ctk.CTkEntry(boxSenha, fg_color="#333333", border_color="#333333", placeholder_text="Senha", placeholder_text_color="#7E7C7C", justify= CENTER, width= 250, font= ("Calibri", 24), text_color= "white", show= "☸")
        senhaEntry.pack()
        
        loginButton = ctk.CTkButton(boxSenha, text="Login", width=200, height=50, border_width=0, corner_radius=10, font=("Calibri", 20), fg_color="#4E4D4D", hover_color="#333333")
        loginButton.pack(pady= 30)       
        
        boxAux = Frame(frame_login, bg= "white")
        boxAux.pack(anchor= W, padx=50)
        
        aux = ctk.CTkLabel(boxAux, text="Se não tiver conta, saia e na tela inicial clique em cadastrar.", font=("Calibri", 15), bg_color="#ffffff", text_color="#7E7C7C", wraplength=300, justify = CENTER, corner_radius=5)
        aux.pack(anchor = E, side=BOTTOM, pady=10)
        
        sairButton = ctk.CTkButton(self.janela, text= "Sair", width= 200, height= 50, border_width= 0, corner_radius= 10, font= ("Calibri", 20), fg_color="#4E4D4D", hover_color="#333333", command= quit)
        sairButton.pack(anchor= W, side= BOTTOM, padx= 80, pady= 30)