import time
import os

from Views.View import View
from Domains.Tarefa import Tarefa

class ListaView(View):
        def exibir_listas(self, usuario_id):
                listas = self.controller.buscar_listas(usuario_id)
                print("Lista de tarefas:")
                for lista in listas:
                        print(f"{lista[0]} - {lista[1]}")
                return [lista[0] for lista in listas]

        def cadastrar_lista(self, usuario_id):
                descricao = input("Digite o nome da lista: ") 
                lista_cadastrada = self.controller.cadastrar_lista(descricao, usuario_id)
                if lista_cadastrada: print("Lista cadastrada com sucesso")

        def excluir_lista(self, usuario_id):
                id_listas = self.exibir_listas(usuario_id)
                id_input = int(input("\nQual lista deseja excluir?\nDigite o número: "))                   
                if(id_input in id_listas):
                        self.controller.excluir_lista(id_input)
                        print('Lista deletada com sucesso')
                else:
                        print("Não há nenhuma lista com esse ID")
                        
        def selecionar_lista(self, usuario_id):
                while True:
                        listas = self.exibir_listas(usuario_id)               
                        lista_id = int(input("Qual lista deseja selecionar?\n"))
                        if lista_id in listas:
                                return lista_id
                        else:
                                print("Não há nenhuma lista com esse ID")
                                
        def iniciar_execucao_lista(self, usuario_id):
                lista_selecionada_id = self.selecionar_lista(usuario_id)
                tarefas_usuario = [Tarefa(*tarefa) for tarefa in self.controller.buscar_tarefas_por_lista(lista_selecionada_id)]
                os.system('cls')
                for tarefa in tarefas_usuario:
                        for x in range(tarefa.tempo, 0, -1):
                                segundos = x % 60
                                minutos = int(x / 60) % 60 
                                horas = int(x / 3600)
                                print(tarefa.descricao)
                                print(f'{horas:02}:{minutos:02}:{segundos:02}')
                                time.sleep(1)
                                os.system('cls')
                        print("Tarefa concluída!")
