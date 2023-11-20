from Models.ModelBase import ModelBase

class TarefaModel(ModelBase):

    def cadastrar_tarefa(self, tarefa):
        
        # Insere tarefa
        super().executar_query("INSERT INTO TAREFA VALUES(?,?,?,?,?);", (tarefa.id,tarefa.descricao,tarefa.status,tarefa.tempo,tarefa.lista_id))

    def editar_tarefa_por_id(self, tarefa):
        
        # Atualiza tarefa
        super().executar_query("UPDATE TAREFA set descricao=?, concluida=?, tempo=? WHERE id=?;", (tarefa.descricao, tarefa.status, tarefa.tempo, tarefa.id))

    def concluir_tarefa_por_id(self, tarefa):
        
        # Atualiza tarefa
        super().executar_query("UPDATE * TAREFA set concluida=? WHERE id=?;", (tarefa.status, tarefa.id))

    def excluir_tarefa_por_id(self, tarefa):
        
        # Deleta tarefa
        super().executar_query("DELETE FROM TAREFA WHERE id=?;", (tarefa.id,))  
    
    def buscar_tarefas_por_lista(self, lista_id):
        
        # Busca as tarefas
        return super().executar_query("SELECT * FROM TAREFA WHERE lista_id=?", (lista_id,))
