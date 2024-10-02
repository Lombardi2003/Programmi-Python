# Scrivere un programma che simuli una rubrica telefonica
# 
# L'utente deve poter scegliere se inserire un numero, cancellarlo o stampare l'intera rubrica
# 
# La struttura della rubrica è molto semplice ongi contatto ha un nome e un numero

rubrica = {}

while 1 :
    a = input("Inserisci:\n\t1: Inserire un numero \n\t2: Cancellare un numero\n\t3: Stampare l'intera rubrica\n\nPer uscire inserire qualunque altro numero\n\nNumero scelto: ")
    if a=='1' :
        print(" ")
        rubrica[input('Inserisci il numero: ')]=input('Inserisci il nome: ')
        print(" ")
    elif a=='2' :
        print(" ")
        del rubrica[input('Inserisci il numero da eliminare: ')]
        print(" ")
    elif a=='3' :
        print("\nStampa della rubrica:\n")
        for t in rubrica.items() :
            print(f'Nome: {t[1]} Numero: {t[0]}')
        print(" ")
    else :
        break