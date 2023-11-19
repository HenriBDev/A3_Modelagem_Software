import os, sys
CURRENT_DIR = os.path.dirname(os.path.abspath(__file__))
PARENT_DIR = os.path.dirname(CURRENT_DIR)
sys.path.append(PARENT_DIR)
from model.listaModel import ListaModel
from model.tarefaModel import TarefaModel

class listaController:
    
    def verificar_lista_existente(self,usuario: object,lista: object) -> bool:
        listas_do_usuario = self.exibir_lista(usuario)
        if len(listas_do_usuario) == 0:
            return False
        else:
            for nome_lista in listas_do_usuario:
                if nome_lista[1] == lista.descricao:
                    return True
        
        return False
    
    def cadastrar_lista(self, lista: object, usuario: object):
        if not self.verificar_lista_existente(usuario,lista):
            return ListaModel.cadastrar_lista(lista)
        else:
            print("A lista não pôde ser cadastrada, pois essa lista já está cadastrada.")
            
    def verificar_se_tem_tarefas(self,lista_id) -> bool:
        if len(TarefaModel.verificar_tarefas_na_lista(lista_id)) > 0:
            return True
        
        return False
    
    def deletar_lista(self, lista_id):
            if not(self.verificar_se_tem_tarefas(lista_id)):      
                ListaModel.excluir_lista(lista_id) 
                return True
            return False
    
    def exibir_lista(self, usuario):
        return ListaModel.listar_listas(usuario.id)
