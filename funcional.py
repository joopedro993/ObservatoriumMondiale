from tkinter import *
import tkinter as tk
from tkinter import ttk
import customtkinter as ctk

class Funcional:
    def __init__(self):
        pass

    def criar_janela(self):
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
        
        self.fileImage = PhotoImage(file="assets/TerraGig.png")
        labelImage = Label(self.janela, image=self.fileImage, bg="#ffffff")
        labelImage.place(x=240, y=380) 

        observatorio_label = Label(self.janela, text="Observatorium Mondiale", font=("Calibri", 48, "bold"), bg="#ffffff", fg="#333333")
        observatorio_label.pack()

        bemvindo_label = Label(self.janela, text="Digite algum país para ver suas informações e sua história!", wraplength=720, font=("Calibri", 28, "bold"), bg="#ffffff", fg="#7E7C7C")
        bemvindo_label.pack(pady=10)

        questEntry = ctk.CTkEntry(self.janela, fg_color="#333333", border_color="#7E7C7C", placeholder_text="Digite...", placeholder_text_color="#7E7C7C", justify= CENTER, width= 680, font= ("Calibri", 24), text_color= "white")
        questEntry.pack()

        questButton = ctk.CTkButton(self.janela, text="Pesquisar", width=200, height=50, border_width=0, corner_radius=10, font=("Calibri", 20), fg_color="#4E4D4D", hover_color="#333333")
        questButton.pack(pady= 30)  

        sairButton = Button(self.janela, text = "sair", command=quit)
        sairButton.pack()