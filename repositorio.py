import sqlite3

class Repositorio:
    def __init__(self):
        self.conexao = sqlite3.connect("mundiale.db")
        self.cursor = self.conexao.cursor()
        self.criar_tabelas()

    def criar_tabelas(self):
        
        self.cursor.execute('''
            CREATE TABLE IF NOT EXISTS usuarios (
                cpf TEXT UNIQUE PRIMARY KEY,
                nome TEXT NOT NULL,
                email TEXT NOT NULL,
                senha TEXT NOT NULL
            )
        ''')
        
        self.cursor.execute('''
            CREATE TABLE IF NOT EXISTS historico (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                pais TEXT,
                cpf_cliente TEXT,
                FOREIGN KEY (cpf_cliente) REFERENCES usuarios(cpf)
            )
        ''')
        
        self.conexao.commit()

    def salvar_usuario(self, usuario):
        
        self.cursor.execute(
        "SELECT COUNT(*) from usuarios WHERE cpf = ?", 
        (usuario.cpf,)
        )
        resultado = self.cursor.fetchone()[0]
        if resultado == 1:
            return False
        
        else:
            self.cursor.execute(
                "INSERT INTO usuarios VALUES (?, ?, ?, ?)", 
                (usuario.cpf, usuario.nome, usuario.email, usuario.senha)
            )
            self.conexao.commit()
            return True
            
    
    def login_usuario(self, cpf, senha):

        self.cursor.execute(
        "SELECT COUNT(*) FROM usuarios WHERE cpf = ? AND senha = ?", 
        (cpf, senha)
        )
        resultado = self.cursor.fetchone()[0]
        if resultado == 1:
            return True
        
        else:
            return False
 
    def salvar_historico(self, pais, cpf_cliente):

        self.cursor.execute("INSERT INTO historico (pais, cpf_cliente) VALUES (?, ?)", 
                       (pais, cpf_cliente))
        self.conexao.commit()

    def deletar_histórico(self,cpf_cliente):
        self.cursor.execute("DELETE FROM historico WHERE cpf_cliente = ?",
                        (cpf_cliente,))
        self.conexao.commit()
    
    def fechar(self):
        self.conexao.close()
