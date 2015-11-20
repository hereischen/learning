# -*- coding: utf-8 -*-
from base64 import b64encode, b64decode
from M2Crypto.EVP import Cipher

__all__ = ['encrypt', 'decrypt']

ENC = 1
DEC = 0


# 128bits AES
# The cipher mode is CBC with PKCS5 padding
def get_cryptor(op, key, alg='aes_128_ecb', iv=None):
    if iv is None:
        iv = '\0' * 16
    cryptor = Cipher(alg=alg, key=key, iv=iv, op=op)
    return cryptor


def encrypt(key, plaintext):
    cryptor = get_cryptor(ENC, key)
    ret = cryptor.update(plaintext)
    ret = ret + cryptor.final()
    ret = b64encode(ret)
    return ret


def decrypt(key, ciphertext):
    cryptor = get_cryptor(DEC, key)
    ciphertext = b64decode(ciphertext)
    ret = cryptor.update(ciphertext)
    ret = ret + cryptor.final()
    return ret
