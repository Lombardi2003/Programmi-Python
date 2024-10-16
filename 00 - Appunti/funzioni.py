# Le funzioni si definiscono con la parola chiave def <nome_funzione>, sono indendate in un blocco che corrisponde al corpo della funzione
#
# Si può passare qualunque oggetto, quando viene passato si può inserire anche il nome dell'oggetto corrispondente al parametro della funzione, ciò
# significa che si può eseguire un assegnamento tramite un keyword argument (una chiave che identifica il parametro passato) e non solo positional argument (dalla posizione
# di ciò che viene passato). Si dice Parametro Opzionale se si assegna un valore di default al parametro quando non gli viene passato nulla.
#
# Una funzione può ritornare uno o più oggetti e assegnarli a delle variabili

# Funzione f: stampa gli argomenti passati (se al secondo posto non viene passato nulla viene preso in default 0) e li stampa.
print('\nFunzione f:')
def f(arg1, arg2=0) :
    print(f'arg1 = {arg1} e arg2 = {arg2}')
    return True, 3, 'pippo', []
# In questo modo viene ritornato un valore booleano, un intero, una stringa e una lista, salvandole nelle rispettive variabili
b, i, s, l = f('ciao')
# Si crea una lista e la funzione prenderà gli elementi della lista come propri argomenti
l1 = ['pippo',2]
f(*l1)
# Si crea un dizionario e la funzione prenderà gli elementi del dizionario come propri argomenti
d = {'arg1':'pluto','arg2':42}
f(**d)

#######

# Funzione m: stampa gli argomenti passati, stampa anche tutti gli argomenti nella tupla args e con le chiavi dentro al dizionario kwargsh
print('\nFunzione m:')
def m(arg1, arg2, *args, **kwargsh) : 
    print(arg1)
    print(arg2)
    # Stampa degli argomenti della tupla tutti insieme
    print(args)
    # Stampa degli argomenti della tupla uno alla volta
    for arg in args :
        print(arg)
    # Stampa degli argomenti del dizionario tutti insieme
    print(kwargsh)
    # Stampa degli argomenti del dizionareio uno alla volta
    for k in kwargsh : 
        print(f'chiave: {k}')
        print(f'valore: {kwargsh[k]}')
# Si assegna degli argomenti alla funzione
m(1,2,3,4,5, x='pippo', y='pluto', z=3.5)

#######

# Funzione g: esempio di programmazione di ordine superiore, definizione di una funzione h interna, ritorno di questa funzione che stampa la parola help
#             ad una variabile di nome res e vedere la differenza di ciò che stampa la variabile con e senza parentesi tonde ()
print('\nFunzione g:')
def g():
    def h():
        # Stampa della parola help
        print('help')
    return h
# La variabile res prende una funzione
res = g()
# Stampa di res senza le parentesi
print(res)
# Stampa di res con le parentesi
print(res())

#######

# Funzione z: esempio di programmazione di ordine superiore, in particolare del CLOSURE, cioè che la funzione all'interno di un'altra funzione può accedere a 
#             una argomento della funzione padre. In questo caso, la funzione y stampa l'argomento che gli viene passato alla funzione padre z; dopodichè
#             una variabile di nome res1 prende la funzione y che la stampera con e senza parentesi nella direttiva print
print('\nFunzione z:')
def z(arg):
    def y():
        # Stampa dell'argomento della funzione padre z
        print(arg)
    return y
# La variabile res1 prende la funzione y
res1 = z('pippo')
# Stampa di res1 senza le parentesi
print(res1)
# Stampa di res1 con le parentesi
print(res1())

#######

# Funzione r: esempio di programmazione di ordine superiore, in particolare la funzione map, che prende come argomenti un oggetto e una funzione che viene applicata
#             all'oggetto stesso. In questo caso viene convertito in un oggetto lista, che a sua volta viene stampato
print('\nFunzione r:')
def r(a):
    return a**2
# Stampa dell'oggetto lista proveniente da map
print(list(map(r, [1,2,3])))

#######

# Funzioni p: esempio di programmazione di ordine superiore, in particolare la funzione anonima lambda applicata alla funzione map. In questo contesto, prima viene
#             visto come una funzione p che preso come argomento un intero ne ritorna il quadrato del numero passato può essere sostiutita da una funzione anonima che
#             che si esprime con lambda. In questo caso c'è l'esempio che oltre al quadrato si può eseguire anche altre operazione come un aggiunta di due (+2)
print('\nFunzione p:')
# Funzione che restituisce il quadrato dell'intero passato
def p(i) :
    return i*i
# Ciclo che stampa la lista tutta al quadrato dopo essere passata dalla funzione p
for i in map(p, [1,2,3,4]) :
    print(i)
print(' ')
# Ciclo che stampa la lista tutta al quadrato dopo essere passata da una funzione anonima lambda
for i in map(lambda i: i**2, [1,2,3,4]) :
    print(i)
