import os, sys
CURRENT_DIR = os.path.dirname(os.path.abspath(__file__))
PARENT_DIR = os.path.dirname(CURRENT_DIR)
sys.path.append(PARENT_DIR)
from model.tarefaModel import TarefaModel

class tarefaController:
    
    def verificar_tarefa_existe(self,tarefa: object, lista_id) -> bool:
        for tarefas in TarefaModel.verificar_tarefas_na_lista(lista_id):
            if tarefas[0] == tarefa.id:
                return True
            
        return False
    
    def cadastrar_tarefa(self, tarefa: object, lista_id):
        if not self.verificar_tarefa_existe(tarefa, lista_id):
            TarefaModel.cadastrar_tarefa(tarefa)

        else:
            print("A tarefa não pôde ser cadastrada.")
            
    def deletar_tarefa(self, tarefa_id):
            TarefaModel.excluir_tarefa(tarefa_id)       
            
    def editar_editar(self, tarefa: object, lista_id):
        if self.verificar_tarefa_existe(tarefa, lista_id):
            TarefaModel.editar_tarefa(tarefa)
        else:
            print("A tarefa não pôde ser editada.")

    def concluir_tarefa(self,tarefa_id):
        TarefaModel.concluir_tarefa(tarefa_id)

    def exibir_tarefa(self,lista_id):
        return TarefaModel.exibir_tarefas(lista_id)
