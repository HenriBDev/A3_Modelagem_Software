import os, sys
TAREFA_DIR = os.path.dirname(os.path.abspath("view/tarefaView.py"))
sys.path.append(os.path.dirname(TAREFA_DIR))
LISTA_DIR = os.path.dirname(os.path.abspath("view/listaView.py"))
sys.path.append(os.path.dirname(LISTA_DIR))
from view.tarefaView import TarefaView
from view.listaView import ListaView
class Menu:        
    def exibir_menu(self):
        print("------------LISTA DE TAREFAS------------\no que voce deseja fazer ?\n1 - Adicionar tarefas ?\n2 - concluir tarefas ?\n3 - Remover tarefas ?\n4 - Checar a lista ?\n5 - sair ?\n")
    def navegar_menu(self):
        self.exibir_menu()
        valorDigitado = input()
        if(valorDigitado == '1'):
           TarefaView.cadastrar_tarefa()
        elif(valorDigitado == '2'):
            TarefaView.concluir_tarefa()
        elif(valorDigitado == '3'):
            TarefaView.excluir_tarefa()
        elif(valorDigitado == '4'):
            ListaView.exibir_listas()
           

if __name__ == '__main__':
    menu = Menu()
    menu.navegar_menu()