print(' ')
# Ciclo che stampa la lista con aggiuna di due ai membri dopo essere passata da una funzione anonima lambda
for i in map(lambda i: i+2, [1,2,3,4]) :
    print(i)

#######

# Funzioni my_range: esempio di funzioni generatrici, la funzione crea e ritorna una sequenza di valori da 0 fino allo stop, cioè fino all'argomento passato alla funzione.
#                    Viene stampato prima il risultato della funzione e poi viene applicata ad un for. Infine stanno degli esempi dove la stessa cosa può essere eseguita come
#                    espressione generatrice per la creazione di liste
print('\nFunzione my_range:')
# Funzione che ritorna un numeor e si ferma quando arriva all'argomento passato
def my_range(stop) :
    i = 0
    while i < stop :
        yield i
        i = i + 1
# Stampa della funzione my_range
print(my_range(10))
# La funzione generatrice viene applicata ad un ciclo for
for i in my_range(10) :
    print(i)
print('\n')
# Espressione generatrice
print(j for j in range(10))
# Espressione generatrice applicata ad un ciclo for
for j in (j**2 for j in range(10)) :
    print(j)
# Espressione generatrice applicata alla creazione di una lista
print(' ')
list_comprension = [i*2 for i in range(10)]
print(list_comprension)
# Espressione generatrice più complessa applicata alla creazione di una lista
list_comprension2 = [i*j for i in range(10) for j in range(5)]  # 5 elementi alla volta
print(list_comprension2)

#######

# Funzioni f_scope: esempio di variabile locale e globale per capire come funziona la scope di un programma, la funzione all'interno dichiara una variabile localmente
#                   di nome come la variabile globale x, che a sua volta la funzione la gestirà in maniera locale e la distrugerà una volta che la funzione termina
print('\nFunzione f_scope:')
x = 0
# Funzione che dichiara la x in maniera locale e solo localmente ne cambia il valore, non globalmente
def f_scope():
    x = 11
    print(x)
f_scope()
print(x)

#######

# Funzioni f_scope_2: esempio di variabile locale e globale per capire come funziona la scope di un programma, la funzione all'interno chama la variabile globale x e ne
#                     cambia il valore in maniera globale
print('\nFunzione f_scope_2:')
x = 0
# Funzione che richiama la variabile globale per cambiarne il valore
def f_scope_2():
    global x
    x = 11
    print(x)
f_scope_2()
print(x)

#######

# Funzioni f_exception: esempio di gestione delle eccezioni, funzione che quando chiamata viene solleva un eccezione, che viene gestita in un try - catch
print('\nFunzione f_exception:')
x = 0
# Funzione per il sollevamento dell'eccezione
def f_exception():
    if x > 0 :
        print(x)
    else:
        raise Exception('The argument should be greater than 0')
# Blocco per la gestione dell'eccezzione
try:
    f_exception(x)
    print("Tutto ok!!!")
except Exception as e :
    print(f'Eccezione: {e}')
else :
    print("Else!!!")
finally:
    print("Finally!!!")

#######

# Funzioni z: esempio una funzione che ritorna una funzione che utilizza come parametro la funzione passata in ingresso al padre. Viene ritornata la funzione function che utilizza la funzione t passata come parametro
#             a z, funzione padre e restituisce il risultato della funzione t passandogli *args e **kwargs
print('\nFunzione z:')
# Funzione padre che prende in ingresso una funzione
def z(t):
    # Funzione figlia che prende in ingresso dei valori
    def function(*args, **kwargs):
        # Ritorno della funzione passata al padre con gli argomenti passati alla funzione figlia
        return t(*args, **kwargs)
    # Ritorno della funzione
    return function
# Generica funzione per fare una prova
def pippo(x,y,p):
    print(x)
    print(y)
    print(p)
# Creazione di una variabile funzione
new_func = z(pippo)
# Chiamata alla funzione
new_func(1,2,3)
# Funzione pippo
pippo(1,2,3)

#######

# Funzioni z_2: esempio una funzione che ritorna una funzione che utilizza come parametro la funzione passata in ingresso al padre. Viene ritornata la funzione function che utilizza la funzione t passata come parametro
#             a z, funzione padre e restituisce il risultato della funzione t passandogli *args e **kwargs -> tutto questo fatto tramite una funzione con il decoratore
print('\nFunzione z_2:')
# Funzione padre che prende in ingresso una funzione
def z(t):
    # Funzione figlia che prende in ingresso dei valori
    def function(*args, **kwargs):
        # Stampa di una generica stringa
        print('ciao')
        return t(*args, **kwargs)
    return function
# Decoratore applicato alla funzione pippo -> uguale a dire z(pippo)(1,2,3)
@z
# Generica funzione per fare una prova
def pippo(x,y,p):
    print(x)
    print(y)
    print(p)
# Funzione pippo -> in questo caso è uguale a dire z(pippo)(1,2,3) perchè la funzione pippo è decorata con la funzione z
pippo(1,2,3)