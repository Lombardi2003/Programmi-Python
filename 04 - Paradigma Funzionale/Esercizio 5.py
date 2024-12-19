# Utilizzare il paradigma map e reduce
from functools import *

lista = ["123","456","789"]

num = list(map(lambda x: int(x), lista))

somma = reduce(lambda x,y: x+y, num)

print(somma)