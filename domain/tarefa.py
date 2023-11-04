import uuid

class Tarefa():
    def __init__(self,descricao):
        self.id = uuid.uuid4()
        self.tempo = None
        self.status = False
        self.descricao = descricao