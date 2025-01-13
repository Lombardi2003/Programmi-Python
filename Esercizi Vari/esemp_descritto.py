class Temperatura:
    def __init__(self):
        self.__value = 0

    def __get__(self, instance, owner):
        return self.__value

    def __set__(self, instance, value):
        if value < -273.15:  # Limite minimo teorico della temperatura (zero assoluto)
            raise ValueError("La temperatura non può essere inferiore a -273.15 gradi!")
        self.__value = value

class Frigorifero:
    temperatura = Temperatura()

    def __init__(self, marca):
        self.marca = marca

# Creazione di un'istanza di Frigorifero
frigo = Frigorifero("Samsung")

# Impostazione della temperatura
frigo.temperatura = -10
print(f"La temperatura del {frigo.marca} è impostata a {frigo.temperatura} gradi.")

# Tentativo di impostare una temperatura non valida
try:
    frigo.temperatura = -300
except ValueError as e:
    print(e)
