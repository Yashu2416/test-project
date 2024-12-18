from Crypto.Cipher import AES
from Crypto.Util.Padding import pad, unpad
import base64
import os
from cryptography.fernet import Fernet
from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.kdf.hkdf import HKDF


# password = b"passwordpassword"
# hkdf = HKDF(
# algorithm=hashes.SHA256(),  # You can swap this out for hashes.MD5()
# length=32,
# salt=None,    # You may be able to remove this line but I'm unable to test
# info=None,    # You may also be able to remove this line
# backend=default_backend()
# )
# key = base64.urlsafe_b64encode(hkdf.derive(password))
# f = Fernet(key)
# token = f.encrypt(b"Secret message!")
# token
# b'...'
# f.decrypt(token)  # Process the key in the exact same manner to decode an encoded message
# b'Secret message!'


# SECRET_KEY = b'yashwantdevanshvedpalme'  # Must be 16, 24, or 32 bytes long

# def encrypt(data):
#     cipher = AES.new(SECRET_KEY, AES.MODE_CBC)
#     ct_bytes = cipher.encrypt(pad(data.encode(), AES.block_size))
#     iv = base64.b64encode(cipher.iv).decode('utf-8')
#     ct = base64.b64encode(ct_bytes).decode('utf-8')
#     return iv + ct

# def decrypt(enc_data):
#     iv = base64.b64decode(enc_data[:24])
#     ct = base64.b64decode(enc_data[24:])
#     cipher = AES.new(SECRET_KEY, AES.MODE_CBC, iv)
#     pt = unpad(cipher.decrypt(ct), AES.block_size)
#     return pt.decode('utf-8')

from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives import padding
import os

# Generate a key and IV (Initialization Vector)
key = os.urandom(32)  # AES-256 key (32 bytes)
iv = os.urandom(16)   # 16 bytes for AES block size

# Encrypt data
def encrypt_data(plaintext):
    # Pad plaintext to block size (AES block size is 16 bytes)
    padder = padding.PKCS7(128).padder()
    padded_data = padder.update(plaintext.encode()) + padder.finalize()

    cipher = Cipher(algorithms.AES(key), modes.CBC(iv), backend=default_backend())
    encryptor = cipher.encryptor()
    encrypted_data = encryptor.update(padded_data) + encryptor.finalize()
    return encrypted_data

# Decrypt data
def decrypt_data(encrypted_data):
    cipher = Cipher(algorithms.AES(key), modes.CBC(iv), backend=default_backend())
    decryptor = cipher.decryptor()
    decrypted_padded_data = decryptor.update(encrypted_data) + decryptor.finalize()

    # Unpad the decrypted data
    unpadder = padding.PKCS7(128).unpadder()
    decrypted_data = unpadder.update(decrypted_padded_data) + unpadder.finalize()
    return decrypted_data.decode()
