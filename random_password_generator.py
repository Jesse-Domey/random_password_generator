import random
import string

# set password length to 10 characters
length = 10

# define the characters of the password
password = ''.join(random.choices(string.ascii_letters + string.digits, k=length))

# output the password
print("Random password of Length", length, ":", password)