# Funzione iterativa che calcola il numero di fibonacci su quello inserito
def fib_i(n):
    a, b = 0, 1
    for i in range(n):
        print(b)
        a, b = b, a + b

# Funzione ricorsiva che calcola il numero di fibonacci su quello inserito
def fib_r(n):
    if n == 1:
        print(1)
        return 0, 1
    a, b = fib_r(n - 1)
    print(a + b)
    return b, a + b

# Inserimento del numero da tastiera
x = int(input("Inserisci un numero: "))
# Chiamata alla funzione del numero di fibonacci in maniera iterativa
print(f"Numero di fibonacci su {x} con la funzione iterativa")
fib_i(x)
# Chiamata alla funzione del numero di fibonacci in maniera ricorsiva
print(f"Numero di fibonacci su {x} con la funzione ricorsiva")
fib_r(x)