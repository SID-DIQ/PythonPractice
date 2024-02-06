"""
	Exception Handling in python

		exception is ocuured in run time.
		in python the try block it is used to find the exception (except)
		try block have an else part the else part print the statement if no exception ocurred
		finally keyword
		the finally key word is used to print all the time if exception ocurred it will print of exception not it also print


"""
try:
    a=10/0
except Exception as e:
    print(e)
else:
    print(a)
finally:
    print("finished")


print(len(dir(locals()['__builtins__'])))