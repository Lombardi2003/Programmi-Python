# Inizializzazione del dizionario come un dizionario vuoto
dict = {}
# Definizione della varabile che serve ad uscire dal ciclo
a = 'si'

# Ciclo per l'inserimento della chiave e del valore dentro al dizionario
while a=='si' :
    print(' ')
    nome = input('Inserisci la chiave: ')
    numero = input('Inserisci il valore: ')
    dict[nome] = numero
    a=input("Vuoi continuare ad inserire valori (si o no)??? ")

# Stampa dei tutti i valori del dizionario
print("\nStampa del dizionario:\n")
for i in dict.items() :
    print('Chiave: ',i[0],'\tNumero:', i[1])
    print(" ")