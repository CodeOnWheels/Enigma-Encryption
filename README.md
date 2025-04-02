# Encryption and Decryption Script

## Overview

This script provides functionality to encrypt and decrypt strings using a simple character substitution algorithm. It adds random noise to the string before encryption and removes it during decryption using predefined delimiters.

## Features

- Encrypts a given string by shifting characters based on an incrementing wheel mechanism.
- Decrypts a string by reversing the shifting process.
- Supports multiple layers of encryption and decryption through recursive stacking.
- Includes a debugging and testing function.

## Code

```python
import random

# Alpha numeric list used for character substitution
alphaNumericList = [' ', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z',
                    'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z',
                    '!', '"', '#', '$', '%', '&', "'", '(', ')', '*', '+', ',', '-', '.', '/', ':', ';', '<', '=', '>', '?', '@', '[', '\\', ']', '^', '_', '`', '{', '|', '}', '~',
                    '0', '1', '2', '3', '4', '5', '6', '7', '8', '9']

# Encrypt function
def encrypt(string, initWheel=1, initIncrement=1):
    inString = ""
    
    # Add random noise
    for _ in range(random.randint(1, random.randint(1, 100))):
        inString += random.choice(alphaNumericList)
    
    # Insert delimiter
    inString += "###" + string + "###"
    
    # Add more random noise
    for _ in range(random.randint(1, random.randint(1, 100))):
        inString += random.choice(alphaNumericList)
    
    wheel = initWheel
    incrementer = initIncrement
    retVal = ""
    
    for char in inString:
        wheel += incrementer
        incrementer += 2
        if char in alphaNumericList:
            retVal += alphaNumericList[(alphaNumericList.index(char) + wheel) % len(alphaNumericList)]
        else:
            retVal += char
    
    return retVal

# Decrypt function
def decrypt(string, initWheel=1, initIncrement=1):
    wheel = initWheel
    incrementer = initIncrement
    retVal = ""
    
    for char in string:
        wheel += incrementer
        incrementer += 2
        if char in alphaNumericList:
            retVal += alphaNumericList[(alphaNumericList.index(char) - wheel) % len(alphaNumericList)]
        else:
            retVal += char
    
    return retVal.split("###")[1]

# Recursive encryption
def stackEncrypt(string, iterations, initWheel=1, initIncrement=1):
    for _ in range(iterations):
        string = encrypt(string, initWheel, initIncrement)
    return string

# Recursive decryption
def stackDecrypt(string, iterations, initWheel=1, initIncrement=1):
    for _ in range(iterations):
        string = decrypt(string, initWheel, initIncrement)
    return string

# Testing function
def runTests(string, initWheel=1, initIncrement=1):
    testString = string
    print("Initial:   " + testString)
    
    testString = stackEncrypt(testString, 1)
    print("Encrypted: " + testString)
    
    testString = stackDecrypt(testString, 1)
    print("Decrypted: " + testString + "\n")

runTests("Hello")
```
# Usage
Call encrypt(your_string) to encrypt a string.

Call decrypt(encrypted_string) to decrypt it back.

Use stackEncrypt(your_string, iterations) to apply encryption multiple times.

Use stackDecrypt(encrypted_string, iterations) to reverse the stacking process.

The runTests function demonstrates the encryption-decryption cycle with a sample string.

Notes
The algorithm introduces randomness, which increases the security of the encryption.

The decryption process effectively removes the added randomness by extracting the actual message using predefined delimiters.
