import importlib
import os

DIRETORIO_ATUAL = os.path.dirname(os.path.abspath(__file__))
NOME_ARQUIVO_ATUAL = os.path.basename(__file__)
NOMES_IGNORADOS = ['__pycache__', '__init__.py', NOME_ARQUIVO_ATUAL]

class ControllerFactory:
    
    def __init__(self):
        self.controllers = {
            nomeController[:-13]: getattr(importlib.import_module(f"Controllers.{nomeController[:-3]}"), nomeController[:-3]) 
        for nomeController in os.listdir(DIRETORIO_ATUAL) if nomeController not in NOMES_IGNORADOS}
        
    def create_controller(self, nome_controller):
        
        nome_controller = nome_controller.capitalize()
        
        if nome_controller not in self.controllers.keys():
            
            raise Exception("Controller inexistente")
        
        return self.controllers[nome_controller.capitalize()]()