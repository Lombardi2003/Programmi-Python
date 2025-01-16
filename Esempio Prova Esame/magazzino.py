from datetime import datetime
class Oggetto:
    def __init__(self, nome, quantita):
        self.__nome = nome
        self.__quantita = quantita
    def __str__(self):
        return self.__nome
    def __repr__(self):
        return self.__nome
    @property
    def nome(self):
        return self.__nome
    @property
    def quantita(self):
        return self.__quantita
    def esaurito(self):
        return self.__quantita <= 0
    def preleva(self):
        if self.esaurito():
            raise ValueError('Oggetto esaurito')
        self.__quantita -= 1
        return f'Oggetto {self.nome} prelevato, (rimangono {self.quantita})'
    def restituisci(self):
        self.__quantita += 1
        return f'Oggetto {self.nome} restituito (quantità in magazzino {self.quantita})'

class Movimento:
    def __init__(self, oggetto, causale):
        self.__oggetto = oggetto
        self.__causale = causale
        self.__data = datetime.now()
    def __str__(self):
        return f'{self.__causale} in data {self.__data}'
    def __repr__(self):
        return self.__str__()
    @property
    def oggetto(self):
        return self.__oggetto
    @property
    def causale(self):
        return self.__causale
    @property
    def data(self):
        return self.__data

class Magazzino:
    def __init__(self):
        self.oggetti = list()
        self.movimenti = list()
    def stampa_oggetti(self):
        if not self.oggetti:
            raise IndexError('Nessun oggetto in magazzino')
        else:
            for ind in range(len(self.oggetti)):
                print(f'{ind + 1}. {self.oggetti[ind]}')
    def add_oggetto(self, nome, qta):
        self.oggetti.append(Oggetto(nome, qta))
    def rm_oggetto(self, obj):
        if obj not in self.oggetti:
            raise IndexError('Oggetto non in magazzino')
        self.oggetti.remove(obj)
        print(f'Oggetto eliminato')
    def preleva_oggetto(self, obj):
        if obj not in self.oggetti:
            raise IndexError('Oggetto non in magazzino')
        self.movimenti.append(Movimento(obj, obj.preleva()))
        print(f'Oggetto {obj} prelevato')
    def restituisci_oggetto(self, obj):
        if obj not in self.oggetti:
            raise IndexError('Oggetto non in magazzino')
        self.movimenti.append(Movimento(obj, obj.restituisci()))
        print(f'Oggetto {obj} restituito')
    def get_movimenti(self, obj):
        if obj not in self.oggetti:
            raise IndexError('Oggetto non in magazzino')
        return list(filter(lambda x: x.oggetto == obj, self.movimenti))
    def export_movimenti(self, obj, username):
        if obj not in self.oggetti:
            raise IndexError('Oggetto non in magazzino')
        with open(f'{username}_{obj.nome}.txt', 'w') as exp:
            movimenti = self.get_movimenti(obj)
            for m in movimenti:
                exp.write(f'{m}\n')
        print(f'Movimenti di {obj} esportati')