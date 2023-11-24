import os
from Factory import Factory

class ModelFactory(Factory):
    
    def __init__(self):
        super().__init__("model", os.path.dirname(os.path.abspath(__file__)))
        
    def create_model(self, nome_model):
        return super().create_instancia(nome_model)