import argparse
def fun(x=0):
    print("Valore",x)

def main():
    parser = argparse.ArgumentParser(description="Esporta un progetto specificato in un file di output.")
    # Aggiunta degli argomenti
    parser.add_argument("x", type=str, help="X")
    # Parsing degli argomenti
    args = parser.parse_args()
    # Esegui la funzione di esportazione
    fun(args.x)

if __name__ == "__main__":
    main()