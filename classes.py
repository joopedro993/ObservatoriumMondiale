class Cadastro:
    def __init__(self,cpf,nome,email,senha):
        self.cpf=cpf
        self.nome=nome
        self.email=email
        self.senha=senha
        


    def __str__ (self):
        return f'''
    CPF: {self.cpf}
    Nome: {self.nome}
    Email: {self.email}
    Senha: {self.senha}
    '''
