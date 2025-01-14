# Scrivere un programma che prenda un valore inserito dall’utente e mostri a video
# il tipo che assume la variabile in cui viene inserito.
# 
# Aiutatevi con la funzione type()


var = input('Inserisci un testo: ')

print(f'Hai inserito questo: {var}')

print(f'Il testo inserito è di tipo: {type(var)}')