# Scrivere una funzione chiamata create_multiplier che
#   1) accetta un numero come argomento e
#   2) restituisce una closure.
# Questa closure deve accettare un altro numero e restituire il prodotto dei due numeri.
# Esempio:
#   $- multiply_by_3 = create_multiplier(3)
#   $- print(multiply_by_3(10)) # Output: 30

def create_multiplier(arg):
    def f(num):
        return num*arg
    return f

multiply_by_5=create_multiplier(5)
print(multiply_by_5(10))