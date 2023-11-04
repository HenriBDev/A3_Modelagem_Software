import os, sys
USUARIO_DIR = os.path.dirname(os.path.abspath("domain/usuario.py"))
sys.path.append(os.path.dirname(USUARIO_DIR))
from domain.usuario import Usuario
import os, sys
MENU_DIR = os.path.dirname(os.path.abspath("menu.py"))
sys.path.append(os.path.dirname(MENU_DIR))
from menu import Menu
class LoginView: 
    usuario = Usuario ("Abraão","teste","123");
            
    def exibir_mensagem(self, mensagem):
        print(mensagem)

    def login(self):
        while True:
            email = input("Digite seu e-mail: ")
            senha = input("Digite sua senha: ")

            if email in self.usuario.email and self.usuario.senha == senha:
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
                self.exibir_mensagem("Novo usuário cadastrado com sucesso!")                
                break

if __name__ == '__main__':
    view = LoginView()
    view.login()
    view.cadastrar_usuario()
                