import os, sys
CURRENT_DIR = os.path.dirname(os.path.abspath("view/loginView.py"))
sys.path.append(os.path.dirname(CURRENT_DIR))
from view.loginView import LoginView
class Main:
    def __init__(self):
        self
        
    def main(self): 
        login = LoginView()
        login.login()

if __name__=="__main__":
    init  = Main();
    init.main()