from Models.Model import Model

class ListaModel(Model):
            
    def cadastrar_lista(self, descricao, usuario_id):
        
        # Insere lista
        super().executar_query("INSERT INTO LISTA VALUES (?,?);", (descricao, usuario_id))
        
    def editar_lista(self, colunas: dict, filtros: dict|None):
        
        query = "UPDATE Lista SET "
        
        query_args = []
        for nome_coluna in colunas.keys():
            query += f"{nome_coluna}=(?), "
            query_args.append(colunas[nome_coluna])
        query = query[:-2]
        
        query += " WHERE"
        for nome_filtro in filtros.keys():
            if nome_filtro != 'id':
                query += f" {nome_filtro}=(?) AND"
            else:
                query += " rowid=(?) AND"
            query_args.append(filtros[nome_filtro])
        query = query[:-4]

        # Atualiza tarefa
        super().executar_query(query, tuple(query_args))

    def excluir_lista_por_id(self, lista_id):
        
        # Deleta lista
        super().executar_query("DELETE FROM LISTA WHERE rowid=?;", (lista_id,))
    
    def buscar_listas(self, colunas: list|tuple = ("id", "descricao", "usuario_id"), filtros: dict|None = None):
        
        query = "SELECT "
        for nome_coluna in colunas:
            if nome_coluna != 'id':
                query += f"{nome_coluna}, "
            else:
                query += "rowid, "
        query = query[:-2]
        query += " FROM Lista"
        
        filtro_args = []
        if filtros != None:
            query += " WHERE"
            for nome_filtro in filtros.keys():
                if nome_coluna != 'id':
                    query += f" {nome_filtro}=(?) AND"
                else:
                    query += " rowid=(?) AND"
                filtro_args.append(filtros[nome_filtro])
            query = query[:-4]
            
        result_query = super().executar_query(query, tuple(filtro_args))
        
        result_domains = []
        for linha in result_query:
            result_domains.append(self.Domain({
                nome_coluna: linha[index_coluna]
            for index_coluna, nome_coluna in enumerate(colunas)}))
        return tuple(result_domains)
        
    