import os, sys
MENU_DIR = os.path.dirname(os.path.abspath("menu.py"))
sys.path.append(os.path.dirname(MENU_DIR))
from menu import Menu
class Main:
    def __init__(self):
        self
        
    def main(self):
     menu = Menu() 
     menu.exibir_menu_inicial()
        

if __name__=="__main__":
    init  = Main();
    init.main()