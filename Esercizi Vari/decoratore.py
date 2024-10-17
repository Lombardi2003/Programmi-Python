# Definizione del decoratore - viene passata la funzione a cui verrà associato il decoratore
def saluta_decoratore(funzione):
    def wrapper():
        print("Ciao!")
        funzione()          # Chiamata alla funzione originale -> chiamata alla funzione di_nome
        print("Arrivederci!")
    return wrapper

# Utilizzo del decoratore
@saluta_decoratore
# Definizione della funzione principale
def di_nome():
    print("Mi chiamo Python.")

# Chiamata della funzione decorata
di_nome()           # In realtà -> saluta_decoratore(di_nome)
