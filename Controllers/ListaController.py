from Models.ModelFactory import ModelFactory

class ListaController:
    
    def verificar_lista_existente(self, descricao: str, usuario_id: str) -> bool:
        return bool(ModelFactory().create_model('lista').buscar_lista(descricao, usuario_id))
    
    def cadastrar_lista(self, descricao: str, usuario_id: str):
        if not self.verificar_lista_existente(descricao, usuario_id):
            ModelFactory().create_model('lista').cadastrar_lista(descricao, usuario_id)
            return True
        else:
            print("A lista não pôde ser cadastrada, pois já existe uma lista com o mesmo nome.")
            return False
            
    def verificar_se_tem_tarefas(self, lista_id) -> bool:
        if len(ModelFactory().create_model('tarefa').buscar_tarefas_por_lista(lista_id)) > 0:
            return True
        return False
    
    def excluir_lista(self, lista_id):
        if not self.verificar_se_tem_tarefas(lista_id):      
            ModelFactory().create_model('lista').excluir_lista_por_id(lista_id)
            return True 
        else:
            print("Não é possível deletar uma lista com tarefas dentro")
            return False
    
    def buscar_listas(self, usuario_id):
        return ModelFactory().create_model('lista').buscar_listas_do_usuario(usuario_id)
    
    def buscar_tarefas_por_lista(self, lista_id):
        return ModelFactory().create_model('tarefa').buscar_tarefas_por_lista(lista_id)
