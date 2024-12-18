from Crypto.Cipher import AES
from Crypto.Util.Padding import pad, unpad
from Crypto.Random import get_random_bytes
import base64
import hashlib

SECRET_KEY = 'base64.urlsafe_b64encode(hkdf.derive(password))'  

def get_key():

    return hashlib.sha256(SECRET_KEY.encode()).digest()

def encrypt_data(data: str) -> str:

    key = get_key()
    cipher = AES.new(key, AES.MODE_CBC)
    
    data_bytes = data.encode('utf-8')
    padded_data = pad(data_bytes, AES.block_size)

    encrypted_data = cipher.encrypt(padded_data)

    encrypted_data_with_iv = cipher.iv + encrypted_data

    return base64.b64encode(encrypted_data_with_iv).decode('utf-8')

def decrypt_data(encrypted_data: str) -> str:

    encrypted_data_bytes = base64.b64decode(encrypted_data)

    iv = encrypted_data_bytes[:16]  
    encrypted_data = encrypted_data_bytes[16:] 

    key = get_key()
    cipher = AES.new(key, AES.MODE_CBC, iv)


    decrypted_data = unpad(cipher.decrypt(encrypted_data), AES.block_size)

    return decrypted_data.decode('utf-8')