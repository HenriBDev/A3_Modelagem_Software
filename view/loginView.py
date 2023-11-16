import os, sys
USUARIO_DIR = os.path.dirname(os.path.abspath("domain/usuario.py"))
sys.path.append(os.path.dirname(USUARIO_DIR))
from domain.usuario import Usuario
import os, sys
MENU_DIR = os.path.dirname(os.path.abspath("menu.py"))
sys.path.append(os.path.dirname(MENU_DIR))
LOGIN_BD_DIR = os.path.dirname(os.path.abspath("model/loginView.py"))
sys.path.append(os.path.dirname(LOGIN_BD_DIR))
from model.loginModel import loginModel

class LoginView: 
    
            
    def exibir_mensagem(self, mensagem):
        print(mensagem)

    def login(self):
        from menu import Menu
        while True:
            email = input("Digite seu e-mail: ")
            senha = input("Digite sua senha: ")
            user = loginModel.login(email,senha)
            usuario= Usuario(user[1],user[2],user[3])

            if email in usuario.email and usuario.senha == senha:
                self.exibir_mensagem("Login bem-sucedido!")
                menu = Menu()
                menu.navegar_menu()
                break
            else:
                self.exibir_mensagem("E-mail ou senha incorretos. Tente novamente.")
    
    def cadastrar_usuario(self):
        while True:

            novo_email = input("Digite o seu e-mail: ")

            if novo_email in self.usuario.email:
                self.exibir_mensagem("O e-mail informado já existe. Tente novamente.")
            else:                
                novo_nome = input("Digite o seu nome: ")
                nova_senha = input("Digite a senha para o novo usuário: ")
                novo_usuario = Usuario(novo_nome,novo_email,nova_senha)

                loginModel.cadastrar_usuario(novo_usuario)
                loginModel.listar_usuario()
                self.exibir_mensagem("Novo usuário cadastrado com sucesso!")                
                break

    def sair(self):
        self.exibir_mensagem("Log out realizado com sucesso!")
        self.login()

                