# Descrittori sono oggetti che ci permettono di avere dei determinati metodi
# -> metodo di get
# -> metodo di set
# -> metodo di delete

class Desc:
    def __init__(self, fget):
        print('Sono stato creato!!')
        self.fget = fget        # ingresso della funzione
    def __get__(self, istance, owner):      
        return self.fget(istance)   # princio è che il descrittore incapsula un oggetto, quell'oggetto usa una funzione di get, noi stiamo facendo 
    
class C:
    def __init__(self):
        self.__a = 0
    @Desc       # equivalente a Desc(a) ---> C.a <---> Desc(a) ----> c.a                        # quando si va a chiamare a è il descrittore che contiene a
    def a(self):
        return self.__a
    
c = C()
print(c.a)

# quando si va a creare l'oggetto, la funzione a esso associato, quando si va a creare la classe C, quando vede la desc fa il mapping in modo che viene passato direttamente 
# a desc

# la @propriety esiste già ed è un descrittore

# con la @propriety che già esiste si possono usare per i semplici get e set, ma si va a creare un descrittore per avere le cose più interessanti e più particolari

# tutto ciò funziona solo se i descrittore (cosa vera) hanno la priorità sul __dict__
