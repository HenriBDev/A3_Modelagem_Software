from Views.ViewFactory import ViewFactory
class Main():
    
    def __init__(self) -> None:
        
        self._view_factory = ViewFactory()
        self._menu_view = self._view_factory.criar_instancia('menu')
        self._usuario_view = self._view_factory.criar_instancia('usuario')
        self._lista_view = self._view_factory.criar_instancia('lista')
        self._tarefa_view = self._view_factory.criar_instancia('tarefa')
        self.id_usuario_logado = False
        
        while True:
            
            while str(self.id_usuario_logado) != "False":
                
                match self._menu_view.menu_inicial():
                    
                    case '1': self.id_usuario_logado = self._usuario_view.logar_usuario()
                    
                    case '2': self._usuario_view.cadastrar_usuario()
                    
                    case '3': self._menu_view.encerrar_programa()
                    
                    case _: self._menu_view.valor_digitado_invalido()
                
            while True:
                    
                match self._menu_view.menu_principal(self.id_usuario_logado):
                    
                    case '1': self._lista_view.cadastrar_lista(self.id_usuario_logado.id)
                    
                    case '2': self._lista_view.excluir_lista(self.id_usuario_logado.id)
                    
                    case '3': self._tarefa_view.cadastrar_tarefa(self.id_usuario_logado.id)
                    
                    case '4': self._tarefa_view.editar_tarefa(self.id_usuario_logado.id)
                    
                    case '5': self._tarefa_view.excluir_tarefa(self.id_usuario_logado.id)
                    
                    case '6': self._lista_view.iniciar_execucao_lista(self.id_usuario_logado.id)
                    
                    case '7': self._lista_view.exibir_listas(self.id_usuario_logado.id)
                    
                    case '8': break
                
                    case '9': self._menu_view.encerrar_programa()
                
                    case _: self._menu_view.valor_digitado_invalido()
            
if __name__ == '__main__':
    Main()