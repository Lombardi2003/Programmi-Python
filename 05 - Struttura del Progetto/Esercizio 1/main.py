from cane import Cane
from gatto import Gatto

# Creazione di istanze per testare la classe Cane
cane1 = Cane(4, True, 2, 'Maschio')
cane2 = Cane(4, True, 3, 'Femmina')
print(f'Il numero di istanze create della classe Cane è {Cane.istanze()}')

if cane1.malato:
    print('Il cane è malato')
else:
    print('Il cane non è malato')

cane1.abbaia()
cane1.malato = True

if cane1.malato:
    print('Il cane è malato')
else:
    print('Il cane non è malato')

# Test dell'operatore + per la classe Cane
cucciolo = cane1 + cane2
print(f"Il cucciolo è un {cucciolo.sesso}")

# Creazione di istanze per testare la classe Gatto
gatto1 = Gatto(4, 1, 20,'Femmina')
gatto2 = Gatto(4, 2, 21,'Maschio')
print(f'Il numero di istanze create della classe Gatto è {Gatto.istanze()}')

gatto1.Miagola()