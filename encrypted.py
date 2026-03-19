from arc9.engine import ARC9

def encrypted():
    secret_key = "you_key"
    engine = ARC9(secret_key)
    text = "you_text"
    encrypted_data = engine.process(text)
    print(f"Encrypted: {encrypted_data}")
    decoder = ARC9(secret_key)

if __name__ == "__main__":
    encrypted()