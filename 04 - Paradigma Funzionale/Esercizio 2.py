# Partendo da una stringa molto lunga di caratteri minuscoli, scrivere una sequenza di espressioni che tengano solo le consonanti e le renda maiuscole
# Provare a contare la frequenza di ogni lettera filtrata

from functools import *

s = input("Inserisci frase: ")
cons = list(filter(lambda i: i not in ['a','e','i','o','u'],s))
caps = list(map(lambda x: x.upper(),cons))
print("Stampa delle consonanti rese maiuscole: ", *cons)

print(reduce(lambda acc,x: acc | {x: acc.get(x,0)+1}, caps,{}))


# oppure

from collections import Counter
h = Counter(caps)
for i in h:
    print(i, h[i])