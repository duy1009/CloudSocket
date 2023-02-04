from Crypto.Cipher import ARC4
from Crypto.Hash import SHA256, HMAC
from Crypto.Random import get_random_bytes

def enc(key,p):
		return ARC4.new(key).encrypt(p)

def dec(key,msg):
		return ARC4.new(key).decrypt(msg)