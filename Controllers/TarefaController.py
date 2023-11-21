from Models.TarefaModel import TarefaModel
import time

class TarefaController:
    
    def verificar_tarefa_existe(self, descricao, lista_id) -> bool:
        return bool(TarefaModel().buscar_tarefas_por_descricao(descricao, lista_id))
    
    def cadastrar_tarefa(self, descricao, duracao, lista_id):
        if not self.verificar_tarefa_existe(descricao, lista_id):
            TarefaModel().cadastrar_tarefa(descricao, duracao, lista_id)
        else:
            print("A tarefa não pôde ser cadastrada.")
            
    def deletar_tarefa(self, tarefa_id):
        
        tarefa_model = TarefaModel()
        
        if bool(tarefa_model.buscar_tarefa_por_id(tarefa_id)):
            tarefa_model.excluir_tarefa_por_id(tarefa_id)
        else:
            print("A tarefa não pôde ser excluída.")
            
    def editar_tarefa(self, tarefa_id, descricao, duracao):
        
        tarefa_model = TarefaModel()
        
        if bool(tarefa_model.buscar_tarefa_por_id(tarefa_id)):
            tarefa_model.editar_tarefa_por_id(tarefa_id, descricao, duracao)
        else:
            print("Não há tarefas com esse ID.")

    def concluir_tarefa(self, tarefa_id):
        TarefaModel().concluir_tarefa_por_id(tarefa_id)
        
    def exibir_tarefas(self,lista_id):
        return TarefaModel().buscar_tarefas_por_lista(lista_id)
    
    
    def timer(self, tempo):
        
        timer = tempo
        
        for x in range(timer, 0, -1):
            segundos = x % 60
            minutos = int(x / 60) % 60 
            horas = int(x / 3600)
            print(f'{horas:02}:{minutos:02}:{segundos:02}')
            time.sleep(1)
            
        print('acabou o tempo')