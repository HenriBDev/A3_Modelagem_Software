from Models.Model import Model

class UsuarioModel(Model):

    def cadastrar_usuario(self, nome, email, senha):
        
        # Insere usuário
        super().executar_query("INSERT INTO Usuario VALUES (?,?,?)", (nome, email, senha))
    
    def buscar_todos_usuarios(self):
        
        # Busca os usuários
        return super().executar_query("SELECT * FROM Usuario;")

    def buscar_usuario_por_credenciais(self, email, senha):
        
        # Busca o usuário
        return super().executar_query("SELECT rowid, * FROM Usuario WHERE email=(?) AND senha=(?);", (email, senha))
    
    def buscar_usuario_por_email(self, email):
        
        # Busca o usuário
        return super().executar_query("SELECT rowid, * FROM Usuario WHERE email=(?)", (email,))
