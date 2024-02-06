class students():
    name= 'sid'
    age = 10

"""
 by using getattr meythod we print the object inside the class
 it is have three arameters first one will class name second one be the object name thiird one be the print statement
 """
print(getattr(students,'name'))
print(getattr(students,'age'))
print(getattr(students,'gender','no attribute found'))
print(students)