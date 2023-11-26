from Views.View import View
from Domains.Usuario import Usuario

class UsuarioView(View): 
    
    @View.view_action
    def logar_usuario(self) -> object|bool:

        print("Logando usuário")
        email = input("Digite seu e-mail: ")
        senha = input("Digite sua senha: ")
        if (self.controller.usuario_existe(email, senha)):
            usuario = Usuario(*self.controller.buscar_usuario(email, senha)[0])
            print("\nUsuário logado com sucesso!")
            return usuario
        else:
            print("\nEmail e/ou senha incorretos")
            return False
        
    @View.view_action
    def cadastrar_usuario(self) -> bool:

        print("Cadastrando usuário")
        novo_email = input("Digite o seu e-mail: ")

        if (self.controller.email_ja_cadastrado(novo_email)):
            print("O e-mail informado já existe. Digite outro email")
        else:
            novo_nome = input("Digite o seu nome: ")
            nova_senha = input("Digite a senha para o novo usuário: ")

            self.controller.cadastrar_usuario(novo_email, nova_senha, novo_nome) 
            print("\nUsuário cadastrado com sucesso!")
                