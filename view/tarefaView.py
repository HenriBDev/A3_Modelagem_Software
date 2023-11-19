import os, sys
CURRENT_DIR = os.path.dirname(os.path.abspath("domain/tarefa.py"))
sys.path.append(os.path.dirname(CURRENT_DIR))
TAREFA_CT_DIR = os.path.dirname(os.path.abspath("controller/tarefaController.py"))
sys.path.append(os.path.dirname(TAREFA_CT_DIR))
LISTA_VIEW_DIR = os.path.dirname(os.path.abspath("view/listaView.py"))
sys.path.append(os.path.dirname(LISTA_VIEW_DIR))
MENU_DIR = os.path.dirname(os.path.abspath("menu.py"))
sys.path.append(os.path.dirname(MENU_DIR))
from domain.tarefa import Tarefa
from controller.tarefaController import tarefaController
from view.listaView import ListaView
class TarefaView:

        def excluir_tarefa(self,usuario):
                from menu import Menu
                menu = Menu() 
                lista_view = ListaView()
                tarefa_controller = tarefaController()                
                lista_id=lista_view.manipular_listas(usuario)
                self.exibir_tarefa(lista_id) 
                tarefa_id = input("Qual tarefa deseja excluir ? (Digite o id dela)\n")
                tarefa_controller.deletar_tarefa(tarefa_id)
                print("Tarefa excluida com sucesso")                
                menu.navegar_menu(usuario)
            
        def exibir_tarefa(self,lista_id):
               tarefa_controller = tarefaController()
               tarefas = tarefa_controller.exibir_tarefa(lista_id)
               print("Tarefas:\n")
               for tarefa in tarefas:
                      print(f"{tarefa[0]} - {tarefa[1]}")

        def editar_tarefa(self,usuario):
                from menu import Menu
                menu = Menu()
                lista_view = ListaView()
                tarefa_controller = tarefaController()                
                lista_id=lista_view.manipular_listas(usuario)
                self.exibir_tarefa(lista_id)
                tarefa_id = int(input("Qual tarefa deseja alterar ? (Digite o id dela)\n"))
                nova_descricao=input("Digite o descrição da tarefa:\n")
                novo_tempo=int(input("Digite o tempo da tarefa:\n"))
                tarefa_editada = Tarefa(nova_descricao,lista_id)
                tarefa_editada.tempo = novo_tempo
                tarefa_editada.id = tarefa_id
                tarefa_controller.editar_editar(tarefa_editada,lista_id)
                print("Tarefa editada com sucesso")                
                menu.navegar_menu(usuario)
                                

        def cadastrar_tarefa(self,usuario):
                from menu import Menu
                menu = Menu()
                lista_view = ListaView()
                tarefa_controller = tarefaController()
                lista_id=lista_view.manipular_listas(usuario)                
                descricao = input("Digite o nome da tarefa\n")
                tarefa = Tarefa(descricao,lista_id)
                tarefa.tempo = input("Digite um tempo da tarefa\n")
                tarefa_controller.cadastrar_tarefa(tarefa,tarefa.lista_id)
                print("Tarefa cadastrada com sucesso")
                menu.navegar_menu(usuario)
                
                
        def concluir_tarefa(self,usuario):
                from menu import Menu
                menu = Menu() 
                lista_view = ListaView()
                tarefa_controller = tarefaController()                
                lista_id=lista_view.manipular_listas(usuario)
                self.exibir_tarefa(lista_id) 
                tarefa_id = input("Qual tarefa deseja concluir ? (Digite o id dela)\n")  
                tarefa_controller.concluir_tarefa(tarefa_id)                   
                print("Tarefa concluida com sucesso")
                menu.navegar_menu(usuario)
               