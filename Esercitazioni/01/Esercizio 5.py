# Scrivere un programma che stampi per tutti i numeri da 0 a 100 se sono pari o dispari.
#
# In python il modulo si calcola con l’operatore %

for i in range(101):
    if i%2==0:
        print(f'{i} Pari')
    else:
        print(f'{i} Dispari')