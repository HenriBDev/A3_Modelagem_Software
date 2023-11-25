from Views.View import View
from Domains.Usuario import Usuario

class UsuarioView(View): 
    
    def logar_usuario(self) -> object|bool:

        print("Logando usuário")
        email = input("Digite seu e-mail: ")
        senha = input("Digite sua senha: ")
        if (self.controller.usuario_existe(email, senha)):
            return Usuario(*self.controller.buscar_usuario(email, senha)[0])
        else:
            input(
                "\n"
                "Email e/ou senha incorretos\n"
                "Pressione enter para continuar"
            )
            return False
    
    def cadastrar_usuario(self) -> bool:

        print("Cadastrando usuário")
        novo_email = input("Digite o seu e-mail: ")

        if (self.controller.email_ja_cadastrado(novo_email)):
            input(
                "O e-mail informado já existe. Digite outro email\n"
                "Pressione enter para continuar"
            )
            return False
        else:
            novo_nome = input("Digite o seu nome: ")
            nova_senha = input("Digite a senha para o novo usuário: ")

            self.controller.cadastrar_usuario(novo_email, nova_senha, novo_nome)
            usuario_cadastrado = bool(self.controller.buscar_usuario(novo_email, nova_senha))
            if usuario_cadastrado: input(
                "\n"
                "Usuário cadastrado com sucesso!\n"
                "Pressione enter para continuar"
            )
            return usuario_cadastrado
                