import importlib
import os

DIRETORIO_ATUAL = os.path.dirname(os.path.abspath(__file__))
NOME_ARQUIVO_ATUAL = os.path.basename(__file__)
NOMES_IGNORADOS = ['__pycache__', '__init__.py', NOME_ARQUIVO_ATUAL]

class ModelFactory:
    
    def __init__(self):
        self.models = {
            nomeModel[:-8]: getattr(importlib.import_module(f"Models.{nomeModel[:-3]}"), nomeModel[:-3]) 
        for nomeModel in os.listdir(DIRETORIO_ATUAL) if nomeModel not in NOMES_IGNORADOS}
        
    def create_model(self, nome_model):
        
        nome_model = nome_model.capitalize()
        
        if nome_model not in self.models.keys():
            
            raise Exception("Model inexistente")
        
        return self.models[nome_model.capitalize()]()