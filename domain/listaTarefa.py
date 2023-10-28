import uuid

class ListaTarefa():
    def __init__(self):
        self.id = uuid.uuid4()
        self.tarefa = None