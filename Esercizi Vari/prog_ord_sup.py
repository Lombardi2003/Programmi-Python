def fun():
	def fun1(arg1):
		print('Ciao ',arg1)
	return fun1

a = fun()

a('mondo')