from Models.Model import Model

class ListaModel(Model):
            
    def cadastrar_lista(self, descricao, usuario_id):
        
        # Insere lista
        super().executar_query("INSERT INTO LISTA VALUES (?,?);", (descricao, usuario_id))
        
    def editar_lista_por_id(self, descricao, lista_id):
        
        # Atualiza lista
        super().executar_query("UPDATE LISTA set descricao=? WHERE rowid=?;", (descricao, lista_id))

    def excluir_lista_por_id(self, lista_id):
        
        # Deleta lista
        super().executar_query("DELETE FROM LISTA WHERE rowid=?;", (lista_id,))
            
    def buscar_listas_do_usuario(self, usuario_id):
        
        # Busca as listas
        return super().executar_query("SELECT rowid, * FROM LISTA WHERE usuario_id=?;", (usuario_id,))
    
    def buscar_lista(self, descricao, usuario_id):
        
        # Busca lista
        return super().executar_query("SELECT rowid, * FROM LISTA WHERE descricao=? AND usuario_id=?;", (descricao, usuario_id))
        
    