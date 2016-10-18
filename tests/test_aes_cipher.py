# -*- coding: utf-8 -*-

import unittest
import string
import random

import sys
import os
sys.path.append(os.path.dirname(os.path.abspath(__file__)) + '/../')

from simple_aes_cipher import AESCipher, generate_secret_key


class TestAESCipher(unittest.TestCase):
    def setUp(self):
        pass_phrase = self._choice_randome_string()
        self.secret_key = generate_secret_key(pass_phrase)
        self.cipher = AESCipher(self.secret_key)

    def _choice_randome_string(self):
        return ''.join([random.choice(string.ascii_letters + string.digits)])

    def test_encrypt(self):
        text = self._choice_randome_string()
        encrypt_text = self.cipher.encrypt(text)
        self.assertNotEqual(text, encrypt_text)

    def test_decrypt(self):
        text = self._choice_randome_string()

        encrypt_text = self.cipher.encrypt(text)
        self.assertNotEqual(text, encrypt_text)

        decrypt_text = self.cipher.decrypt(encrypt_text)
        self.assertNotEqual(encrypt_text, decrypt_text)
        self.assertEqual(text, decrypt_text)


if __name__ == "__main__":
    unittest.main()
