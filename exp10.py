# Write a program Implementation of Hill cipher 

import numpy as np

# Function to get the modular inverse of a matrix
def mod_inverse(matrix, modulus):
    det = int(np.round(np.linalg.det(matrix)))  # Determinant of the matrix
    det_inv = pow(det, -1, modulus)  # Modular inverse of the determinant

    # Adjugate matrix (cofactor matrix transposed) mod 26
    matrix_mod_inv = (
        det_inv * np.round(det * np.linalg.inv(matrix)).astype(int) % modulus
    )
    return matrix_mod_inv % modulus

# Function to encrypt a plaintext using the Hill cipher
def hill_encrypt(plaintext, key_matrix):
    modulus = 26
    plaintext = plaintext.upper().replace(" ", "")
    
    # Ensure plaintext length is a multiple of matrix size
    while len(plaintext) % 2 != 0:
        plaintext += "X"  # Pad with 'X' if necessary
    
    ciphertext = ""
    for i in range(0, len(plaintext), 2):
        block = np.array([ord(plaintext[i]) - ord("A"), ord(plaintext[i + 1]) - ord("A")])
        encrypted_block = np.dot(key_matrix, block) % modulus
        ciphertext += chr(encrypted_block[0] + ord("A"))
        ciphertext += chr(encrypted_block[1] + ord("A"))
    
    return ciphertext

# Function to decrypt a ciphertext using the Hill cipher
def hill_decrypt(ciphertext, key_matrix):
    modulus = 26
    inverse_key_matrix = mod_inverse(key_matrix, modulus)
    plaintext = ""
    
    for i in range(0, len(ciphertext), 2):
        block = np.array([ord(ciphertext[i]) - ord("A"), ord(ciphertext[i + 1]) - ord("A")])
        decrypted_block = np.dot(inverse_key_matrix, block) % modulus
        plaintext += chr(int(decrypted_block[0]) + ord("A"))
        plaintext += chr(int(decrypted_block[1]) + ord("A"))
    
    return plaintext

# Main program
if __name__ == "__main__":
    # Example 2x2 key matrix (must be invertible mod 26)
    key_matrix = np.array([[3, 3], [2, 5]])
    
    # Example plaintext
    plaintext = "HELLO"
    print("Plaintext:", plaintext)
    
    # Encrypt the plaintext
    ciphertext = hill_encrypt(plaintext, key_matrix)
    print("Ciphertext:", ciphertext)
    
    # Decrypt the ciphertext
    decrypted_text = hill_decrypt(ciphertext, key_matrix)
    print("Decrypted Text:", decrypted_text)
