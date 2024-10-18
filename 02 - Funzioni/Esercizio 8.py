# Implementare un decoratore chiamato @log_execution che
#   1) ogni volta che la funzione decorata viene eseguita, scrive su un file di log
#      (es. "execution_log.txt") la data e l'ora di esecuzione, insieme al nome della
#      funzione eseguita e agli argomenti passati.
#   2) Applicare questo decoratore a una funzione che accetta un qualsiasi
#      numero di argomenti e li somma.

import datetime

def log_execution(function):
    def wrapper(*args, **kwargs):
        data_ora_corrente = datetime.datetime.now()
        with open("Execution_log.txt","a+") as file:
            file.write(f"Esecuzione svolta: {data_ora_corrente}.\n")
        print("Scrittura completata")
        return function(*args,**kwargs)
    return wrapper

@log_execution
def somma(*args:int):
    return sum(args)

a = input("Inserisci il numero di addendi dell'operazione: ")
lista = []
for i in range(int(a)):
    lista.append(int(input("Inserisci un numero: ")))
print('La somma degli addenti è ',somma(*lista))