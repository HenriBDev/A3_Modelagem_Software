import importlib
import os

DIRETORIO_ATUAL = os.path.dirname(os.path.abspath(__file__))
NOME_ARQUIVO_ATUAL = os.path.basename(__file__)
NOMES_IGNORADOS = ['__pycache__', '__init__.py', NOME_ARQUIVO_ATUAL]

class ViewFactory:
    
    def __init__(self):
        self.views = {
            nomeView[:-7]: getattr(importlib.import_module(f"Views.{nomeView[:-3]}"), nomeView[:-3]) 
        for nomeView in os.listdir(DIRETORIO_ATUAL) if nomeView not in NOMES_IGNORADOS}
        
    def create_view(self, nome_view):
        
        nome_view = nome_view.capitalize()
        
        if nome_view not in self.views.keys():
            
            raise Exception("View inexistente")
        
        return self.views[nome_view.capitalize()]()