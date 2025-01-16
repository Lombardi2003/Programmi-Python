class Richieste:
    def __init__(self,ore,status):
        self.ore = ore
        self.status = status

    def get_ore(self):
        return self.ore
    
    def get_status(self):
        return self.status
    
    def set_status(self,x):
        self.status = x