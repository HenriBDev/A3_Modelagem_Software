from Controllers.Controller import Controller

class UsuarioController(Controller):
    
    def usuario_existe(self, email, senha) -> bool:
        return bool(self.buscar_usuario(email, senha))
    
    def email_ja_cadastrado(self, email) -> bool:
        return bool(self.model.buscar_usuario_por_email(email))
    
    def cadastrar_usuario(self, email: str, senha: str, nome: str):
        self.model.cadastrar_usuario(nome, email, senha)
    
    def buscar_usuario(self, email, senha):
        return self.model.buscar_usuario_por_credenciais(email, senha)
