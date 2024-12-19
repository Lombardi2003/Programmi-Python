from functools import partial

def mol(a,b):
    return a*b

moltiplipartial = partial(mol, b=5)

# con a non funziona perchè la a viene presa come 20 -> è posizionale

print(moltiplipartial(20))