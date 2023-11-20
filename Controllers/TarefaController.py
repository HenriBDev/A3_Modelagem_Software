from Models.TarefaModel import TarefaModel

class TarefaController:
    
    def verificar_tarefa_existe(self, tarefa: object, lista: object) -> bool:
        return TarefaModel().buscar_tarefas_por_lista(lista)[0][0] == tarefa.id
    
    def cadastrar_tarefa(self, tarefa: object, lista: object):
        if not self.verificar_tarefa_existe(tarefa, lista):
            TarefaModel().cadastrar_tarefa(tarefa)
        else:
            print("A tarefa não pôde ser cadastrada.")
            
    def deletar_tarefa(self, tarefa: object, lista: object):
        if self.verificar_tarefa_existe(tarefa, lista):
            TarefaModel().excluir_tarefa_por_id(tarefa)
        else:
            print("A tarefa não pôde ser excluída.")
            
    def editar_tarefa(self, tarefa: object, lista: object):
        if not self.verificar_tarefa_existe(tarefa, lista):
            TarefaModel().editar_tarefa_por_id(tarefa)
        else:
            print("A tarefa não pôde ser editada.")

    def concluir_tarefa(self, tarefa):
        TarefaModel().concluir_tarefa_por_id(tarefa)