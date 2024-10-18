# Utilizzare un'espressione generatrice per creare un generatore che produca
# tutti i numeri dispari tra 0 e un numero n fornito dall'utente.
# 
# Utilizzare il generatore per stampare uno a uno tutti i numeri dispari generati.

num = input("Inserisci l'ultimo numero della sequenza: ")
# Espressione generatrice
print('Stampa della lista creata con una espressione generatrice: ')
lista = (i for i in range(int(num)) if i%2!=0)
print(*list(lista))
# List comprension
print('Stampa della lista creata con la list comprension: ')
lista_e = [i for i in range(int(num)) if i%2!=0]
print(*lista_e)