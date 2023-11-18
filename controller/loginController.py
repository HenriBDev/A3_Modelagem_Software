import os, sys
CURRENT_DIR = os.path.dirname(os.path.abspath(__file__))
PARENT_DIR = os.path.dirname(CURRENT_DIR)
sys.path.append(PARENT_DIR)
from model.loginModel import loginModel

class loginController:
    
    def verificarUsuarioCorreto(email,senha) -> bool:        
        return type(loginModel.login(email, senha)) == tuple
    
    def verificarUsuarioExiste(email) -> bool:
        for usuario in loginModel.listar_usuario():
            if usuario[2] == email:
                return True
        
        return False
    def cadastrarUsuario(Usuario: object) -> bool:
        return loginModel.cadastrar_usuario(Usuario);
