import os
from Factory import Factory

class ControllerFactory(Factory):
    
    def __init__(self):
        super().__init__("controller", os.path.dirname(os.path.abspath(__file__)))
        
    def create_controller(self, nome_controller):
        return super().create_instancia(nome_controller)