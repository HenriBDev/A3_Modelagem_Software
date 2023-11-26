import os
from Views.View import View
from Controllers.ControllerFactory import ControllerFactory

class TarefaView(View):
        
        @View.view_action
        def excluir_tarefa(self, usuario_id):
                
                lista_controller = ControllerFactory().criar_instancia('lista')
                
                print('Suas listas:')
                msg_retorno, retorno = lista_controller.buscar_listas_do_usuario(usuario_id)
                
                if msg_retorno != "ok":
                        print(msg_retorno)
                        return False
                
                for lista in retorno:
                        print(f"Lista {lista.id} - {lista.descricao}\n")
                        
                lista_id = int(input("De qual lista deseja remover uma tarefa?\n"))
                msg_retorno, retorno = lista_controller.buscar_lista_do_usuario_por_id(lista_id, usuario_id)
                
                if msg_retorno != "ok":
                        print(msg_retorno)
                        return False
                
                msg_retorno, tarefas = self.controller.buscar_tarefas_por_lista(lista_id)
                
                if msg_retorno != "ok":
                        print(msg_retorno)
                        return
                
                os.system('cls' if os.name=='nt' else 'clear')
                
                print("Tarefas:\n")
                for tarefa in tarefas:
                        duracao_tarefa = tarefa.tempo
                        horas, resto = divmod(duracao_tarefa, 3600)
                        minutos, segundos = divmod(resto, 60)
                        print(f"{tarefa.id} - {tarefa.descricao} ({horas:02}:{minutos:02}:{segundos:02})")
                        
                id_input = int(input("Qual tarefa deseja excluir? (Digite o id dela)\n"))
                msg_retorno = self.controller.excluir_tarefa(id_input, lista_id)
                print("Tarefa excluida com sucesso" if msg_retorno == "ok" else msg_retorno)

        @View.view_action
        def editar_tarefa(self, usuario_id):
                
                lista_controller = ControllerFactory().criar_instancia('lista')
                
                print('Suas listas:')
                msg_retorno, retorno = lista_controller.buscar_listas_do_usuario(usuario_id)
                
                if msg_retorno != "ok":
                        print(msg_retorno)
                        return False
                
                for lista in retorno:
                        print(f"Lista {lista.id} - {lista.descricao}\n")
                        
                lista_id = int(input("Qual lista está a tarefa que deseja alterar?\n"))
                msg_retorno, retorno = lista_controller.buscar_lista_do_usuario_por_id(lista_id, usuario_id)
                
                if msg_retorno != "ok":
                        print(msg_retorno)
                        return False
                
                msg_retorno, tarefas = self.controller.buscar_tarefas_por_lista(lista_id)
                
                if msg_retorno != "ok":
                        print(msg_retorno)
                        return
                
                os.system('cls' if os.name=='nt' else 'clear')
                
                print("Tarefas:\n")
                for tarefa in tarefas:
                        duracao_tarefa = tarefa.tempo
                        horas, resto = divmod(duracao_tarefa, 3600)
                        minutos, segundos = divmod(resto, 60)
                        print(f"{tarefa.id} - {tarefa.descricao} ({horas:02}:{minutos:02}:{segundos:02})")
        
                tarefa_id = int(input("Qual tarefa deseja alterar? (Digite o id dela)\n"))
                novo_nome = input("Digite o nome da tarefa: ")
                nova_duracao = int(input("Digite a duração da tarefa em segundos: "))
                
                msg_retorno = self.controller.editar_tarefa(tarefa_id, novo_nome, nova_duracao, lista_id)
                print("Tarefa editada com sucesso" if msg_retorno == "ok" else msg_retorno)
        
        @View.view_action              
        def cadastrar_tarefa(self, usuario_id):
                
                lista_controller = ControllerFactory().criar_instancia('lista')
                
                print('Suas listas:')
                msg_retorno, retorno = lista_controller.buscar_listas_do_usuario(usuario_id)
                
                if msg_retorno != "ok":
                        print(msg_retorno)
                        return False
                
                for lista in retorno:
                        print(f"Lista {lista.id} - {lista.descricao}\n")
                        
                lista_id = int(input("Qual lista deseja adicionar a tarefa?\n"))
                msg_retorno, retorno = lista_controller.buscar_lista_do_usuario_por_id(lista_id, usuario_id)
                
                if msg_retorno != "ok":
                        print(msg_retorno)
                        return False
                
                nome = input("Digite o nome da tarefa: ")
                duracao = int(input("Digite a duração da tarefa em segundos: "))
                msg_retorno = self.controller.cadastrar_tarefa(nome, duracao, lista_id)
                print("Tarefa cadastrada com sucesso" if msg_retorno == "ok" else msg_retorno)
               