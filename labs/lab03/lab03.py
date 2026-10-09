Alphabet = "абвгдежзийклмнопрстуфхцчшщъыьэюя"

N = len(Alphabet)

def to_number(text):
    return [Alphabet.index(char) +1 for char in text.lower() if char in Alphabet]

def to_text(numbers):
    return "".join([Alphabet[number - 1] for number in numbers])

def gamma_encrypt(text, key):
    plaintext = to_number(text)
    key = to_number(key)
    
    ciphertext = []
    
    for i in range(len(plaintext)):
        key_index = key[i % len(key)]  # gamma repeat if needed
        ciphertext.append((plaintext[i] + key_index -1) % N +1)
    
    return to_text(ciphertext)

def gamma_decrypt(text, key):
    ciphertext = to_number(text)
    key = to_number(key)
    
    plaintext = []
    
    for i in range(len(ciphertext)):
        key_index = key[i % len(key)]  # gamma repeat if needed
        plaintext.append((ciphertext[i] - key_index -1) % N +1)
    return to_text(plaintext)

text = "ПРИКАЗ"
key = "ГАММА"

encrypted = gamma_encrypt(text, key)
print("Encrypted: ", encrypted)

decrypted = gamma_decrypt(encrypted, key)
print("Decrypted: ", decrypted)