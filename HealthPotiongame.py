# Random package for add random number with player health
import random

# Enter The Player Helath
health = int(input("Enter The Player Health : "))

# Enter The Difficulty Level for example 1 == easy 2 == medium 3 == Hard and so on
difficulty = int(input("Enter The Difficulty Level : "))

#random.randit is Package to give the random number between the parantheesis in this case it wii generate the number randomly 25-50
increasedHealth =int(random.randint(25,50) / difficulty)
health =health+increasedHealth
#print(health)
if(health>=75):
    print(str(health) + "The Player is safe..!")
elif 50<= health <75:
    print(str(health) + "The plyer is partially in the safe zone..!")
elif 50>  health >=25:
    print(str(health) + "The player in Danger...")
else:
    print(str(health) + "The player near to the Hell/Hayyat")