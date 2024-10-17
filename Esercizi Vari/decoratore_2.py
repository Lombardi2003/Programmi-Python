# Funzione che raddoppia il risultato di un'addizione tramite un decoratore

# Definizione del decoratore
def raddoppia_risultato(funzione):
    def wrapper(*args, **kwargs):
        risultato = funzione(*args, **kwargs)  # Chiamata alla funzione originale
        return risultato * 2  # Modifica del risultato
    return wrapper

# Utilizzo del decoratore
@raddoppia_risultato
# Funzione di somma
def somma(a, b):
    return a + b

# Chiamata della funzione decorata
risultato = somma(3, 4)
print(risultato)  # Output: 14
