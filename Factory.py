import importlib
import os

class Factory:
    
    tipo_factory = None
    
    def __init__(self, tipo_factory, diretorio_factory):
        
        self.tipo_factory = tipo_factory.capitalize()
        
        nomes_ignorados = ['__pycache__', '__init__.py', f"{self.tipo_factory}Factory.py"]
        
        self.tipo_instancias = {
            nome_classe[:- (3 + len(tipo_factory))]: getattr(importlib.import_module(f"{self.tipo_factory}s.{nome_classe[:-3]}"), nome_classe[:-3]) 
        for nome_classe in os.listdir(diretorio_factory) if nome_classe not in nomes_ignorados}
        
    def create_instancia(self, nome_instancia):
        
        nome_instancia = nome_instancia.capitalize()
        
        if nome_instancia not in self.tipo_instancias.keys():
            
            raise Exception(f"{self.tipo_factory} inexistente")
        
        return self.tipo_instancias[nome_instancia.capitalize()]()