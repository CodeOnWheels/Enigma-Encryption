"""Educational character-shift demo; not suitable for protecting sensitive data."""

import random

# Alpha numeric list I am using to iterate through the alphabet
alphaNumericList = [' ', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z',
                    'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z',
                    '!', '"', '#', '$', '%', '&', "'", '(', ')', '*', '+', ',', '-', '.', '/', ':', ';', '<', '=', '>', '?', '@', '[', '\\', ']', '^', '_', '`', '{', '|', '}', '~',
                    '0', '1', '2', '3', '4', '5', '6', '7', '8', '9']

# Padding cannot contain the frame marker or merge with its boundaries.
noiseAlphabet = [char for char in alphaNumericList if char != '#']

# Encrypt and Decrypt
def encrypt(string, initWheel = 1, initIncrement = 1):
  inString = ""

  # Inserting the randomness
  for i in range(random.randint(1, random.randint(1, 100))):
    inString += random.choice(noiseAlphabet)

  # Inserting delimiter
  inString += "###" + string + "###"

  # Inserting the randomness
  for i in range(random.randint(1, random.randint(1, 100))):
    inString += random.choice(noiseAlphabet)

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
  start = retVal.find("###")
  end = retVal.rfind("###")
  if start == -1 or end < start + 3:
    raise ValueError("Ciphertext does not contain a complete message frame")
  return retVal[start + 3:end]

# Recursive encryption and decryption
def stackEncrypt(string, iterations, initWheel = 1, initIncrement = 1):
  if not isinstance(iterations, int) or isinstance(iterations, bool) or iterations < 0:
    raise ValueError("iterations must be a non-negative integer")
  for i in range(iterations):
    string = encrypt(string, initWheel, initIncrement)
  return string

def stackDecrypt(string, iterations, initWheel = 1, initIncrement = 1):
  if not isinstance(iterations, int) or isinstance(iterations, bool) or iterations < 0:
    raise ValueError("iterations must be a non-negative integer")
  for i in range(iterations):
    string = decrypt(string, initWheel, initIncrement)
  return string

# Debugging and Testing
def runTests(string, initWheel = 1, initIncrement = 1):
  testString = string

  print("Initial:   "  + testString)

  testString = stackEncrypt(testString, 1, initWheel, initIncrement)
  print("Encrypted: " + testString)

  testString = stackDecrypt(testString, 1, initWheel, initIncrement)
  print("Decrypted: " + testString + "\n")

if __name__ == "__main__":
  runTests("Hello, robotics!")

