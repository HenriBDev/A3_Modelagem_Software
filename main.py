from Views.ViewFactory import ViewFactory

class Main():
    
    def __init__(self) -> None:
        
        self._view_factory = ViewFactory()
        self._menu_view = self._view_factory.criar_instancia('menu')
        self._usuario_view = self._view_factory.criar_instancia('usuario')
        self._lista_view = self._view_factory.criar_instancia('lista')
        self._tarefa_view = self._view_factory.criar_instancia('tarefa')
        self.usuario_logado = None
        
        while True:
            
            while True:
                
                valor_digitado = self._menu_view.menu_inicial()
                
                match valor_digitado:
                    
                    case '1':
                        self.usuario_logado = self._usuario_view.logar_usuario()
                        if bool(self.usuario_logado): break
                    
                    case '2': self._usuario_view.cadastrar_usuario()
                    
                    case '3': self._menu_view.encerrar_programa()
                    
                    case _: self._menu_view.valor_digitado_invalido()
                
            while True:
                
                valor_digitado = self._menu_view.menu_principal(self.usuario_logado)
                    
                match valor_digitado:
                    
                    case '1': self._lista_view.cadastrar_lista(self.usuario_logado.id)
                    
                    case '2': self._lista_view.excluir_lista(self.usuario_logado.id)
                    
                    case '3':
                        id_lista_selecionada = self._lista_view.selecionar_lista(self.usuario_logado.id)
                        if(id_lista_selecionada): self._tarefa_view.cadastrar_tarefa(id_lista_selecionada)
                    
                    case '4':
                        id_lista_selecionada = self._lista_view.selecionar_lista(self.usuario_logado.id)
                        if(id_lista_selecionada): self._tarefa_view.editar_tarefa(id_lista_selecionada)
                    
                    case '5': 
                        id_lista_selecionada = self._lista_view.selecionar_lista(self.usuario_logado.id)
                        if(id_lista_selecionada): self._tarefa_view.excluir_tarefa(id_lista_selecionada)
                    
                    case '6':
                        id_lista_selecionada = self._lista_view.selecionar_lista(self.usuario_logado.id)
                        if(id_lista_selecionada): self._lista_view.iniciar_execucao_lista(id_lista_selecionada)
                    
                    case '7': self._lista_view.exibir_listas(self.usuario_logado.id)
                    
                    case '8': break
                
                    case '9': self._menu_view.encerrar_programa()
                
                    case _: self._menu_view.valor_digitado_invalido()
            
if __name__ == '__main__':
    Main()