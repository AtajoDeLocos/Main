'''
Bootcamp Ciberseguridad
Práctica Criptografía
Carlos Gutiérrez, Torrejón
Ejercicio 13
'''
import os

from Crypto.PublicKey import RSA
from Crypto.Signature.pkcs1_15 import PKCS115_SigScheme
from Crypto.Hash import SHA256

my_path = os.path.dirname(__file__)

# Generamos la privada
fichero_fpriv = my_path + "\clave-rsa-oaep-priv.pem"
fpriv = open(fichero_fpriv,'r')
privkey = RSA.import_key(fpriv.read())

msg = bytes('El equipo está preparado para seguir con el proceso, necesitaremos más recursos.','utf8')

hash = SHA256.new(msg)
signer = PKCS115_SigScheme(privkey)
signature = signer.sign(hash)

print("Firma Generada", signature.hex())