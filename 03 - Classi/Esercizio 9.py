# Provare a scrivere un decoratore che si comporti come @property.
# (limitarsi alle funzionalità get per accedere al dato tralasciando le funzionalità set e
# delete)

class my_property:
    def __init__(self, getter):
        self.getter = getter  # Salva la funzione di getter

    def __get__(self, instance, owner):
        if instance is None:
            return self
        return self.getter(instance)  # Chiama la funzione getter


# Esempio di utilizzo
class Prova:
    def __init__(self, valore):
        self._valore = valore

    @my_property
    def valore(self):
        return self._valore  # Restituisce l'attributo privato _valore


# Test
oggetto = Prova(42)
print(oggetto.valore)  # Output: 42
