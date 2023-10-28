import uuid

class Tarefa():
    def __init__(self,tempo,status,descricao):
        self.id = uuid.uuid4()
        self.tempo = tempo
        self.status = status
        self.descricao = descricao