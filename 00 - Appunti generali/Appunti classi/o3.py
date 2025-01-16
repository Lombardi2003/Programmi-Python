# Python ci permette di istanziare classi per istanziare classi (metaclassi) -> super classe di chiunque è type (per gli oggeti è object)

# l'obbiettivo di type è che restituisce di che tipo di classe è un oggetto -> type(x) = classe Y
# type('nome_classe_da_creare',(nome_classe_padre),dict(attributi))



class MetaC(type):
    def __new__(cls, classname, bases, classdict):              # classe, nome della classe, genitori, dizionario
        def new_method(self):
            print('hi')
        classdict['my_method'] = new_method                     # così quando si userà questa classe per creare altre classi generate tra questa avranno il metodo di classe my_method
        classdict['myAttr'] = 10 
        return super().__new__(cls,classname, bases, classdict)
    
class C(metaclass=MetaC):
    def __call__(self, *args, **kwargs):
        print('hi')


c = C()
c()



#m_c = MetaC() # equivalente a class X():pass
#print(m_c)

# metodo __call__ 