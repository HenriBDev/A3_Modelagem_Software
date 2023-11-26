from Views.View import View

class TarefaView(View):
        
        @View.view_action
        def excluir_tarefa(self, lista_id):
                msg_retorno, tarefas = self.controller.buscar_tarefas_por_lista(lista_id)
                
                if msg_retorno != "ok":
                        print(msg_retorno)
                        return
                
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
        def editar_tarefa(self, lista_id):
                msg_retorno, tarefas = self.controller.buscar_tarefas_por_lista(lista_id)
                
                if msg_retorno != "ok":
                        print(msg_retorno)
                        return
                
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
        def cadastrar_tarefa(self, lista_id):
                nome = input("Digite o nome da tarefa: ")
                duracao = int(input("Digite a duração da tarefa em segundos: "))
                msg_retorno = self.controller.cadastrar_tarefa(nome, duracao, lista_id)
                print("Tarefa cadastrada com sucesso" if msg_retorno == "ok" else msg_retorno)
               