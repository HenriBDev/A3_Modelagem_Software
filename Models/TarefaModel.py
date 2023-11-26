from Models.Model import Model

class TarefaModel(Model):

    def cadastrar_tarefa(self, descricao, tempo, lista_id):
        
        # Insere tarefa
        super().executar_query("INSERT INTO TAREFA VALUES(?,?,?);", (descricao, tempo, lista_id))

    def buscar_tarefas(self, colunas: list|tuple = ("id", "descricao", "tempo", "lista_id"), filtros: dict|None = None):
        
        query = "SELECT "
        for nome_coluna in colunas:
            if nome_coluna != 'id':
                query += f"{nome_coluna}, "
            else:
                query += "rowid, "
        query = query[:-2]
        query += " FROM Tarefa"
        
        filtro_args = []
        if filtros != None:
            query += " WHERE"
            for nome_filtro in filtros.keys():
                if nome_filtro != 'id':
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
    
    def editar_tarefa(self, colunas: dict, filtros: dict|None):
        
        query = "UPDATE Tarefa SET "
        
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

    def excluir_tarefa_por_id(self, tarefa_id):
        
        # Deleta tarefa
        super().executar_query("DELETE FROM TAREFA WHERE rowid=?;", (tarefa_id,))

