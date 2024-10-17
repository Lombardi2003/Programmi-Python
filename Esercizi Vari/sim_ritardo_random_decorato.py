# Funzione che calcola randomicamente un certo numero e lo moltiplica per 5, fa aspettare il pc per il numero trovato e poi stampa quando tempo ci ha messo

# Libreria per prendere il tempo di sistema
import time
# Libreria che restituisce un numero randomico
import random

# Funzione che funge da decoratore
def time_function(function):
    def new_function(*args, **kwargs):
        start = time.time()
        value = function(*args, **kwargs)  # Passa argomenti alla funzione originale
        end = time.time()
        print("Ci ha messo", end - start, "secondi")
        return value
    return new_function
# Decoratore per la funzione
@time_function
# Funzione che fa aspettare il pc tramite un numero randomico
def func4(x, y, z):
    time.sleep(random.random() * x + (y - z))

# Chiamata della funzione decorata
func4(5, 3, 1)