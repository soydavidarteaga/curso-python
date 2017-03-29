from tinyintError import tiny_int



def call_back_function():
	print("Esto se ejecuta cuando hay un error")
print(tiny_int(50 , call_back_function))
