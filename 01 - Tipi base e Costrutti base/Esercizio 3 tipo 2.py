# Scrivere un programma che prenda un valore inserito dall'utente
#   - Se è 1 stampa 'red'
#   - Se è 2 stampa 'blue'
#   - Se è 3 stampa 'green'
# Negli altri casi stampa un messaggio di errore
#
# Modificare il programma precedente in modo da usare un solo if e nessun elif.
#
# Suggerimento: Dizionari o Liste/Tuple

a = input('Inserisci: ')    
d = {'1':'red', '2':'blue', '3':'green'}
if a in d :
    print(d[a])
else :
    print('Errore')
