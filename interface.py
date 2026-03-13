from tkinter import *
import tkinter as tk
from tkinter import ttk
import customtkinter as ctk
from funcional import Funcional

funcional = Funcional()

class Janela:
    def __init__(self):
        self.janela = tk.Tk()
        self.janela.resizable(0,0)
        self.janela.config(bg = "#ffffff")
        self.janela.title("Observatorium Mondiale")
       
        larg_tela = self.janela.winfo_screenwidth()
        alt_tela = self.janela.winfo_screenheight()
        pos_x = ((larg_tela // 2) - (1080 // 2))
        pos_y = (alt_tela // 2) - (720 // 2)
        self.janela.geometry(f"{1080}x{720}+{pos_x}+{pos_y}")


        self.janela.iconbitmap("assets/mapico.ico")

        self.janela.overrideredirect(True)
        
        self.fileImage = PhotoImage(file="assets/TerraBig.png")
        labelImage = Label(self.janela, image=self.fileImage, bg="#ffffff")
        labelImage.place(x=85, y=300) 

        observatorio_label = Label(self.janela, text="Observatorium Mondiale", font=("Calibri", 48, "bold"), bg="#ffffff", fg="#333333")
        observatorio_label.pack()

        text = Label(self.janela, text="O mundo em dados e documentos!", font=("Calibri", 24, "bold"), bg="#ffffff", fg="#7E7C7C")
        text.pack()

        bemvindo_label = Label(self.janela, text="Bem-vindo(a)!", font=("Calibri", 28, "bold"), bg="#ffffff", fg="#333333")
        bemvindo_label.pack(pady=10)

        escolha_label = Label(self.janela, text="Escolha uma opção para começar:", font=("Calibri", 20), bg="#ffffff", fg="#7E7C7C")
        escolha_label.pack(pady=10)

        boxEscolha = Frame(self.janela, bg="#ffffff")
        boxEscolha.pack()
        
        cadastrar_button = ctk.CTkButton(boxEscolha, text="Cadastrar", width=200, height=50, border_width=0, corner_radius=10, font=("Calibri", 20), fg_color="#4E4D4D", hover_color="#333333", command = self.tela_cadastro)
        cadastrar_button.pack(side = LEFT, padx=10)

        login_button = ctk.CTkButton(boxEscolha, text="Login", width=200, height=50, border_width=0, corner_radius=10, font=("Calibri", 20), fg_color="#4E4D4D", hover_color="#333333", command= self.tela_login)
        login_button.pack(side = LEFT, padx=10)

        creditsText = ctk.CTkLabel(self.janela, text="@Desenvolvido por: Alexandre, Elias Gabriel, João Pedro e Maria Victória. 3º DS", font=("Calibri", 15), bg_color="#ffffff", text_color="#7E7C7C", wraplength=300, justify = RIGHT, corner_radius=5)
        creditsText.pack(anchor = E, side=BOTTOM, pady=10)
        
        sairButton = ctk.CTkButton(self.janela, text= "Sair", width= 200, height= 50, border_width= 0, corner_radius= 10, font= ("Calibri", 20), fg_color="#4E4D4D", hover_color="#333333", command= quit)
        sairButton.pack(anchor= E, side= BOTTOM)


        self.janela.mainloop()
    
    def limpar_tela(self):
        for widget in self.janela.winfo_children():
            widget.destroy()
            
    def formatar_cpf(self, event):
        texto = event.widget.get()

        numeros = ''.join(filter(str.isdigit, texto))

        if len(numeros) > 3:
            numeros = numeros[:3] + '.' + numeros[3:]

        if len(numeros) > 7:
            numeros = numeros[:7] + '.' + numeros[7:]

        if len(numeros) > 11:
            numeros = numeros[:11] + '-' + numeros[11:]

        event.widget.delete(0, "end")
        event.widget.insert(0, numeros[:14])

    def tela_login(self):
        def nova_janela():
            funcional.criar_janela()

        self.limpar_tela()
        
        frame_login = tk.Frame(self.janela, bg="#ffffff")
        frame_login.pack(fill="both", expand=True)
        
        labelImage = Label(self.janela, image=self.fileImage, bg="#ffffff")
        labelImage.place(x=400, y=10) 

        titulo = Label(frame_login, text="ObMondi", font=("Calibri", 32, "bold"), fg="#333333", bg = "white")
        titulo.pack(anchor = W, padx = 85)
        
        loginText = Label(frame_login, text="Login", font=("Calibri", 28, "bold"), fg="#333333", bg = "white")
        loginText.pack(anchor = W, padx = 130)

        boxCpf = Frame(frame_login, bg= "white")
        boxCpf.pack(anchor= W, padx= 50)
                
        cpfText = Label(boxCpf, text= "CPF:", fg= "#7E7C7C", bg= "white", font= ("Calibri",24, "bold"))
        cpfText.pack()
        
        cpfEntry = ctk.CTkEntry(boxCpf, fg_color="#333333", border_color="#333333", placeholder_text="CPF", placeholder_text_color="#7E7C7C", justify= CENTER, width= 250, font= ("Calibri", 24), text_color= "white")
        cpfEntry.pack()

        cpfEntry.bind('<KeyRelease>', self.formatar_cpf)
        
        boxSenha = Frame(frame_login, bg= "white")
        boxSenha.pack(anchor= W, padx=50)
                
        senhaText = Label(boxSenha, text= "Senha:", fg= "#7E7C7C", bg= "white", font= ("Calibri",24, "bold"))
        senhaText.pack()
        
        senhaEntry = ctk.CTkEntry(boxSenha, fg_color="#333333", border_color="#333333", placeholder_text="Senha", placeholder_text_color="#7E7C7C", justify= CENTER, width= 250, font= ("Calibri", 24), text_color= "white", show= "☸")
        senhaEntry.pack()
        
        loginButton = ctk.CTkButton(boxSenha, text="Login", width=200, height=50, border_width=0, corner_radius=10, font=("Calibri", 20), fg_color="#4E4D4D", hover_color="#333333", command= nova_janela)
        loginButton.pack(pady= 30)       
        
        boxAux = Frame(frame_login, bg= "white")
        boxAux.pack(anchor= W, padx=50)
        
        aux = ctk.CTkLabel(boxAux, text="Se não tiver conta, saia e na tela inicial clique em cadastrar.", font=("Calibri", 15), bg_color="#ffffff", text_color="#7E7C7C", wraplength=300, justify = CENTER, corner_radius=5)
        aux.pack(anchor = E, side=BOTTOM, pady=10)
        
        sairButton = ctk.CTkButton(self.janela, text= "Sair", width= 200, height= 50, border_width= 0, corner_radius= 10, font= ("Calibri", 20), fg_color="#4E4D4D", hover_color="#333333", command= quit)
        sairButton.pack(anchor= W, side= BOTTOM, padx= 80, pady= 30)
        
    def tela_cadastro(self):
        self.limpar_tela()
        
        frame_cadastro = tk.Frame(self.janela, bg="#ffffff")
        frame_cadastro.pack(fill="both", expand=True)
        
        labelImage = Label(self.janela, image=self.fileImage, bg="#ffffff")
        labelImage.place(x=400, y=10) 

        titulo = Label(frame_cadastro, text="ObMondi", font=("Calibri", 32, "bold"), fg="#333333", bg = "white")
        titulo.pack(anchor = W, padx = 85)
        
        loginText = Label(frame_cadastro, text="Cadastro", font=("Calibri", 28, "bold"), fg="#333333", bg = "white")
        loginText.pack(anchor = W, padx = 105)

        boxCpf = Frame(frame_cadastro, bg= "white")
        boxCpf.pack(anchor= W, padx= 50)
                
        cpfText = Label(boxCpf, text= "CPF:", fg= "#7E7C7C", bg= "white", font= ("Calibri",24, "bold"))
        cpfText.pack()
        
        cpfEntry = ctk.CTkEntry(boxCpf, fg_color="#333333", border_color="#333333", placeholder_text="CPF", placeholder_text_color="#7E7C7C", justify= CENTER, width= 250, font= ("Calibri", 24), text_color= "white")
        cpfEntry.pack()
        cpfEntry.bind('<KeyRelease>', self.formatar_cpf)
        
        boxUsuario = Frame(frame_cadastro, bg= "white")
        boxUsuario.pack(anchor= W, padx=50)
                
        usuarioText = Label(boxUsuario, text= "Usuário:", fg= "#7E7C7C", bg= "white", font= ("Calibri",24, "bold"))
        usuarioText.pack()
        
        usuarioEntry = ctk.CTkEntry(boxUsuario, fg_color="#333333", border_color="#333333", placeholder_text="Usuário", placeholder_text_color="#7E7C7C", justify= CENTER, width= 250, font= ("Calibri", 24), text_color= "white")
        usuarioEntry.pack()
        
        boxEmail = Frame(frame_cadastro, bg= "white")
        boxEmail.pack(anchor= W, padx=50)
                
        emailText = Label(boxEmail, text= "E-Mail:", fg= "#7E7C7C", bg= "white", font= ("Calibri",24, "bold"))
        emailText.pack()
        
        emailEntry = ctk.CTkEntry(boxEmail, fg_color="#333333", border_color="#333333", placeholder_text="E-Mail", placeholder_text_color="#7E7C7C", justify= CENTER, width= 250, font= ("Calibri", 24), text_color= "white")
        emailEntry.pack()
        
        boxSenha = Frame(frame_cadastro, bg= "white")
        boxSenha.pack(anchor= W, padx=50)
                
        senhaText = Label(boxSenha, text= "Senha:", fg= "#7E7C7C", bg= "white", font= ("Calibri",24, "bold"))
        senhaText.pack()
        
        senhaEntry = ctk.CTkEntry(boxSenha, fg_color="#333333", border_color="#333333", placeholder_text="Senha", placeholder_text_color="#7E7C7C", justify= CENTER, width= 250, font= ("Calibri", 24), text_color= "white", show= "☸")
        senhaEntry.pack()
        
        cadButton = ctk.CTkButton(boxSenha, text="Cadastrar", width=200, height=50, border_width=0, corner_radius=10, font=("Calibri", 20), fg_color="#4E4D4D", hover_color="#333333", command= self.tela_login)
        cadButton.pack(pady= 30)       
        
        sairButton = ctk.CTkButton(self.janela, text= "Sair", width= 200, height= 50, border_width= 0, corner_radius= 10, font= ("Calibri", 20), fg_color="#4E4D4D", hover_color="#333333", command= quit)
        sairButton.pack(anchor= W, side= BOTTOM, padx= 80, pady= 30)
        