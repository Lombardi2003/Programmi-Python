class Canzone:

    def __init__(self, titolo, artista, durata, genere):
        self.titolo = titolo
        self.astista = artista
        self.durata = durata
        self.genere = genere

    def getTitolo(self):
        return self.titolo

    def getGenere(self):
        return self.genere

    def getArtista(self):
        return self.astista

    def getDurata(self):
        return self.durata