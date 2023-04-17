import random
import string

email_name = random.randint(1,100)
email_pref = random.randint(1,46)
generatedSuffix = ''.join(random.choice(string.ascii_lowercase + string.digits+string.ascii_uppercase) for _ in range(email_name))+ '@gmail.com'

print (generatedSuffix)
a = 'dsda'
print(type(a))

l = -9
is_minus = l < 0
print(is_minus)