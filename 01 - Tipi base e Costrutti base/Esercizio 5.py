# Scrivere un programma che stampi per tutti i numeri da 0 a 100 se sono pari o dispari
# 
# In python il modulo si calcola con l'operatore %

for i in range(0,101) :
    if i%2==0 :
        print(i,' = Pari')
    else :
        print(i,' = Dispari')
    i=i+1