import os
import pathlib
import cryptography 
import re
import requests
from cryptography.fernet import Fernet
key = Fernet.generate_key()
with open("symmetric.key", "wb") as fo:
    fo.write(key)
encrypted_email = "iamsven2005@gmail.com"
key = b'K9d5WxI61uDucnDzlSZCXXP_9mBlGMPs38Pb6Ya0_aU='
f = Fernet(key)
decrypted_email = f.decrypt(encrypted_email)
print(decrypted_email)