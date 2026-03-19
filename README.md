# 🧬 ARC-9 DNA Mutagen

**ARC-9** is a unique, high-security encryption protocol based on **Cellular Automata** and **DNA Mutation** logic. Unlike standard AES, it uses a self-mutating engine where every byte depends on the entire history of the message.

## ✨ Key Features
- **Zero Dependencies:** Pure Python, no external libraries required.
- **DNA Mutation Engine:** Bytes evolve during encryption, making patterns impossible to find.
- **Custom ARC-HEX:** Uses a unique 16-symbol alphabet (`0123456789AZ@#$!`) instead of standard HEX.
- **Built-in Salting:** Every encryption produces a unique result, even with the same password.

## ⭐ Quick Start
**Encrypted script**
from arc9 import ARC9

# Initialize with your secret key
cipher = ARC9("your-secret-password")

# Encrypt a message
encrypted = cipher.process("Hello, World!")
print(f"Encrypted packet: {encrypted}")
# Result will look like: !A7Z98@2#...

**decrypted script**
from arc9 import ARC9

# To decrypt, create a NEW object with the same key to reset the mutation state
decoder = ARC9("your-secret-password")

packet = "!A7Z98@2#..." # Use the packet from the example above
decrypted = decoder.process(packet, decrypt=True)

print(f"Decrypted text: {decrypted}")

## 🚀 Installation
```bash
pip install arc-9