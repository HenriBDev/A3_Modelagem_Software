import os, sys
USUARIO_DIR = os.path.dirname(os.path.abspath("domain/usuario.py"))
sys.path.append(os.path.dirname(USUARIO_DIR))
from domain.usuario import Usuario
import os, sys
MENU_DIR = os.path.dirname(os.path.abspath("menu.py"))
sys.path.append(os.path.dirname(MENU_DIR))
LOGIN_BD_DIR = os.path.dirname(os.path.abspath("model/loginModel.py"))
sys.path.append(os.path.dirname(LOGIN_BD_DIR))
from model.loginModel import loginModel
LOGIN_CONTROLLER_DIR = os.path.dirname(os.path.abspath("controller/loginController.py"))
sys.path.append(os.path.dirname(LOGIN_CONTROLLER_DIR))
from controller.loginController import loginController

class LoginView:                 
    
    def login(self):
        from menu import Menu
        
        while True:
            email = input("Digite seu e-mail: ")
            senha = input("Digite sua senha: ")            
            usuario_encontrado =loginController.verificar_usuario_correto(email,senha)
            if (usuario_encontrado):
                print("Login bem-sucedido!")
                usuario_logado = Usuario(usuario_encontrado[2],usuario_encontrado[3])
                usuario_logado.id = usuario_encontrado[0]
                usuario_logado.nome = usuario_encontrado[1]               
                menu = Menu()
                menu.navegar_menu(usuario_logado)
                break
            else:
                print("E-mail ou senha incorretos. Tente novamente.")

    
    def cadastrar_usuario(self):
        while True:

            novo_email = input("Digite o seu e-mail: ")

            if (loginController.verificarUsuarioExiste(novo_email)):
                print("O e-mail informado já existe. Tente novamente.")
            else:                
                novo_nome = input("Digite o seu nome: ")
                nova_senha = input("Digite a senha para o novo usuário: ")
                novo_usuario = Usuario(novo_email,nova_senha)
                novo_usuario.nome = novo_nome

                if(loginController.cadastrarUsuario(novo_usuario)):
                    print("Novo usuário cadastrado com sucesso!")
                    self.login()
                    break
                else:
                    print("Erro ao cadastrar usuário")
                

    def sair(self):
        sys.exit("Log out realizado com sucesso!")
            

                