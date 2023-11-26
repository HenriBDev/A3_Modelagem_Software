from Models.ModelFactory import ModelFactory
from Controllers.Controller import Controller

class ListaController(Controller):
    
    def verificar_lista_existente(self, descricao: str, usuario_id: str) -> bool:
        return bool(self.model.buscar_lista(descricao, usuario_id))
    
    def cadastrar_lista(self, descricao: str, usuario_id: str):
        self.model.cadastrar_lista(descricao, usuario_id)
            
    def verificar_se_tem_tarefas(self, lista_id) -> bool:
        return len(ModelFactory().instanciar_model('tarefa').buscar_tarefas_por_lista(lista_id)) > 0
    
    def excluir_lista(self, lista_id):  
        self.model.excluir_lista_por_id(lista_id)
    
    def buscar_listas(self, usuario_id):
        return self.model.buscar_listas_do_usuario(usuario_id)
    
    def buscar_tarefas_por_lista(self, lista_id):
        return ModelFactory().instanciar_model('tarefa').buscar_tarefas_por_lista(lista_id)
