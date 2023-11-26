import time
import os
from Views.View import View
from Controllers.ControllerFactory import ControllerFactory

class ListaView(View):
        
        @View.view_action
        def selecionar_lista(self, usuario_id):
                os.system('cls' if os.name=='nt' else 'clear')
                print('Suas listas:')
                msg_retorno, retorno = self.controller.buscar_listas_do_usuario(usuario_id)
                
                if msg_retorno != "ok":
                        print(msg_retorno)
                        return False
                
                for lista in retorno:
                        print(f"Lista {lista.id} - {lista.descricao}\n")
                        
                id_input = int(input("Qual lista deseja selecionar?\n"))
                msg_retorno, retorno = self.controller.buscar_lista_do_usuario_por_id(id_input, usuario_id)
                
                if msg_retorno != "ok":
                        print(msg_retorno)
                        return False
                
                print(f"Lista {id_input} selecionada.")
                return retorno.id
                
        @View.view_action
        def exibir_listas(self, usuario_id):
                print('Suas listas:')
                msg_retorno, retorno = self.controller.buscar_listas_do_usuario(usuario_id, incluir_tarefas=True)

                if msg_retorno != "ok":
                        print(msg_retorno)
                        return
                
                for lista_com_tarefas in retorno:
                        print(f"Lista {lista_com_tarefas['lista'].id} - {lista_com_tarefas['lista'].descricao}")
                        if len(lista_com_tarefas['tarefas']) > 0:
                                for index, tarefa in enumerate(lista_com_tarefas['tarefas']):
                                        horas, resto = divmod(tarefa.tempo, 3600)
                                        minutos, segundos = divmod(resto, 60)
                                        if index < len(lista_com_tarefas['tarefas']) - 1:
                                                print(f"  ├Tarefa {tarefa.id} - {tarefa.descricao} ({horas:02}:{minutos:02}:{segundos:02})")
                                        else:
                                                print(f"  └Tarefa {tarefa.id} - {tarefa.descricao} ({horas:02}:{minutos:02}:{segundos:02})")
                        else:
                                print("  └Sem tarefas\n")
                        print("")

        @View.view_action
        def cadastrar_lista(self, usuario_id):
                nome = input("Digite o nome da lista: ")
                msg_retorno = self.controller.cadastrar_lista(nome, usuario_id)
                if msg_retorno == "ok": print("Lista cadastrada com sucesso")

        @View.view_action
        def excluir_lista(self, usuario_id):
                print('Suas listas:')
                msg_retorno, retorno = self.controller.buscar_listas_do_usuario(usuario_id)
                
                if msg_retorno != "ok":
                        print(msg_retorno)
                        return False
                
                for lista in retorno:
                        print(f"Lista {lista.id} - {lista.descricao}\n")
                        
                id_input = int(input("\nQual lista deseja excluir?\nDigite o número: "))
                msg_retorno = self.controller.excluir_lista_do_usuario(id_input, usuario_id)
                print('Lista deletada com sucesso' if msg_retorno == "ok" else msg_retorno)
                       
                         
        @View.view_action
        def iniciar_execucao_lista(self, lista_id):
                tarefa_controller = ControllerFactory().criar_instancia('tarefa')
                
                msg_retorno, tarefas = tarefa_controller.buscar_tarefas_por_lista(lista_id)
                if msg_retorno != "ok":
                        print(msg_retorno)
                        return
                
                os.system('cls' if os.name=='nt' else 'clear')
                for tarefa in tarefas:
                        for tempo_restante in range(tarefa.tempo, 0, -1):
                                segundos = tempo_restante % 60
                                minutos = int(tempo_restante / 60) % 60 
                                horas = int(tempo_restante / 3600)
                                print(f"Executando {tarefa.descricao}...")
                                print(f'{horas:02}:{minutos:02}:{segundos:02}')
                                time.sleep(1)
                                os.system('cls' if os.name=='nt' else 'clear')
                        print(f"Tarefa {tarefa.descricao} concluída!")
                print("Lista concluída!")
