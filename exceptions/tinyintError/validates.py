def validate_tiny_int(val):
	return val >= 0 and val <= 255
def validate_val(val):
	try:
		return isinstance(int(val),int)
	except ValueError as error:
		return False