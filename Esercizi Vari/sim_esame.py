a = [1, 2]
def fun(x):
    x.append(3)
    x = [4, 5]
fun(a)
print(a)