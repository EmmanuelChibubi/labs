import string

def generate_substitution_key():
    # Example substitution key; you can customize this
    alphabet = string.ascii_uppercase
    substitution_key = "QWERTYUIOPLKJHGFDSAZXCVBNM"  # This should be a permutation of alphabet
    return dict(zip(alphabet, substitution_key))

def encrypt_message(message, key):
    encrypted_message = []
    for char in message.upper():
        if char in key:
            encrypted_message.append(key[char])
        else:
            encrypted_message.append(char)  # Non-alphabet characters are added as-is
    return ''.join(encrypted_message)

def decrypt_message(encrypted_message, key):
    # Reverse the substitution key to map encrypted letters back to original ones
    reversed_key = {v: k for k, v in key.items()}
    decrypted_message = []
    for char in encrypted_message:
        if char in reversed_key:
            decrypted_message.append(reversed_key[char])
        else:
            decrypted_message.append(char)  # Non-alphabet characters are added as-is
    return ''.join(decrypted_message)

# Example usage
key = generate_substitution_key()

original_message = "HELLO WORLD"
encrypted_message = encrypt_message(original_message, key)
decrypted_message = decrypt_message(encrypted_message, key)

print("Original Message:", original_message)
print("Encrypted Message:", encrypted_message)
print("Decrypted Message:", decrypted_message)
