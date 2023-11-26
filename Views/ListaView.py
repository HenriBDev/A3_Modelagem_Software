import time
import os

from Views.View import View
from Controllers.ControllerFactory import ControllerFactory
from Domains.Tarefa import Tarefa

class ListaView(View):
        
        def _exibir_listas(self, usuario_id, incluir_tarefas = False):
                tarefa_controller = ControllerFactory().instanciar_controller('tarefa')
                listas = self.controller.buscar_listas(usuario_id)
                print("Suas listas:")
                if len(listas) > 0:
                        for lista in listas:
                                lista_id = lista[0]
                                tarefas = tarefa_controller.buscar_tarefas_por_lista(lista_id)
                                print(f"Lista {lista[0]} - {lista[1]}")
                                if incluir_tarefas:
                                        if len(tarefas) > 0:
                                                for index, tarefa in enumerate(tarefas):
                                                        duracao_tarefa = tarefa[3]
                                                        horas, resto = divmod(duracao_tarefa, 3600)
                                                        minutos, segundos = divmod(resto, 60)
                                                        if index < len(tarefas) - 1:
                                                                print(f"  ├Tarefa {tarefa[0]} - {tarefa[1]} ({horas:02}:{minutos:02}:{segundos:02})")
                                                        else:
                                                                print(f"  └Tarefa {tarefa[0]} - {tarefa[1]} ({horas:02}:{minutos:02}:{segundos:02})")
                                        else:
                                                print("  └Sem tarefas")
                                print()
                else:
                        print("Você não possui nenhuma lista")
                return listas
                        
        @View.view_action
        def checar_listas(self, usuario_id):
                self._exibir_listas(usuario_id, incluir_tarefas=True)

        @View.view_action
        def cadastrar_lista(self, usuario_id):
                descricao = input("Digite o nome da lista: ")
                if not self.controller.verificar_lista_existente(descricao, usuario_id):
                        self.controller.cadastrar_lista(descricao, usuario_id)
                        print("Lista cadastrada com sucesso\n")
                else: print("A lista não pôde ser cadastrada, pois já existe uma lista com o mesmo nome.\n")

        @View.view_action
        def excluir_lista(self, usuario_id):
                listas = self._exibir_listas(usuario_id)
                if len(listas) > 0:
                        ids_listas = [lista[0] for lista in listas]
                        id_input = int(input("\nQual lista deseja excluir?\nDigite o número: "))          
                        if(id_input in ids_listas):
                                if not self.controller.verificar_se_tem_tarefas(id_input):
                                        self.controller.excluir_lista(id_input)
                                        print('Lista deletada com sucesso')
                                else:
                                        print("Não é possível deletar uma lista com tarefas dentro")
                        else:
                                print("Não há nenhuma lista com esse ID")
                       
        @View.view_action 
        def selecionar_lista(self, usuario_id):
                listas = self._exibir_listas(usuario_id)
                if len(listas) > 0:
                        ids_listas = [lista[0] for lista in listas]
                        lista_id = int(input("Qual lista deseja selecionar?\n"))
                        
                        if lista_id in ids_listas: return lista_id
                        else: print("Não há nenhuma lista com esse ID\n")
                return False
                         
        @View.view_action       
        def iniciar_execucao_lista(self, lista_id):
                tarefas = self.controller.buscar_tarefas_por_lista(lista_id)
                if len(tarefas) > 0:
                        tarefas_mapeadas = [Tarefa(*tarefa) for tarefa in tarefas]
                        os.system('cls' if os.name=='nt' else 'clear')
                        for tarefa in tarefas_mapeadas:
                                for x in range(tarefa.tempo, 0, -1):
                                        segundos = x % 60
                                        minutos = int(x / 60) % 60 
                                        horas = int(x / 3600)
                                        print(tarefa.descricao)
                                        print(f'{horas:02}:{minutos:02}:{segundos:02}')
                                        time.sleep(1)
                                        os.system('cls' if os.name=='nt' else 'clear')
                                print("Tarefa concluída!")
                else:
                        print("Essa lista não possui tarefas")
