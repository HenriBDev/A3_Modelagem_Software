import os
from Controllers.ControllerFactory import ControllerFactory

class View:
    
    def __init__(self):
        nome_view = self.__class__.__name__[:-4]
        self.controller = ControllerFactory().instanciar_controller(nome_view) if f"{nome_view}Controller.py" in os.listdir(os.path.abspath('./Controllers')) else None
        
    @staticmethod
    def view_action(action):
        def wrapper(self, *args, **kwargs):
            os.system('cls' if os.name=='nt' else 'clear')
            retorno = action(self, *args, **kwargs)
            input("Pressione enter para continuar.")
            os.system('cls' if os.name=='nt' else 'clear')
            return retorno
        return wrapper