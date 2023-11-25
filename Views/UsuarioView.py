# Python libs
import sys

from Views.View import View
from Domains.Usuario import Usuario

class UsuarioView(View): 
    
    def logar_usuario(self):
        
        while True:
            email = input("Digite seu e-mail: ")
            senha = input("Digite sua senha: ")            
            usuario_encontrado = self.controller.validar_dados(email, senha)
            if (usuario_encontrado):
                print("Login bem-sucedido!")
                return Usuario(*self.controller.buscar_usuario(email, senha)[0])
            else:
                if input("E-mail ou senha incorretos. Deseja voltar para o menu inicial? [S/N]\n(N)").strip().upper() == "S": return False
    
    def cadastrar_usuario(self):
        
        while True:

            novo_email = input("Digite o seu e-mail: ")

            if (self.controller.verificar_usuario_existe(novo_email)):
                print("O e-mail informado já existe. Digite outro email.")
            else:                
                novo_nome = input("Digite o seu nome: ")
                nova_senha = input("Digite a senha para o novo usuário: ")

                self.controller.cadastrar_usuario(novo_email, nova_senha, novo_nome)
                usuario_cadastrado = self.controller.buscar_usuario(novo_email, nova_senha)

                if(usuario_cadastrado):
                    print("Usuário cadastrado com sucesso!")
                    return usuario_cadastrado
                else:
                    print("Erro ao cadastrar usuário. Deseja voltar para o menu inicial? [S/N]")
                