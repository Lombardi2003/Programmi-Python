from playlist import Playlist


class Utente:
    def __init__(self, nome):
        self.nome = nome
        self.playlist = list()

    def getNome(self):
        return self.nome

    def decora_titolo(fun):
        def wrapper(*args,**kwargs):
            titolo = fun(*args,**kwargs)
            if titolo == None or titolo == "":
                print("Titolo non valido")
                return 0
            else:
                return titolo
        return wrapper

    @decora_titolo
    def titoloPlaylist(self):
        return input("Inserisci il titolo della playlist: ")

    def creaPlaylist(self):
        titolo = self.titoloPlaylist()
        if titolo == 0:
            print("Playlist non creata")
            return 0
        data_creazione = input("Inserisci la data di creazione: ")
        descrizione = input("Inserisci la descrizione della playlist: ")
        self.playlist.append(Playlist(titolo, data_creazione, descrizione))
        print("Playlist creata")

    def visualizzaPlaylist(self):
        if self.playlist == []:
            print("Nessuna playlist presente")
        else:
            print("Playlist presenti:")
            c = 1
            for p in self.playlist:
                print(f"{c}. {p.getTitolo()}")
                c += 1

    def inserisciBrano(self):
        if self.playlist == []:
            print("Nessuna playlist presente")
        else:
            self.visualizzaPlaylist()
            indice = int(input("\nInserisci il numero della playlist in cui vuoi inserire il brano: ")) - 1
            self.playlist[indice].creaCanzone()

    def visualizzaBrani(self):
        if self.playlist == []:
            print("Nessuna playlist presente")
        else:
            self.visualizzaPlaylist()
            self.playlist[int(input("Inserisci il numero della playlist: ")) - 1].visualizzaCanzoni()

    def filtraggioBrani(self):
        if self.playlist == []:
            print("Nessuna playlist presente")
        else:
            brani = list()
            genere = input("Inserisci il genere dei brani che vuoi visualizzare: ")
            for p in self.playlist:
                for c in p.getCanzoni():
                    brani.append(c)
            if brani == []:
                print("Nessun brano presente")
            else:
                for b in brani:
                    if b.getGenere() == genere:
                        print(f'{b.getTitolo()} - {b.getGenere()}')
    def filtraggioBrani_backgraund(self,genere):
        brani = list()
        for p in self.playlist:
            for c in p.getCanzoni():
                brani.append(c)
        return brani

    def esportaPlaylist(self):
        if self.playlist == []:
            print("Nessuna playlist presente")
        else:
            self.visualizzaPlaylist()
            indice = int(input("\nInserisci il numero della playlist che si vuole esportare: ")) - 1
            scelta = int(input("Inserire 0 per esportare tutta la playlist, 1 un elenco filtrato per genere:"))
            nome = self.playlist[indice].getTitolo()
            if scelta == 0:
                p = self.playlist[indice]
                with open(f"Playlist {nome}.txt", "w") as f:
                    f.write(f"{p.getTitolo()} - {p.getDataCreazione()} - {p.getDescrizione()}\n")
                    f.write("BRANI:\n")
                    for c in p.getCanzoni():
                        f.write(f"{c.getTitolo()} - {c.getArtista()} - {c.getGenere()} - {c.getDurata()} min\n")
            else:
                brani = list()
                genere = input("Inserisci il genere dei brani che vuoi esportare: ")
                p = self.playlist[indice]
                for c in p.getCanzoni():
                    brani.append(c)
                with open(f"Playlist {nome}_{genere}.txt", "w") as f:
                    f.write(f"{p.getTitolo()} - {p.getDataCreazione()} - {p.getDescrizione()}\n")
                    f.write("BRANI:\n")
                    for b in brani:
                        if b.getGenere() == genere:
                            f.write(f"{b.getTitolo()} - {b.getArtista()} - {b.getGenere()} - {b.getDurata()} min\n")
            print("Playlist esportata")
