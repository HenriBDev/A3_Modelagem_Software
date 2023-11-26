from Views.View import View

class TarefaView(View):
        
        def _exibir_tarefas_da_lista(self, lista_id):
                tarefas = self.controller.buscar_tarefas_por_lista(lista_id)
                print("Tarefas:\n")
                for tarefa in tarefas:
                        duracao_tarefa = tarefa[3]
                        horas, resto = divmod(duracao_tarefa, 3600)
                        minutos, segundos = divmod(resto, 60)
                        print(f"{tarefa[0]} - {tarefa[1]} ({horas:02}:{minutos:02}:{segundos:02})")
                return [tarefa[0] for tarefa in tarefas]
        
        @View.view_action
        def excluir_tarefa(self, lista_id):
                id_tarefas = self._exibir_tarefas_da_lista(lista_id)
                id_input = int(input("Qual tarefa deseja excluir? (Digite o id dela)\n"))
                if id_input in id_tarefas:
                        self.controller.deletar_tarefa(id_input)
                        print("Tarefa excluida com sucesso")
                else:
                        print("Não há nenhuma tarefa com esse ID")

        @View.view_action
        def editar_tarefa(self, lista_id):
                tarefas = self._exibir_tarefas_da_lista(lista_id)
                tarefa_id = int(input("Qual tarefa deseja alterar? (Digite o id dela)\n"))
                if tarefa_id in tarefas:
                        novo_nome = input("Digite o nome da tarefa: ")
                        if not self.controller.verificar_tarefa_existe(novo_nome, lista_id):
                                nova_duracao = int(input("Digite a duração da tarefa em segundos: "))
                                self.controller.editar_tarefa(tarefa_id, novo_nome, nova_duracao)
                                print("Tarefa editada com sucesso")
                        else:
                                print("Já existe uma tarefa nessa lista com o mesmo nome.")
                else:
                        print("Não há nenhuma tarefa com esse ID")
        
        @View.view_action              
        def cadastrar_tarefa(self, lista_id):
                nome = input("Digite o nome da tarefa: ")
                if not self.controller.verificar_tarefa_existe(nome, lista_id):
                        duracao = int(input("Digite a duração da tarefa em segundos: "))
                        self.controller.cadastrar_tarefa(nome, duracao, lista_id)
                        print("Tarefa cadastrada com sucesso")
                else:
                        print("Já existe uma tarefa nessa lista com o mesmo nome.")
               