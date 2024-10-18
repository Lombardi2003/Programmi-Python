# Creare una lista di numeri e utilizzare una funzione anonima (lambda) insieme a filter per ottenere una nuova lista contenente solo i numeri pari
#
# Stampare la lista risultante
#
# Successivamente, utilizzare la funzione map per ottenere una lista di quadrati dei numeri pari filtrati

stream = [1,2,3,4,5,6,7,8,9]
# Lista di solo numeri pari
lista = list(filter(lambda val: val if val % 2 == 0 else None,stream))
print(lista)
# Lista dei quadrati dei numeri pari
lista = list(map(lambda val: val**2,lista))
print(lista)