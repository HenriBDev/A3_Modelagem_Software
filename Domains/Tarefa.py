class Tarefa():
    def __init__(self, id, descricao, status, tempo, lista_id):
        self.id = id
        self.tempo = tempo
        self.status = status
        self.descricao = descricao
        self.lista_id = lista_id