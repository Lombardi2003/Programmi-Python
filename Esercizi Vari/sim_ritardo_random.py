# Funzione che calcola randomicamente un certo numero e lo moltiplica per 5, fa aspettare il pc per il numero trovato e poi stampa quando tempo ci ha messo

# Libreria per prendere il tempo di sistema
import time
# Libreria che restituisce un numero randomico
import random

# Funzione che fa aspettare il pc tramite un numero randomico
def func(x):
    time.sleep( random.random()*x )

start = time.time()
func(5)
end = time.time()
print ("ci ha messo ", end - start, " secondi")