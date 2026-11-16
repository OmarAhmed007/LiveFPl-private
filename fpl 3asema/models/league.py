class league:
    def __init__(self,id,name,managers):
        self.id = id
        self.name = name
        self.managers = managers if managers is not None else []