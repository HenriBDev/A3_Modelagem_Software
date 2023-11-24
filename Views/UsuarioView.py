# Python libs
import sys

from Controllers.ControllerFactory import ControllerFactory
from Domains.Usuario import Usuario

class UsuarioView: 
    
    def logar_usuario(self):
        
        usuario_controller = ControllerFactory().create_controller('usuario')
        
        while True:
            email = input("Digite seu e-mail: ")
            senha = input("Digite sua senha: ")            
            usuario_encontrado = usuario_controller.validar_dados(email, senha)
            if (usuario_encontrado):
                print("Login bem-sucedido!")
                return Usuario(*usuario_controller.buscar_usuario(email, senha)[0])
            else:
                if input("E-mail ou senha incorretos. Deseja voltar para o menu inicial? [S/N]\n").strip().upper() == "S": return False
    
    def cadastrar_usuario(self):
        
        usuario_controller = ControllerFactory().create_controller('usuario')
        
        while True:

            novo_email = input("Digite o seu e-mail: ")

            if (usuario_controller.verificar_usuario_existe(novo_email)):
                print("O e-mail informado já existe. Digite outro email.")
            else:                
                novo_nome = input("Digite o seu nome: ")
                nova_senha = input("Digite a senha para o novo usuário: ")

                usuario_controller.cadastrar_usuario(novo_email, nova_senha, novo_nome)
                usuario_cadastrado = usuario_controller.buscar_usuario(novo_email, nova_senha)

                if(usuario_cadastrado):
                    print("Usuário cadastrado com sucesso!")
                    return usuario_cadastrado
                else:
                    print("Erro ao cadastrar usuário. Deseja voltar para o menu inicial? [S/N]")
                