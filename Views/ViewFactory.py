import os
from Factory import Factory

class ViewFactory(Factory):
    
    def __init__(self):
        super().__init__("view", os.path.dirname(os.path.abspath(__file__)))
        
    def create_view(self, nome_view):
        return super().create_instancia(nome_view)