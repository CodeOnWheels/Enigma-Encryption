import random

# Alpha numeric list I am using to iterate through the alphabet
alphaNumericList = [' ', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z',
                    'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z',
                    '!', '"', '#', '$', '%', '&', "'", '(', ')', '*', '+', ',', '-', '.', '/', ':', ';', '<', '=', '>', '?', '@', '[', '\\', ']', '^', '_', '`', '{', '|', '}', '~',
                    '0', '1', '2', '3', '4', '5', '6', '7', '8', '9']

# Encrypt and Decrypt
def encrypt(string, initWheel = 1, initIncrement = 1):
  inString = ""

  # Inserting the randomness
  for i in range(random.randint(1, random.randint(1, 100))):
    inString += random.choice(alphaNumericList)

  # Inserting delimiter
  inString += "###" + string + "###"

  # Inserting the randomness
  for i in range(random.randint(1, random.randint(1, 100))):
    inString += random.choice(alphaNumericList)

  # Actual encryption
  wheel = initWheel
  incrementer = initIncrement
  retVal = ""

  for char in inString:
    wheel += incrementer
    incrementer += 2

    if (char in alphaNumericList):
      retVal += alphaNumericList[(alphaNumericList.index(char) + wheel) % len(alphaNumericList)]
    else:
      retVal += char

  return retVal

def decrypt(string, initWheel = 1, initIncrement = 1):
  wheel = initWheel
  incrementer = initIncrement
  retVal = ""

  for char in string:
    wheel += incrementer
    incrementer += 2

    if (char in alphaNumericList):
      retVal += alphaNumericList[(alphaNumericList.index(char) - wheel) % len(alphaNumericList)]
    else:
      retVal += char

  # Delimiter
  return retVal.split("###")[1]

# Recursive encryption and decryption
def stackEncrypt(string, iterations, initWheel = 1, initIncrement = 1):
  for i in range(iterations):
    string = encrypt(string, initWheel, initIncrement)
  return string

def stackDecrypt(string, iterations, initWheel = 1, initIncrement = 1):
  for i in range(iterations):
    string = decrypt(string, initWheel, initIncrement)
  return string

# Debugging and Testing
def runTests(string, initWheel = 1, initIncrement = 1):
  testString = string
  initWheel = initWheel
  initIncrement = initIncrement

  print("Initial:   "  + testString)

  testString = stackEncrypt(testString, 1)
  print("Encrypted: " + testString)

  testString = stackDecrypt(testString, 1)
  print("Decrypted: " + testString + "\n")

runTests(" ")
