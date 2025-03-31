import hashlib
import base64
from cryptography.fernet import Fernet
from django.conf import settings

#Converts a DJango secret key into a Fernet usable key
def convert_DJ_key():
    hash_key = hashlib.sha256(settings.SECRET_KEY.encode()).digest()
    return Fernet(base64.urlsafe_b64encode(hash_key[:32]))

# encrypt a user's key with DJango's secret key
#ukey: the user's key
#Returns: encrypted user key
def encrypt_user_key(ukey):
    f = convert_DJ_key()
    return f.encrypt(ukey.encode())

# decrypt a user's key with DJango's secret key
#ukey: the user's key
#Returns: decrypted user key
def decrypt_user_key(ukey):
    f = convert_DJ_key()
    return f.decrypt(ukey.decode())
    
#Generates a new user encryption key with Fernet
#Returns: new encryption key
def generate_user_key():
    return Fernet.generate_key()

#Encrypts data with Fernet
#key: the encryption
#info: the info to encrypt
#Returns: encrypted data
def encrypt_data(key, info):
    f = Fernet(key)
    return f.encrypt(info.encode())

#Decrypts data with Fernet
#key: the encryption key
#info: the info to decrypt
#Returns: decrypted data
def decrypt_data(key, info):
    f = Fernet(key)
    return f.decrypt(info).decode()