from Controllers.ControllerFactory import ControllerFactory
from Models.ModelFactory import ModelFactory
from Controllers.Controller import Controller

class ListaController(Controller):
    
    def cadastrar_lista(self, nome: str, usuario_id: str):
        busca_lista = self.model.buscar_listas(filtros={'descricao': nome, 'usuario_id': usuario_id})
        
        if len(busca_lista) > 0:
            return "A lista não pôde ser cadastrada, pois já existe uma lista com o mesmo nome.\n"

        self.model.cadastrar_lista(nome, usuario_id)
        return "ok"
    
    def excluir_lista_do_usuario(self, lista_id, usuario_id):
        busca_lista = self.model.buscar_listas(filtros={'id': lista_id, 'usuario_id': usuario_id})
        
        if len(busca_lista) == 0:
            return "Você não possui nenhuma lista com esse ID"
        
        busca_tarefas = ModelFactory().instanciar_model('tarefa').buscar_tarefas(filtros={"lista_id": lista_id})
        
        if len(busca_tarefas) > 0:
            return "Não é possível deletar uma lista com tarefas dentro"
        
        self.model.excluir_lista_por_id(lista_id)
        return "ok"
        
    def buscar_lista_do_usuario_por_id(self, lista_id, usuario_id):
        busca_lista = self.model.buscar_listas(filtros={'id': lista_id, 'usuario_id': usuario_id})
        
        if len(busca_lista) == 0:
            return ("Você não possui nenhuma lista com esse ID", False)
        
        return ("ok", busca_lista[0])
    
    def buscar_listas_do_usuario(self, usuario_id, incluir_tarefas = False):
        listas = self.model.buscar_listas(filtros={'usuario_id': usuario_id})
        
        if len(listas) == 0:
            return ("Você não possui nenhuma lista\n", False)
        
        if incluir_tarefas == False:
            return ("ok", listas)
        else:
            tarefa_controller = ControllerFactory().instanciar_controller('tarefa')
            listas_com_tarefas = []
            for lista in listas:
                msg_retorno, tarefas = tarefa_controller.buscar_tarefas_por_lista(lista.id)
                listas_com_tarefas.append({
                    'lista': lista,
                    'tarefas': tarefas if tarefas != False else []
                })
            return ("ok", listas_com_tarefas)
