import random
import string

total = string.ascii_letters + string.digits + string.punctuation
length = int(input("Enter a length of password: "))
password = "".join(random.choices(total, k=length))  
print("Generated Password: {} ".format{password})
