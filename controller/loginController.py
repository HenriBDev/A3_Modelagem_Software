import os, sys
CURRENT_DIR = os.path.dirname(os.path.abspath(__file__))
PARENT_DIR = os.path.dirname(CURRENT_DIR)
sys.path.append(PARENT_DIR)
from model.loginModel import loginModel

class loginController:
    
    def verificarUsuarioCorreto(Usuario: object) -> bool:
        return type(loginModel.login(Usuario.email, Usuario.senha)) == list
    
    def verificarUsuarioExiste(Usuario: object) -> bool:
        for usuario in loginModel.listar_usuarios():
            if usuario[2] == Usuario.email:
                return True
        
        return False
import os, sys
CURRENT_DIR = os.path.dirname(os.path.abspath(__file__))
PARENT_DIR = os.path.dirname(CURRENT_DIR)
sys.path.append(PARENT_DIR)
from model.loginModel import loginModel

class loginController:
    
    def verificarUsuarioCorreto(Usuario: object) -> bool:
        return type(loginModel.login(Usuario.email, Usuario.senha)) == list
    
    def verificarUsuarioExiste(Usuario: object) -> bool:
        for usuario in loginModel.listar_usuarios():
            if usuario[2] == Usuario.email:
                return True
        
        return False
