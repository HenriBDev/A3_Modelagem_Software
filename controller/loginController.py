import os, sys
CURRENT_DIR = os.path.dirname(os.path.abspath(__file__))
PARENT_DIR = os.path.dirname(CURRENT_DIR)
sys.path.append(PARENT_DIR)
from model.loginModel import loginModel

class loginController:
    
    def verificar_usuario_correto(email,senha) -> bool:  
        usuario = loginModel.login(email, senha)
        if type(usuario) == tuple:
            return usuario
    
    def verificar_usuario_existe(email) -> bool:
        for usuario in loginModel.listar_usuario():
            if usuario[2] == email:
                return True
        
        return False
    
    def cadastrar_usuario(Usuario: object):
        return loginModel.cadastrar_usuario(Usuario)

