username =  input('What is Your Name ?\n')
password = input('Enter Your Password\n')
password_length = len(password)
hidden_password = '*'*password_length
print(f'Hey {username} !, Your Password is {hidden_password}, Your Password Contains {password_length} letters')