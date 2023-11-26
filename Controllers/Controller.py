import os
from Models.ModelFactory import ModelFactory

class Controller:
    
    def __init__(self):
        nome_controller = self.__class__.__name__[:-10]
        self.model = ModelFactory().criar_instancia(nome_controller) if f"{nome_controller}Model.py" in os.listdir(os.path.abspath('./Models')) else None