import os, sys
TAREFA_DIR = os.path.dirname(os.path.abspath("view/tarefaView.py"))
sys.path.append(os.path.dirname(TAREFA_DIR))
LISTA_DIR = os.path.dirname(os.path.abspath("view/listaView.py"))
sys.path.append(os.path.dirname(LISTA_DIR))
LOGIN_DIR = os.path.dirname(os.path.abspath("view/loginView.py"))
sys.path.append(os.path.dirname(LOGIN_DIR))
from view.tarefaView import TarefaView
from view.listaView import ListaView
from view.loginView import LoginView
class Menu:  
    def exibir_menu_inicial(self):            
        while True:        
            print("------------Menu Inicial------------\n1 - Fazer Login\n2 - Cadastrar usuário")

            valor_digitado = input("O que deseja fazer ?\n")
            if(valor_digitado == '1'):
                LoginView.login(self)
                break
            elif(valor_digitado == '2'):
                LoginView.cadastrar_usuario(self)
                break
            else:
                print('Valor digitado errado')

        

    def exibir_menu_principal(self):
        print("------------LISTA DE TAREFAS------------\no que voce deseja fazer ?\n1 - Criar Lista ?\n2 - Excluir Lista ?\n3 - Criar tarefas ?\n4 - Editar tarefa ?\n5 - Concluir tarefa ?\n6 - Excluir tarefa ?\n7 - Sair")
    def navegar_menu(self,usuario: object):
        self.exibir_menu_principal()
        valorDigitado = input()
        if(valorDigitado == '1'):
           ListaView.cadastrar_listas(self,usuario)
        elif(valorDigitado == '2'):
            listaView =ListaView()
            listaView.excluir_lista(usuario)
        elif(valorDigitado == '3'):
            tarefaView=TarefaView()
            tarefaView.cadastrar_tarefa(usuario)
        elif(valorDigitado == '4'):
            tarefaView=TarefaView()
            tarefaView.editar_tarefa(usuario)
        elif(valorDigitado == '5'):
            tarefaView=TarefaView()
            tarefaView.concluir_tarefa(usuario)
        elif(valorDigitado =='6'):
            tarefaView=TarefaView()
            tarefaView.excluir_tarefa(usuario)
        elif(valorDigitado == '7'):
            LoginView.sair(self)
           

if __name__ == '__main__':
    menu = Menu()
    menu.navegar_menu()