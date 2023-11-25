import os
from Views.ViewFactory import ViewFactory

class Main():
    
    def __init__(self) -> None:
        
        self._view_factory = ViewFactory()
        self._menu_view = self._view_factory.instanciar_view('menu')
        self._usuario_view = self._view_factory.instanciar_view('usuario')
        self._lista_view = self._view_factory.instanciar_view('lista')
        self._tarefa_view = self._view_factory.instanciar_view('tarefa')
        self.usuario_logado = None
        
        os.system('cls' if os.name=='nt' else 'clear')
        
        while True:
            
            while True:
                
                valor_digitado = self._menu_view.menu_inicial()
                
                if(valor_digitado == '1'):
                    
                    while True:
                        
                        self.usuario_logado = self._usuario_view.logar_usuario()
                        if not self.usuario_logado: 
                            if self._menu_view.voltar_menu_inicial() == True: break
                        else: break
                        
                    if bool(self.usuario_logado): break
                    
                elif(valor_digitado == '2'): 
                    
                    while True:
                        
                        usuario_foi_cadastrado = self._usuario_view.cadastrar_usuario()
                        if not usuario_foi_cadastrado: 
                            if self._menu_view.voltar_menu_inicial() == True: break
                        else: break
                    
                elif(valor_digitado == '3'): self._menu_view.encerrar_programa()
                    
                else: self._menu_view.valor_digitado_invalido()
                
            while True:
                
                valor_digitado = self._menu_view.menu_principal(self.usuario_logado)
                    
                if valor_digitado == '1': self._lista_view.cadastrar_lista(self.usuario_logado.id)
                    
                elif valor_digitado == '2': self._lista_view.excluir_lista(self.usuario_logado.id)
                    
                elif valor_digitado == '3':
                    id_lista_selecionada = self._lista_view.selecionar_lista(self.usuario_logado.id)
                    self._tarefa_view.cadastrar_tarefa(id_lista_selecionada)
                    
                elif valor_digitado == '4':
                    id_lista_selecionada = self._lista_view.selecionar_lista(self.usuario_logado.id)
                    self._tarefa_view.editar_tarefa(id_lista_selecionada)
                    
                elif valor_digitado == '5': self._lista_view.iniciar_execucao_lista(self.usuario_logado.id)
                    
                elif valor_digitado == '6':
                    id_lista_selecionada = self._lista_view.selecionar_lista(self.usuario_logado.id)
                    self._tarefa_view.excluir_tarefa(id_lista_selecionada)
                    
                elif valor_digitado == '7': self._lista_view.exibir_listas(self.usuario_logado.id)
                    
                elif valor_digitado == '8': break
                
                elif valor_digitado == '9': self._menu_view.encerrar_programa()
                
                else: self._menu_view.valor_digitado_invalido()
            
if __name__ == '__main__':
    Main()