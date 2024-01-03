'''
Bootcamp Ciberseguridad
Práctica Criptografía
Carlos Gutiérrez, Torrejón
Ejercicio 13
'''
import ed25519
import os

my_path = os.path.dirname(__file__)

fichero_fpriv = my_path + "\ed25519-priv"
privatekey = open(fichero_fpriv,"rb").read()

fichero_fpubl = my_path + "\ed25519-publ"
pubkey = open(fichero_fpubl,"rb").read()

print("Clave PRIVADA: ", privatekey.hex())
print("Clave PUBLICA: ", pubkey.hex())

signedKey = ed25519.SigningKey(privatekey)
msg = bytes('El equipo está preparado para seguir con el proceso, necesitaremos más recursos.','utf8')
signature = signedKey.sign(msg, encoding='hex')

print("Firma Generada (64 bytes):", signature.hex())

print("==================================================")
print("               VERIFICAR FIRMA")
print("==================================================")

try:
    verifyKey = ed25519.VerifyingKey(pubkey)
    verifyKey.verify(signature, msg, encoding='hex')
    #pubkey.verify(signature, msg, encoding='hex')
    print("La firma es válida")
except:
    print("Firma inválida!")
