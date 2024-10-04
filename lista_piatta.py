# Provare usando la ricorsione a scrivere una funzione che appiattisca una lista di liste
# 
# Aiutarsi con la funzione hasattr. Cercare nella documentazione

def lista_piatta(args) :
    res = []
    if not hasattr(args,'__iter__') :
        return [args]
    for o in args:
        res.extend(lista_piatta(o))
    return res

lista = [[1,2,3],[4,5,6]]
lp = lista_piatta(lista)
print(*lp)