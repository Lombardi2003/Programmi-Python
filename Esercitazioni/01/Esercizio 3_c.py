# Scrivere un programma che prenda un valore inserito dall’utente
# 
# Se è 1 stampa 'red'
# Se è 2 stampa 'blue'
# Se è 3 stampa 'green'
# 
# Negli altri casi stampa un messaggio di errore
# 
# Modificare il programma precedente in modo da non usare if.
# Suggerimento: https://docs.python.org/3/library/stdtypes.html#dict.get

colori = {1:'red', 2:'blue', 3:'green'}
val = int(input("Inserisci un numero: "))
print(colori.get(val,'Errore!!!'))

