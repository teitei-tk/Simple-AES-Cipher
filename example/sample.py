import sys
import os
sys.path.append(os.path.dirname(os.path.abspath(__file__)) + '/../')

from simple_aes_cipher import AESCipher, generate_secret_key


passphrase = "hogefuga".encode('utf-8')
secret_key = generate_secret_key(passphrase)

cipher = AESCipher(secret_key)
raw_text = "abcdefg"

text = cipher.encrypt(raw_text)
print(text)
assert raw_text != text

decrypt_text = cipher.decrypt(text)
print(decrypt_text)
assert decrypt_text == raw_text
