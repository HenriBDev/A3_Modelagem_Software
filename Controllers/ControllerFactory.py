import os
from MVCFactory import MVCFactory

class ControllerFactory(MVCFactory):
    
    def __init__(self):
        super().__init__("controller", os.path.dirname(os.path.abspath(__file__)))