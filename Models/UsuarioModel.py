from Models.Model import Model

class UsuarioModel(Model):

    def cadastrar_usuario(self, nome, email, senha) -> None:
        
        # Insere usuário
        super().executar_query("INSERT INTO Usuario VALUES (?,?,?)", (nome, email, senha))

    def buscar_usuarios(self, colunas: list|tuple = ("id", "nome", "email", "senha"), filtros: dict|None = None) -> tuple:
        
        query = "SELECT "
        for nome_coluna in colunas:
            if nome_coluna != 'id':
                query += f"{nome_coluna}, "
            else:
                query += "rowid, "
        query = query[:-2]
        query += " FROM Usuario"
        
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
