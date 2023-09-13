# Get The Input From User

Email = input("Enter Your Email Name :").strip()

# Slice The Username

Username =Email[:Email.index("@")]

# Slice The Domainname

Domainname =Email[Email.index("@") + 1 :]

# Format Message

output = "Your name is {} and Your Domain name {}".format(Username,Domainname)

print(output)