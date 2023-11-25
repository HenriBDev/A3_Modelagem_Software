import os
from Factory import Factory

class ViewFactory(Factory):
    
    def __init__(self):
        super().__init__("view", os.path.dirname(os.path.abspath(__file__)))
        
    def instanciar_view(self, nome_view):
        return super().criar_instancia(nome_view)