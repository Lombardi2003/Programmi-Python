# Scrivere un programma che prenda un valore inserito dall’utente
# 
# Se è 1 stampa 'red'
# Se è 2 stampa 'blue'
# Se è 3 stampa 'green'
# 
# Negli altri casi stampa un messaggio di errore
# 
# Modificare il programma precedente in modo da usare un solo if e nessun elif.
# Suggerimento: Dizionari o Liste/Tuple

colori = ['red','blue','green']

color = int(input('Inserisci un numero: '))

if color >= 1 & color<=3:
    print(colori[color+1])
else:
    print('Errore!!')