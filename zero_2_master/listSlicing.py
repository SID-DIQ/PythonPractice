#list sicing and copy
swiggy_cart = ['curd rice',
               'lemon rice',
               'tomato rice',
               'ghee ricd']
print(swiggy_cart) #it will print the actual swiggy_cart

changed_cart = swiggy_cart
swiggy_cart[1] = 'biriyani'
print(changed_cart) #it will print the changed swiggy_cart

print(swiggy_cart) #it will print the actual swiggy_cart

#copy method 
changed_cart = swiggy_cart[:]
print(changed_cart) #it will print the changed swiggy_cart
print(swiggy_cart) #it will print the actual swiggy_cart