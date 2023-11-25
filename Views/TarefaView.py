from Domains.Tarefa import Tarefa
from Views.View import View

class TarefaView(View):
        
        def excluir_tarefa(self, lista_id):                
                id_tarefas = self.exibir_tarefas_da_lista(lista_id) 
                id_input = int(input("Qual tarefa deseja excluir ? (Digite o id dela)\n"))
                if id_input in id_tarefas:
                        self.controller.deletar_tarefa(id_input)
                        print("Tarefa excluida com sucesso")
                else:
                        print("Não há nenhuma tarefa com esse ID")
            
        def trocar_tarefa_de_lista(self):
                tarefa = input("Qual tarefa deseja alterar de lista ? (Digite o id dela)")
                print(f"tarefas:") # fazer interação da lista de tarefa para printar cada uma
                print(f"Tarefa '{tarefa}' alterada de lista")

        def editar_tarefa(self, lista_id):
                while True:
                        tarefas = self.exibir_tarefas_da_lista(lista_id)
                        tarefa_id = int(input("Qual tarefa deseja alterar ? (Digite o id dela)\n"))
                        if tarefa_id in tarefas:
                                nova_descricao=input("Digite o descrição da tarefa:\n")
                                novo_tempo=int(input("Digite a duração da tarefa em segundos:\n"))
                                self.controller.editar_tarefa(tarefa_id, nova_descricao, novo_tempo)
                                print("Tarefa editada com sucesso")
                                break
                        else:
                                print("Não há nenhuma tarefa com esse ID")

        def exibir_tarefas_da_lista(self, lista_id):
                tarefas = self.controller.exibir_tarefas(lista_id)
                print("Tarefas:\n")
                for tarefa in tarefas:
                        print(f"{tarefa[0]} - {tarefa[1]}")
                return [tarefa[0] for tarefa in tarefas]
                      
        def cadastrar_tarefa(self, lista_id):
                descricao = input("Digite o nome da tarefa\n")
                duracao = int(input("Digite a duração da tarefa em segundos\n"))
                self.controller.cadastrar_tarefa(descricao, duracao, lista_id)
                print("Tarefa cadastrada com sucesso")

        def concluir_tarefa(self, tarefa_id):
                # self.exibir_tarefas_da_lista(lista_id) 
                # tarefa_id = int(input("Qual tarefa deseja concluir ? (Digite o id dela)\n"))  
                self.controller.concluir_tarefa(tarefa_id)                   
                print("Tarefa concluida com sucesso")

        def timer(self,lista_id):
                self.exibir_tarefas_da_lista(lista_id)
                tarefa_id = int(input("Qual tarefa deseja concluir ? (Digite o id dela)\n"))
                self.controller.timer(tarefa_id)
                self.concluir_tarefa(tarefa_id)
               