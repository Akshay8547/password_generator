import random
uppercase = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
lowercase = uppercase.lower()
numbers = "0123456789"
symbols = "!@#$&*(){}[]?/\\_-+="
password = uppercase + lowercase + numbers + symbols
length = 15
newpassword = "".join(random.sample(password, length))
print("The new password generated is : ",newpassword)
