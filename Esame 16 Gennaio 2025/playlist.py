from contextlib import nullcontext

from canzoni import *

class Playlist:

    def __init__(self, titolo, data_creazione, descrizione):
        self.titolo = titolo
        self.data_creazione = data_creazione
        self.descrizione = descrizione
        self.canzoni = list()

    def getTitolo(self):
        return self.titolo

    def getCanzoni(self):
        return self.canzoni

    def getDataCreazione(self):
        return self.data_creazione

    def getDescrizione(self):
        return self.descrizione

    def decora_durata(fun):
        def wrapper(*args,**kwargs):
            durata = fun(*args,**kwargs)
            if durata == None or durata == "":
                print("Durata brano non valida")
                return 0
            else:
                if int(durata) < 0:
                    print("Durata brano non valida")
                    return 0
                return int(durata)
        return wrapper

    @decora_durata
    def durataBrano(self):
        return input("Inserisci la durata della canzone in minuti: ")

    def creaCanzone(self):
        titolo = input("Inserisci il titolo della canzone: ")
        artista = input("Inserisci il nome dell'artista: ")
        durata = self.durataBrano()
        if durata == 0:
            print("Brano non caricato")
            return 0
        genere = input("Inserisci il genere della canzone: ")
        self.canzoni.append(Canzone(titolo, artista, durata, genere))
        print("Brano inserito")

    def visualizzaCanzoni(self):
        if self.canzoni == []:
            print("Nessun brano presente in questa playlist")
        else:
            c = 0
            for canzone in self.canzoni:
                print(f'{c}. {canzone.getTitolo()} - {canzone.getGenere()}')
                c += 1