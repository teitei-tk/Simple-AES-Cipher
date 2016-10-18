import sys
import os
sys.path.append(os.path.dirname(os.path.abspath(__file__)) + '/../')

from simple_aes_cipher import AESCipher, generate_secret_key

pass_phrase = "hogefuga"
secret_key = generate_secret_key(pass_phrase)

# generate cipher
cipher = AESCipher(secret_key)

raw_text = "abcdefg"
encrypt_text = cipher.encrypt(raw_text)
assert raw_text != encrypt_text

decrypt_text = cipher.decrypt(encrypt_text)
assert encrypt_text != decrypt_text
assert decrypt_text == raw_text
