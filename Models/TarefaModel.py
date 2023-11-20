from Models.ModelBase import ModelBase

class TarefaModel(ModelBase):

    def cadastrar_tarefa(self, descricao, tempo, lista_id):
        
        # Insere tarefa
        super().executar_query("INSERT INTO TAREFA VALUES(?,0,?,?);", (descricao, tempo, lista_id))

    def buscar_tarefa_por_id(self, tarefa_id):
        
        # Busca a tarefa
        return super().executar_query("SELECT rowid, * FROM TAREFA WHERE rowid=?", (tarefa_id,))
    
    def editar_tarefa_por_id(self, tarefa_id, descricao, duracao):
        
        # Atualiza tarefa
        super().executar_query("UPDATE TAREFA set descricao=?, tempo=? WHERE rowid=?;", (descricao, duracao, tarefa_id))

    def concluir_tarefa_por_id(self, tarefa_id):
        
        # Atualiza tarefa
        super().executar_query("UPDATE TAREFA set concluida=1 WHERE rowid=?;", (tarefa_id,))

    def excluir_tarefa_por_id(self, tarefa_id):
        
        # Deleta tarefa
        super().executar_query("DELETE FROM TAREFA WHERE rowid=?;", (tarefa_id,))  
    
    def buscar_tarefas_por_lista(self, lista_id):
        
        # Busca as tarefas
        return super().executar_query("SELECT rowid, * FROM TAREFA WHERE lista_id=?", (lista_id,))
    
    def buscar_tarefas_por_descricao(self, descricao, lista_id):
        
        # Busca as tarefas
        return super().executar_query("SELECT rowid, * FROM TAREFA WHERE descricao=? AND lista_id=?", (descricao, lista_id))

