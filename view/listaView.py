import os, sys
LISTA_DIR = os.path.dirname(os.path.abspath("domain/listaTarefa.py"))
sys.path.append(os.path.dirname(LISTA_DIR))
from domain.listaTarefa import ListaTarefa
class ListaView:
        def exibir_listas(self):
                print(f"Listas de Tarefas:'{lista}'")
                input("Qual lista deseja exibir")

        def cadastrar_listas(self):
                lista = input("digite o nome da lista")                                
                print("Lista cadastrada com sucesso")

        def editar_listas(self):
                lista_id = input("Qual lista deseja alterar ? (Digite o id dela)")
                input("Digite o nome da lista")

        def excluir_tarefa(self):
                lista = input("Qual lista deseja excluir ? (Digite o id dela)")
                print("Não é possivel exlcuir lista, pois existe tarefas cadastradas")
                print("Lista excluida com sucesso")