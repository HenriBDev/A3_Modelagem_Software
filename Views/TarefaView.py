from Domains.Tarefa import Tarefa
from Models.TarefaModel import TarefaModel

class TarefaView:
        
        def excluir_tarefa(self):
            tarefa = input("Qual tarefa deseja excluir? (Digite o id dela)\n")
            
        def trocar_tarefa_de_lista(self):
                tarefa = input("Qual tarefa deseja alterar de lista ? (Digite o id dela)")
                print(f"tarefas:") # fazer interação da lista de tarefa para printar cada uma
                print(f"Tarefa '{tarefa}' alterada de lista")

        def editar_tarefa(self):
                print(f"{lista}")
                tarefa_id = input("Qual tarefa deseja alterar ? (Digite o id dela)")
                input("Digite o descricao da tarefa")
                input("Digite o tempo da tarefa")                
                concluir = input("Deseja concluir tarefa ? (S/N)")

        def cadastrar_tarefa(self):
                descricao = input("Digite o nome da tarefa\n")
                tarefa = Tarefa(descricao)
                tarefa.tempo = input("Digite um tempo da tarefa\n")
                TarefaModel.cadastrar_tarefa(tarefa)
                
        def concluir_tarefa(self):
               tarefa_id = input("Qual tarefa deseja concluir ? (Digite o id dela)")
               concluir = input("Deseja concluir tarefa ? (S/N)")
               