import os, sys
CURRENT_DIR = os.path.dirname(os.path.abspath(__file__))
PARENT_DIR = os.path.dirname(CURRENT_DIR)
sys.path.append(PARENT_DIR)
from model.tarefaModel import TarefaModel

class tarefaController:
    
    def verificar_tarefa_existe(tarefa: object, lista: object) -> bool:
        for tarefas in TarefaModel.verificar_tarefas_na_lista(lista):
            if tarefas[0] == tarefa.id:
                return True
            
        return False
    
    def cadastrar_tarefa(self, tarefa: object, lista: object):
        if not self.verificar_tarefa_existe(tarefa, lista):
            TarefaModel.cadastrar_tarefa(tarefa)
        else:
            print("A tarefa não pôde ser cadastrada.")
            
    def deletar_tarefa(self, tarefa: object, lista: object):
        if self.verificar_tarefa_existe(tarefa, lista):
            TarefaModel.excluir_tarefa(tarefa)
        else:
            print("A tarefa não pôde ser excluída.")
            
    def editar_editar(self, tarefa: object, lista: object):
        if not self.verificar_tarefa_existe(tarefa, lista):
            TarefaModel.editar_tarefa(tarefa)
        else:
            print("A tarefa não pôde ser editada.")

    def concluir_tarefa(tarefa):
        TarefaModel.concluir_tarefa(tarefa)