import os, sys
CURRENT_DIR = os.path.dirname(os.path.abspath(__file__))
PARENT_DIR = os.path.dirname(CURRENT_DIR)
sys.path.append(PARENT_DIR)
from model.listaModel import ListaModel

class listaController:
    
    def verificar_lista_existente(lista: object) -> bool:
        if len(ListaModel.listar_listas(lista.usuario_id)) == 0:
            return False
        else:
            for nome_lista in ListaModel.listar_listas():
                if nome_lista[1] == lista.descricao:
                    return True
        
        return False
    
    def cadastrar_lista(self, lista: object):
        if not self.verificar_lista_existente(lista):
            return ListaModel.cadastrar_lista(lista)
        else:
            print("A lista não pode ser cadastrada.")