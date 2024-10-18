# Creare una funzione chamata concatena_strings che
#   1) accetta un numero variabile di stringhe come argomenti posizionali (*args)
#   2) e una stringa separatore opzionale con keyword argument (separaotre)
# La funzione deve concatenare tutte le stringhe passate utilizzando il separatore indicato.
# Esempio:
#   $- concatenate_strings('Hello', 'World', separator='-')
#   $- "Hello-World"
# 
# hint: Usare reduce (https://docs.python.org/3.0/library/functools.html)

sep = input('Inserire il separatore: ')
num = input('Inserire il numero di stringhe che si vuole immettere: ')

def concatena_strings(*args, separator=' '):
    return separator.join(args)  # Utilizziamo join per unire le stringhe con il separatore

lista = []

for i in range(int(num)):
    lista.append(input('Inserisci una stringa: '))

print(concatena_strings(*lista, separator=sep))