from Controllers.Controller import Controller
import time

class TarefaController(Controller):
    
    def verificar_tarefa_existe(self, descricao, lista_id) -> bool:
        return bool(self.model.buscar_tarefas_por_descricao(descricao, lista_id))
    
    def cadastrar_tarefa(self, descricao, duracao, lista_id):
        self.model.cadastrar_tarefa(descricao, duracao, lista_id)
            
    def deletar_tarefa(self, tarefa_id):
        self.model.excluir_tarefa_por_id(tarefa_id)
            
    def editar_tarefa(self, tarefa_id, descricao, duracao):
        self.model.editar_tarefa_por_id(tarefa_id, descricao, duracao)

    def concluir_tarefa(self, tarefa_id):
        self.model.concluir_tarefa_por_id(tarefa_id)
        
    def buscar_tarefas_por_lista(self,lista_id):
        return self.model.buscar_tarefas_por_lista(lista_id)