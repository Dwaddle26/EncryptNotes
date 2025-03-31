import hashlib
import base64
from cryptography.fernet import Fernet
from django.conf import settings

#for encrypting user key, use Django secret key for now
def convert_DJ_key():
    hash_key = hashlib.sha256(settings.SECRET_KEY.encode()).digest()
    return Fernet(base64.urlsafe_b64encode(hash_key[:32]))
    
def encrypt_user_key(ukey):
    f = convert_DJ_key()
    return f.encrypt(ukey.encode())
    
def decrypt_user_key(ukey):
    f = convert_DJ_key()
    return f.decrypt(ukey.decode())
    
#user encryption keys

#Generates a new user encryption key with Fernet
#Returns: new encryption key
def generate_user_key():
    return Fernet.generate_key()

#Encrypts data with Fernet
#key: the encryption
#info: the info to encrypt
#Returns: encrypted data
def encrypt_data(key, info):
    fernet = Fernet(key)
    return fernet.encrypt(info.encode())

#Decrypts data with Fernet
#key: the encryption key
#info: the info the decrypt
#Returns: decrypted data
def decrypt_data(key, info):
    fernet = Fernet(key)
    return fernet.decrypt(info).decode()