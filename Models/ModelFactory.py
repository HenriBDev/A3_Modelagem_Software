import os
from MVCFactory import MVCFactory

class ModelFactory(MVCFactory):
    
    def __init__(self):
        super().__init__("model", os.path.dirname(os.path.abspath(__file__)))