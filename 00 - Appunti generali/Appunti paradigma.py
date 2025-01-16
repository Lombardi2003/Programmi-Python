from functools import *

l = [i for i in range (100)]

f = map(lambda x: x**2,filter(lambda x: x%2==0,l))


print(f)
print(list(f))

def somma(x,y):
    return x+y
sommapartial = partial(somma, y=10)


from functools import *
#@total_ordering #ci è andato a ridefinire tutti i metodi che non abbiamo
class Pippo():
    def __init__():
        pass


@lru_cache      # si può dare un maxsize =3 o quando si preferisce @lru_cache(maxsize=10) 
def somma(x,y):
    print('somma è stata chiamata!')
    return x+y

somma(1,2)
somma(1,2)
somma(1,2)
somma(1,2)