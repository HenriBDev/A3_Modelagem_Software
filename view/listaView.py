import os, sys
LISTA_DIR = os.path.dirname(os.path.abspath("domain/listaTarefa.py"))
sys.path.append(os.path.dirname(LISTA_DIR))
LISTA_CT_DIR = os.path.dirname(os.path.abspath("controller/listaController.py"))
sys.path.append(os.path.dirname(LISTA_CT_DIR))
MENU_DIR = os.path.dirname(os.path.abspath("menu.py"))
sys.path.append(os.path.dirname(MENU_DIR))
from domain.listaTarefa import ListaTarefa
from controller.listaController import listaController

class ListaView:
        def exibir_listas(self,usuario):
                lista_controller = listaController()
                listas = lista_controller.exibir_lista(usuario)
                for lista in listas:
                        print(f"Listas de Tarefas:\n{lista[0]} - {lista[1]}")
                return len(listas)

        def cadastrar_listas(self,usuario):
                from menu import Menu
                menu =Menu()
                lista = ListaTarefa(usuario.id)
                lista_controller = listaController()
                descricao = input("digite o nome da lista") 
                lista.descricao = descricao
                lista_controller.cadastrar_lista(lista,usuario)
                print("Lista cadastrada com sucesso")
                menu.navegar_menu(usuario)

        def excluir_lista(self,usuario):
                from menu import Menu
                menu =Menu()
                lista_controller = listaController()
                self.exibir_listas(usuario)
                lista_id = int(input("\nQual lista deseja excluir ?"))                   
                if(lista_controller.deletar_lista(lista_id)):
                        print('Lista deletado com sucesso')
                        menu.navegar_menu(usuario)
