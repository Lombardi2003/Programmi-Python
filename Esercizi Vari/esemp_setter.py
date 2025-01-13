class Cane:
    def __init__(self, nome):
        self._nome = nome

    # Definizione del getter per l'attributo 'nome'
    @property
    def nome(self):
        return self._nome

    # Definizione del setter per l'attributo 'nome'
    @nome.setter
    def nome(self, valore):
        self._nome = valore

# Creazione di un'istanza della classe Cane
cane = Cane("Fido")

# Utilizzo del getter per ottenere il valore di 'nome'
print(cane.nome)  # Output: Fido

# Utilizzo del setter per impostare un nuovo valore a 'nome'
cane.nome = "Rex"

# Verifica del nuovo valore di 'nome' tramite il getter
print(cane.nome)  # Output: Rex
