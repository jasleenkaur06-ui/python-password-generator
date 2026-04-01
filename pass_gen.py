import string
import random       
print("Welcome to the password generator!")
length = int(input("Enter the desired length of your password: "))    
characters = string.ascii_letters + string.digits + string.punctuation
password = ''.join(random.choice(characters) for i in range(length))
print("Your generated password is: " + password)
