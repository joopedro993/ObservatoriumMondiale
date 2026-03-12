from tkinter import *
import tkinter as tk
from tkinter import ttk
import customtkinter as ctk

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


        self.janela.iconbitmap("assets/assets/mapico.ico")

        fileImage = PhotoImage(file="assets/assets/TerraBig.png")
        labelImage = Label(self.janela, image=fileImage, bg="#ffffff")
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
        
        cadastrar_button = ctk.CTkButton(boxEscolha, text="Cadastrar", width=200, height=50, border_width=0, corner_radius=10, font=("Calibri", 20), fg_color="#4E4D4D", hover_color="#333333")
        cadastrar_button.pack(side = LEFT, padx=10)

        login_button = ctk.CTkButton(boxEscolha, text="Login", width=200, height=50, border_width=0, corner_radius=10, font=("Calibri", 20), fg_color="#4E4D4D", hover_color="#333333")
        login_button.pack(side = LEFT, padx=10)

        creditsText = ctk.CTkLabel(self.janela, text="@Desenvolvido por: Alexandre, Elias Gabriel, João Pedro e Maria Victória. 3º DS", font=("Calibri", 15), bg_color="#ffffff", text_color="#7E7C7C", wraplength=300, justify = RIGHT, corner_radius=5)
        creditsText.pack(anchor = E, side=BOTTOM, pady=10)
        






        self.janela.mainloop()