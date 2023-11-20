from Models.UsuarioModel import UsuarioModel

class UsuarioController:
    
    def validar_dados(self, email, senha) -> bool:
        return bool(self.buscar_usuario(email, senha))
    
    def verificar_usuario_existe(self, email) -> bool:
        return bool(UsuarioModel().buscar_usuario_por_email(email))
    
    def cadastrar_usuario(self, email: str, senha: str, nome: str):
        UsuarioModel().cadastrar_usuario(nome, email, senha)
    
    def buscar_usuario(self, email, senha):
        return UsuarioModel().buscar_usuario_por_credenciais(email, senha)
