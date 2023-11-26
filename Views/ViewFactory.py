import os
from MVCFactory import MVCFactory

class ViewFactory(MVCFactory):
    
    def __init__(self):
        super().__init__("view", os.path.dirname(os.path.abspath(__file__)))