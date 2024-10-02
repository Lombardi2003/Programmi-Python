# Scrivere un programma che prenda un valore inserito dall'utente
#   - Se è 1 stampa 'red'
#   - Se è 2 stampa 'blue'
#   - Se è 3 stampa 'green'
# Negli altri casi stampa un messaggio di errore
#
# Modificare il programma precedente in modo da non terminare finchè l'utente non inserisce il testo 'fine'

a = input('Inserisci: ')    
while a!='fine' :
    d = {'1':'red', '2':'blue', '3':'green'}
    print(d.get(a,'Errore'))
    a = input('Inserisci: ')    