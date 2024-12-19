# Partendo da una stringa molto lunga di caratteri minuscoli, scrivere una sequenza di espressioni che tengano solo le consonanti e le renda maiuscole
from functools import *

s = input("Inserisci frase: ")

ret = list(filter(lambda i: i not in ['a','e','i','o','u'],s))

caps = list(map(lambda x: x.upper(),ret))

print("Stampa delle consonanti rese maiuscole: ", *ret)
