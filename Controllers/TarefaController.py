from Controllers.Controller import Controller
import time

class TarefaController(Controller):
    
    def verificar_tarefa_existe(self, nome, lista_id) -> bool:
        return bool(self.model.buscar_tarefas(filtros={"descricao": nome, "lista_id": lista_id}))
    
    def cadastrar_tarefa(self, descricao, duracao, lista_id) -> None:
        self.model.cadastrar_tarefa(descricao, duracao, lista_id)
            
    def deletar_tarefa(self, tarefa_id) -> None:
        self.model.excluir_tarefa_por_id(tarefa_id)
            
    def editar_tarefa(self, tarefa_id, nome, duracao) -> None:
        self.model.editar_tarefa(filtros={"id": tarefa_id}, colunas={"descricao": nome, "tempo": duracao})
        
    def buscar_tarefas_por_lista(self, lista_id) -> tuple:
        return self.model.buscar_tarefas(filtros={"lista_id": lista_id})