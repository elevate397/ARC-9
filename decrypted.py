from arc9.engine import ARC9

def decryptrun():
    secret_key = "you_key"
    decoder = ARC9(secret_key)
    packet = "you_encryptedtext"
    try:
        decrypted_text = decoder.process(packet, decrypt=True)
        print(f"Decrypted: {decrypted_text}")
    except Exception as error:
        print(f"error: {error}")

if __name__ == "__main__":
    decryptrun()