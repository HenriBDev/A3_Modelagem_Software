from Controllers.Controller import Controller

class TarefaController(Controller):
    
    def cadastrar_tarefa(self, nome, duracao, lista_id) -> None:
        
        busca_tarefa = self.model.buscar_tarefas(filtros={"descricao": nome, "lista_id": lista_id})
        if len(busca_tarefa) > 0:
            return "Já existe uma tarefa nessa lista com o mesmo nome."
        
        self.model.cadastrar_tarefa(nome, duracao, lista_id)
        return "ok"
            
    def excluir_tarefa(self, tarefa_id, lista_id) -> None:
        
        busca_tarefa_id = self.model.buscar_tarefas(filtros={"id": tarefa_id, "lista_id": lista_id})
        if len(busca_tarefa_id) == 0:
            return "Você não possui nenhuma tarefa com esse id nessa lista"
        
        self.model.excluir_tarefa_por_id(tarefa_id)
        return "ok"
            
    def editar_tarefa(self, tarefa_id, nome, duracao, lista_id) -> None:
        
        busca_tarefa_id = self.model.buscar_tarefas(filtros={"id": tarefa_id, "lista_id": lista_id})
        if len(busca_tarefa_id) == 0:
            return "Você não possui nenhuma tarefa com esse id nessa lista"
        
        busca_tarefa_nome = self.model.buscar_tarefas(filtros={"lista_id": lista_id, "descricao": nome})
        if len(busca_tarefa_nome) > 0:
            return "Você já possui uma tarefa nessa lista com esse nome"
        
        self.model.editar_tarefa(filtros={"id": tarefa_id}, colunas={"descricao": nome, "tempo": duracao})
        return "ok"
        
    def buscar_tarefas_por_lista(self, lista_id) -> tuple:
        
        busca_tarefas = self.model.buscar_tarefas(filtros={"lista_id": lista_id})
        if len(busca_tarefas) == 0:
            return ("Você não possui tarefas nessa lista", False)
            
        return ("ok", self.model.buscar_tarefas(filtros={"lista_id": lista_id}))