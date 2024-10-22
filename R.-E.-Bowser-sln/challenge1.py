from Crypto.Cipher import ChaCha20
import os

def int_to_bytes(n, length):
    return n.to_bytes(length, byteorder='big')

def decrypt_message(encrypted_msg, key):
    # Extract the nonce from the beginning
    nonce = encrypted_msg[:8]  
    # The rest is the ciphertext
    ciphertext = encrypted_msg[8:]  
    cipher = ChaCha20.new(key=key, nonce=nonce)
    # Handle decoding errors
    return cipher.decrypt(ciphertext).decode('utf-8', errors='ignore')  

with open('encrypted.txt', 'rb') as em:
    # Read the entire file content
    encrypted_data = em.read()  

# Output file to store all decrypted messages
output_file = 'all_decrypted_messages.txt'

# Number of keys to try
num_keys_to_try = 2**32

with open(output_file, 'w', encoding='utf-8') as df:
    for i in range(num_keys_to_try):
        # Convert integer to 32-byte key
        key = int_to_bytes(i, 32)  
        decrypted_message = decrypt_message(encrypted_data, key)
        df.write(f'Decrypted message with key {i}:\n{decrypted_message}\n\n')
        print(f'Decrypted message with key {i} appended to {output_file}')