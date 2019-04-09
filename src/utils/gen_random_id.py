import random, string

def generateRandomId():
  lettersAndDigits = string.ascii_letters + string.digits
  return ''.join(random.choice(lettersAndDigits) for i in range(10))
