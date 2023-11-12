import os, sys
CURRENT_DIR = os.path.dirname(os.path.abspath("domain/tarefa.py"))
sys.path.append(os.path.dirname(CURRENT_DIR))
TAREFA_BD_DIR = os.path.dirname(os.path.abspath("model/tarefaView.py"))
sys.path.append(os.path.dirname(TAREFA_BD_DIR))
from domain.tarefa import Tarefa
from model.tarefaModel import TarefaModel
class TarefaView:
        def excluir_tarefa(self):
            tarefa = input("Qual tarefa deseja excluir ? (Digite o id dela)")
            

        def trocar_tarefa_de_lista(self):
                tarefa = input("Qual tarefa deseja alterar de lista ? (Digite o id dela)")
                print(f"tarefas:") # fazer interação da lista de tarefa para printar cada uma
                print(f"Tarefa '{tarefa}' alterada de lista")

        def editar_tarefa(self):
                tarefa = input("Qual tarefa deseja alterar ? (Digite o id dela)")
                concluir = input("Deseja concluir tarefa ? (S/N)")

        def cadastrar_tarefa():
                descricao = input("Digite o nome da tarefa\n")
                tarefa = Tarefa(descricao)
                tarefa.tempo = input("Digite um tempo da tarefa\n")
                TarefaModel.cadastrar_tarefa(tarefa)
                
                
        def concluir_tarefa(self):
               concluir = input("Deseja concluir tarefa ? (S/N)")
               