import random
import string

#determines length of your password
length = int(input("Enter password length: "))

#adds upper-,lowercase letters and digits
chars = string.ascii_letters
chars += string.digits

password = ""
print("Should your password include punctuation?\n Its more secure to include it\n Press 1 to include it or 2 to not include it")
passwordStrength = int(input("Enter 1 or 2: "))
if(passwordStrength == 1):
    #adds punctuation to char string
    chars += string.punctuation
    #generates password 
    for i in range(length):
        next_character = random.choice(chars)
        password += next_character
elif(passwordStrength == 2):
    #generates password without punctuation
    for i in range(length):
        next_character = random.choice(chars)
        password += next_character
else:
    print("Not a valid input.")

print("Your random Password is:", password)