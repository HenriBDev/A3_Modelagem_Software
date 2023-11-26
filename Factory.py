import importlib
import os

class Factory:
    
    def __init__(self, tipo_factory: str, diretorio_factory: str) -> None:
        
        self.tipo_factory = tipo_factory.capitalize()
        
        self.tipo_instancias = {
            nome_arquivo[:- (3 + len(tipo_factory))]: getattr(importlib.import_module(f"{self.tipo_factory}s.{nome_arquivo[:-3]}"), nome_arquivo[:-3]) 
        for nome_arquivo in os.listdir(diretorio_factory) if nome_arquivo.endswith(f"{self.tipo_factory}.py")}
        
    def criar_instancia(self, nome_instancia: str) -> object:
        
        nome_instancia = nome_instancia.capitalize()
        
        if nome_instancia not in self.tipo_instancias.keys():
            
            raise Exception(f"{self.tipo_factory} inexistente")
        
        return self.tipo_instancias[nome_instancia.capitalize()]()