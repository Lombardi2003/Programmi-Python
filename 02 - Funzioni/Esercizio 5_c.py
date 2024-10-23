# Creare una funzione chamata concatena_strings che
#   1) accetta un numero variabile di stringhe come argomenti posizionali (*args)
#   2) e una stringa separatore opzionale con keyword argument (separaotre)
# La funzione deve concatenare tutte le stringhe passate utilizzando il separatore indicato.
# Esempio:
#   $- concatenate_strings('Hello', 'World', separator='-')
#   $- "Hello-World"
# 
# hint: Usare reduce (https://docs.python.org/3.0/library/functools.html)

import functools as ft

def concatenate_strings(*args, separator=''):
    return ft.reduce(lambda a, b: a+separator+b, args)

print(concatenate_strings("ciao","mondo", separator='###'))