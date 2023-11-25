import os
from Controllers.ControllerFactory import ControllerFactory

class View:
    
    def __init__(self):
        nome_view = self.__class__.__name__[:-4]
        self.controller = ControllerFactory().instanciar_controller(nome_view) if f"{nome_view}Controller.py" in os.listdir(os.path.abspath('./Controllers')) else None