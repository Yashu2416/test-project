import base64
from Crypto.Cipher import AES
from Crypto.Util.Padding import pad
from rest_framework.renderers import BaseRenderer
import json
import os

AES_IV="PBKDF2WithHmacSHA2"
AES_SECRET_KEYS_="PBKDF2WithHmacSHA1"

# here the string gotten from the environmental variable is converted to bytes
AES_SECRET_KEYS_ = bytes(('AES_SECRET_KEYS_'), 'utf-8')
AES_IV = bytes(('AES___________IV'), 'utf-8')

class CustomAesRenderer(BaseRenderer):
    media_type = 'application/octet-stream'
    format = 'aes'

    def render(self, data, media_type=None, renderer_context=None):
        plaintext = json.dumps(data)
        padded_plaintext = pad(plaintext.encode(), 16)
        cipher = AES.new(AES_SECRET_KEYS_, AES.MODE_CBC, AES_IV)
        ciphertext = cipher.encrypt(padded_plaintext)
        ciphertext_b64 = base64.b64encode(ciphertext).decode()
        response = {'ciphertext': ciphertext_b64}
        return json.dumps(response)