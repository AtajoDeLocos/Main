'''
Bootcamp Ciberseguridad
Práctica Criptografía
Carlos Gutiérrez, Torrejón
Ejercicio 6
'''

# Librerías
import jks
import os

from Crypto.Hash import HMAC, SHA256

# Definimos la ruta del KeyStore
path = os.path.dirname(__file__)
keystore = path + "/KeyStorePracticas"
# Cargamos el keystore
ks = jks.KeyStore.load(keystore, "123456")
# Lo recorremos hasta encontrar el que buscamos
for alias, sk in ks.secret_keys.items():
    if sk.alias == "hmac-sha256":
        key = sk.key

#Generamos el hmac, en este caso SHA512 - HMAC-512
mensaje_bytes = bytes("Siempre existe más de una forma de hacerlo, y más de una solución válida.","utf8")
hmac256 = HMAC.new(key,mensaje_bytes,digestmod=SHA256)

#Propio de los hmac, como representar el valor
print(hmac256.hexdigest())

# VALIDACIÓN
key=bytes.fromhex("a212a51c997e14b4df08d55967641b0677ca31e049e672a4b06861aa4d5826eb")
mensaje_bytes = bytes("Siempre existe más de una forma de hacerlo, y más de una solución válida.","utf8")

result = "KO"

hmac256 = HMAC.new(key,mensaje_bytes,digestmod=SHA256)

try:
    #hmac256.verify(hmac_validar_bytes)
   # si queremos verificar sin convertir a bytes
    print("VALIDACIÓN:")
    hmac256.hexverify(hmac256.hexdigest())
    result = "OK"
except ValueError:
    result = "KO"

print(result)