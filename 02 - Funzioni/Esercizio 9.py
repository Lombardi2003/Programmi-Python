# Scrivere un decoratore che arricchisca una funzione come segue:
#   1) Oltre a ritornare il risultato della funzione stessa, lo stampa anche a video.
#   2) Prima di eseguire chiede all’utente se vuole modificare il parametro in
#      ingresso (opzione non possibile se vi sono più parametri)

def modifica_parametro_e_stampa(function):
    def wrapper(*args, **kwargs):
        risposta = input(f"Vuoi modificare il parametro '{args[0]}'? (s/n): ").strip().lower()
        while risposta == 's':
            # Per controllare se viene sollevata una eccezione, se viene immesso un carattere
            try:
                nuovo_parametro = int(input("Inserisci il nuovo valore: "))
            except Exception:
                print(f"Il nuovo valore '{nuovo_parametro}' non è un numero, inserire un numero per il corretto funzionamento del programma.")
                nuovo_parametro = input("Inserisci il nuovo valore: ")
            args = (nuovo_parametro,)
            risposta = input(f"Vuoi modificare il parametro '{args[0]}'? (s/n): ").strip().lower()
        # Esegue la funzione con i (forse) nuovi parametri
        risultato = function(*args, **kwargs)
        # Stampa e ritorna il risultato
        print(f"Risultato: {risultato}")
        return risultato

    return wrapper

# Utilizzo del decoratore
@modifica_parametro_e_stampa
def raddoppia(numero):
    return numero * 2

while True:
    try :
        x = int(input("Inserisci un valore:"))
        break
    except Exception:
        print("Il valore non è un numero, inserire un numero per il corretto funzionamento del programma.")
raddoppia(x)