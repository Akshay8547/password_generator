# password_generator
A Python based project for generating strong, random passwords which enhance security
### installing
   pip install random
# Usage
###importing the random library
import random

###creating a set of letters, numbers and symbols to generate a password
uppercase = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
lowercase = uppercase.lower()
numbers = "0123456789"
symbols = "!@#$&*(){}[]?/\\_-+="

###creating a variable to store the password
password = uppercase + lowercase + numbers + symbols
length = 15

###generating the password
newpassword = "".join(random.sample(password, length))
print("The new password generated is : ",newpassword)
