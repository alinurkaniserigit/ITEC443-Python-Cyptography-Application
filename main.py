import string
import random
import hashlib
from cryptography.fernet import Fernet

def substitution_encrypt(plaintext, cipher_key):
    # convert the plaintext to lowercase
    plaintext = plaintext.lower()
    # apply the substitution cipher to each letter in the plaintext
    ciphertext = ''.join([cipher_key.get(letter, letter) for letter in plaintext])
    return ciphertext

def substitution_decrypt(ciphertext, cipher_key):
    # invert the substitution cipher to create the decryption key
    decryption_key = {v: k for k, v in cipher_key.items()}
    # apply the decryption key to each letter in the ciphertext
    plaintext = ''.join([decryption_key.get(letter, letter) for letter in ciphertext])
    return plaintext

def caesar_encrypt(plaintext, shift):
    # convert the plaintext to lowercase
    plaintext = plaintext.lower()
    # apply the Caesar cipher to each letter in the plaintext
    ciphertext = ''.join([chr((ord(letter) - ord('a') + shift) % 26 + ord('a')) for letter in plaintext])
    return ciphertext

def caesar_decrypt(ciphertext, shift):
    # invert the Caesar cipher to create the decryption key
    decryption_shift = 26 - shift
    # apply the decryption key to each letter in the ciphertext
    plaintext = ''.join([chr((ord(letter) - ord('a') + decryption_shift) % 26 + ord('a')) for letter in ciphertext])
    return plaintext

def sha256_hash(plaintext):
    # compute the SHA-256 hash of the plaintext
    return hashlib.sha256(plaintext.encode()).hexdigest()

def generate_fernet_key():
    # generate a new Fernet key
    return Fernet.generate_key()

def fernet_encrypt(plaintext, key):
    # create a Fernet cipher with the given key
    cipher = Fernet(key)
    # encrypt the plaintext using the Fernet cipher
    ciphertext = cipher.encrypt(plaintext.encode())
    return ciphertext

def fernet_decrypt(ciphertext, key):
    # create a Fernet cipher with the given key
    cipher = Fernet(key)
    # decrypt the ciphertext using the Fernet cipher
    plaintext = cipher.decrypt(ciphertext).decode()
    return plaintext

# define the substitution cipher alphabet
alphabet = list(string.ascii_lowercase)
random.shuffle(alphabet)
substitution_cipher = dict(zip(string.ascii_lowercase, alphabet))

# display the menu and let the user choose which method to use
while True:
    print("Choose an encryption method:")
    print("1. Substitution cipher")
    print("2. Caesar cipher")
    print("3. SHA-256 hash")
    print("4. Fernet encryption")
    choice = input("Enter your choice (q to quit): ")
    if choice == '1':
        plaintext = input("Enter plaintext to encrypt: ")
        key = input("Enter the substitution cipher key: ")
        cipher_key = dict(zip(string.ascii_lowercase, key))
        ciphertext = substitution_encrypt(plaintext, cipher_key)
        print("Ciphertext:", ciphertext)
        decrypted_plaintext = substitution_decrypt(ciphertext, cipher_key)
        print("Decrypted plaintext:", decrypted_plaintext)
    elif choice == '2':
        plaintext = input("Enter plaintext to encrypt: ")
        shift = int(input("Enter shift amount: "))
        ciphertext = caesar_encrypt(plaintext, shift)
        print("Ciphertext:", ciphertext)
        decrypted_plaintext = caesar_decrypt(ciphertext, shift)
        print("Decrypted plaintext:", decrypted_plaintext)
    elif choice == '3':
      plaintext = input("Enter plaintext to hash: ")
      hash_value = sha256_hash(plaintext)
      print("Hash value:", hash_value)
    elif choice == '4':
        plaintext = input("Enter plaintext to encrypt: ")
        key = input("Enter the Fernet key: ")
        ciphertext = fernet_encrypt(plaintext, key.encode())
        print("Ciphertext:", ciphertext)
        decrypted_plaintext = fernet_decrypt(ciphertext, key.encode())
        print("Decrypted plaintext:", decrypted_plaintext)
