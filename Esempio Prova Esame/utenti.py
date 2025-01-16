from magazzino import *
class Utente:
    def __init__(self, username):
        self.__username = username  # lo dichiaro privato perché non voglio permettere modifiche esterne
        self.magazzino = Magazzino()
    def __str__(self):
        return self.__username
    @property
    def username(self):
        return self.__username