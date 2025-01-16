import argparse

def interactive_menu():
    print("Benvenuto nel menu interattivo!")
    try:
        num1 = float(input("Inserisci il primo numero: "))
        num2 = float(input("Inserisci il secondo numero: "))
        result = num1 + num2
        print(f"La somma di {num1} e {num2} è {result}")
    except ValueError:
        print("Errore: Per favore, inserisci solo numeri validi.")

def main():
    # Creazione dell'oggetto ArgumentParser
    parser = argparse.ArgumentParser(description="Calcola la somma di due numeri.")
    parser.add_argument('num1', type=int, nargs='?', help="Il primo numero")
    parser.add_argument('num2', type=int, nargs='?', help="Il secondo numero")
    
    # Parsing degli argomenti
    args = parser.parse_args()

    # Controllo degli argomenti
    if args.num1 is None or args.num2 is None:
        # Se mancano gli argomenti, avvia il menu interattivo
        interactive_menu()
    else:
        # Calcolo della somma quando gli argomenti sono forniti
        result = args.num1 + args.num2
        print(f"La somma di {args.num1} e {args.num2} è {result}")

if __name__ == "__main__":
    main()
