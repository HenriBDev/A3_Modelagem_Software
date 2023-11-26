class DomainFactory():
    
    def __init__(self, campos):
        for nome_campo in campos.keys():
            setattr(self, nome_campo, campos[nome_campo])