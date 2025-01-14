def fun(arg1):
	def fun1():
		print('Ciao ',arg1)
	return fun1

a = fun('mondo')

a()