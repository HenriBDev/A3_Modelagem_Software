from Controllers.Controller import Controller

class UsuarioController(Controller):
    
    def buscar_usuario_por_id(self, id_usuario) -> tuple:
        busca_usuario = self.model.buscar_usuarios(filtros={"id": id_usuario})
        
        if len(busca_usuario) == 0:
            return ("Não há nenhum usuário com esse ID.", False)
        
        return ("ok", busca_usuario[0])
    
    def cadastrar_usuario(self, email: str, senha: str, nome: str) -> None:
        busca_usuario = self.model.buscar_usuarios(filtros={"email": email})
        
        if len(busca_usuario) > 0:
            return "\nEmail já cadastrado. Digite um email diferente."
        
        self.model.cadastrar_usuario(nome, email, senha)
        return "ok"
    
    def logar_usuario(self, email: str, senha: str) -> tuple:
        busca_usuario = self.model.buscar_usuarios(filtros={"email": email, "senha": senha})
        if len(busca_usuario) == 0:
            return ("\nEmail e/ou senha incorretos", False)
        
        return ("ok", busca_usuario[0].id)
