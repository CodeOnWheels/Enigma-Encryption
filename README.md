# Enigma-inspired character-shift demo

A Python learning project that transforms text using changing character offsets, randomized padding, and repeated encryption/decryption passes.

This is a custom substitution exercise, not a simulation of the historical Enigma machine or secure cryptography. Random padding and additional passes do not make it suitable for protecting passwords or other sensitive data.

## Run

Requires Python 3 and only the standard library:

```sh
git clone https://github.com/CodeOnWheels/Enigma-Encryption.git
cd Enigma-Encryption
python enigmaEncrypter.py
```

## Use as a module

```python
from enigmaEncrypter import stackEncrypt, stackDecrypt

message = "Hello ### robotics! 中文"
ciphertext = stackEncrypt(message, 3, initWheel=7, initIncrement=2)
restored = stackDecrypt(ciphertext, 3, initWheel=7, initIncrement=2)
assert restored == message
```

Use the same wheel, increment, and number of passes to reverse the transformation. Zero passes returns the original string. Negative or non-integer pass counts raise `ValueError`.

## How it works

`encrypt` adds random padding around a `###`-framed message, then shifts characters through a fixed alphabet. The wheel offset changes with each character. Characters outside that alphabet pass through unchanged. `decrypt` reverses those shifts and extracts the frame.

Padding excludes `#` so it cannot create false frame boundaries. Extraction uses the outer frame to preserve `###` inside messages, including repeated transformations. Importing the module does not run the example.

Malformed frames raise `ValueError`. This is not authentication: wrong parameters or modified text are not reliably detected. Older ciphertext whose random padding contained ambiguous hash sequences may not be recoverable.

## Tests

```sh
python -m unittest discover -s tests -v
```

Tests cover delimiter-containing messages, Unicode, stacked transformations, custom wheel settings, malformed frames, and import behavior.

