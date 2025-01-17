import os
from cryptography.fernet import Fernet

class WinEncrypt:
    def __init__(self, key_file='secret.key'):
        self.key_file = key_file
        self.key = self.load_key()

    def generate_key(self):
        """
        Generates a new encryption key and saves it to a file.
        """
        key = Fernet.generate_key()
        with open(self.key_file, 'wb') as key_file:
            key_file.write(key)
        print("Encryption key generated and saved to", self.key_file)

    def load_key(self):
        """
        Loads the encryption key from a file.
        """
        if not os.path.exists(self.key_file):
            self.generate_key()
        with open(self.key_file, 'rb') as key_file:
            key = key_file.read()
        return key

    def encrypt_file(self, file_path):
        """
        Encrypts a file and saves the encrypted data back to the same file.
        """
        with open(file_path, 'rb') as file:
            data = file.read()
        fernet = Fernet(self.key)
        encrypted = fernet.encrypt(data)
        with open(file_path, 'wb') as file:
            file.write(encrypted)
        print(f"File '{file_path}' encrypted successfully.")

    def decrypt_file(self, file_path):
        """
        Decrypts an encrypted file and saves the decrypted data back to the same file.
        """
        with open(file_path, 'rb') as file:
            encrypted_data = file.read()
        fernet = Fernet(self.key)
        decrypted = fernet.decrypt(encrypted_data)
        with open(file_path, 'wb') as file:
            file.write(decrypted)
        print(f"File '{file_path}' decrypted successfully.")

if __name__ == "__main__":
    import argparse

    parser = argparse.ArgumentParser(description="WinEncrypt - Simple File Encryption/Decryption")
    parser.add_argument('action', choices=['encrypt', 'decrypt'], help="Action to perform: 'encrypt' or 'decrypt'")
    parser.add_argument('file', help="The file to encrypt or decrypt")
    parser.add_argument('--key-file', help="Path to the encryption key file", default='secret.key')

    args = parser.parse_args()

    encryptor = WinEncrypt(key_file=args.key_file)

    if args.action == 'encrypt':
        encryptor.encrypt_file(args.file)
    elif args.action == 'decrypt':
        encryptor.decrypt_file(args.file)