# Scrivere un programma che simuli una rubrica telefonica.
#
# L’utente deve poter scegliere se inserire un numero, cancellarlo o stampare l’intera rubrica.
#
# La struttura della rubrica è molto semplice ogni contatto ha un nome e un numero.

rubrica = {}

while True:
    val = int(input('MENU:\n1: Inserisci un numero\n2: Cancellare un numero\n3: Stampare intera rubrica\n4: Uscire\n\nComando: '))
    if val == 1:
        rubrica[input("Inserisci il numero di telefono: ")] = input("Inserisci il nome della persona del numero: ")
    elif val == 2:
        del rubrica[input("Inserisci il numero di telefono da eliminare: ")]
    elif val == 3:
        for i in rubrica.items():
            print(f'Numero:{i[0]} Nome:{i[1]}')   
    else:
        break