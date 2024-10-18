# In Python non c'è bisogno di specificare il tipo delle variabili, ogni cosa in Python è un oggetto

##### NUMERICS #####
# I tipi numerics sono definiti da:
#  - numeri interi, dove la lunghezza di questi numeri sono senza limiti fino a quando c’è memoria → no overflow
#  - numeri float, con precisione che dipende dall’architettura e avente separatore parte intera/decimale “.”
#  - numeri complessi, formato da un numero reale e un numero reale con suffisso j
#  - booleani, considerati sottotipo degli interi

a = 1
b = 2
print(f"Variabili intere a = {a} e b = {b}")
# Operazioni possibili sui numerics sono
print("\tAddizione (a + b): ", a + b)
print("\tSottrazione (a - b): ",a - b)
print("\tMoltiplicazione (a * b): ",a * b)
print("\tDivisione (a / b): ",a / b)
print("\tDivisione intera (a // b): ",a // b)
print("\tResto divisione intera (a % b): ",a % b)
print("\tValore assoluto (abs(a)): ",abs(a))
print("\tElevamento a potenza (pow(b) oppure **): ",b**2)
print("\tArrotondamento (math.trunc() oppure round() o ...) [round(a)]: ",round(a))

print("\n")

##### SEQUENZE #####
# Le sequenze ordinate di elementi sono le
#  - stringhe, racchiuse tra '' oppure "" con la possibilità di usare caratteri speciali come \n e immutabiili nel tempo
#  - liste, elementi di qualsiasi tipo, anche non coerenti, racchiusi tra []
#  - tuple, elementi di qualsiasi tipo, anche non coerenti, racchiusi tra () e immutabili nel tempo
#
# Le operazioni possibili sono
#  - accesso: ad un elemento (a[1]), a delle sottoliste/sottostringhe (a[1:3]) oppure partendo dal fondo (a[-1])
#  - concatenazione: degli esempi sono 'a' + 'b' = 'ab' oppure [1,2] + [3,4] = [1,2,3,4]
#  - ripetizione: degli esempi sono 'a' * 4 = 'aaaa' oppure [1] * 4 = [1,1,1,1]
#  - lunghezza della sequenza: funzione len() -> len(a) = 1

print("")

##### STRINGHE #####
# Nello specifico, le stringhe in Python (UTF-8) sono immutabiili ma possono avere queste operazioni

c = 'ciao'
d = 'mondo'
print(f"Stringhe c = {c} e d = {d}")
# Funzioni possibili sulle stringhe sono
print("\tc.lower(): ", c.lower())
print("\td.upper(): ", d.upper())
print("\tc.count('o'): ", c.count('o'))
print("\td.find('d'): ", d.find('d'))
print("\tc.replece('ciao','miao'): ", c.replace('ciao','miao'))
print("\tJOIN -> ';'.join(['1','2','3']) = ",';'.join(['1','2','3']))
print("\tSPLIT -> 1+2+3+4+5'.split('+') = ", '1+2+3+4+5'.split('+'))

print("\n\n")

##### LISTE #####
# Nello specifico, le liste in Python possono avere queste operazioni

##### TUPLE #####
# Nello specifico, le tuple in Python sono immutabiili ma possono avere queste operazioni

##### SET #####

##### DICTIONARY #####
