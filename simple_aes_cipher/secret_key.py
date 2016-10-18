# -*- coding: utf-8 -*-

from hashlib import sha256


def generate_secret_key(passphrase, algorithm_func=sha256):
    return algorithm_func(passphrase.encode('utf-8')).digest()
