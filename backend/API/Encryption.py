from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
from cryptography.hazmat.primitives import padding
from cryptography.hazmat.backends import default_backend
import base64

def encrypt_data(data, key_data):
    key = iv = key_data.encode('utf-8')
    
    data_in_bytes = data.encode('utf-8')
    
    padder = padding.PKCS7(algorithms.AES.block_size).padder()
    padded_data = padder.update(data_in_bytes) + padder.finalize()
    
    cipher = Cipher(algorithms.AES(key), modes.CBC(iv), backend=default_backend())
    
    encryptor = cipher.encryptor()
    encrypted_data = encryptor.update(padded_data) + encryptor.finalize()
    
    encrypted_data_base64 = base64.b64encode(encrypted_data).decode('utf-8')
    return encrypted_data_base64

def decrypt_data(encrypted_data_base64 , key_data):
    encrypted_data = base64.b64decode(encrypted_data_base64)
    
    key = iv = key_data.encode('utf-8')
    
    cipher = Cipher(algorithms.AES(key), modes.CBC(iv), backend=default_backend())
    
    decryptor = cipher.decryptor()
    decrypted_padded_data = decryptor.update(encrypted_data) + decryptor.finalize()
    
    unpadder = padding.PKCS7(algorithms.AES.block_size).unpadder()
    decrypted_data = unpadder.update(decrypted_padded_data) + unpadder.finalize()
    
    decrypted_string = decrypted_data.decode('utf-8')
    return decrypted_string