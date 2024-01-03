'''
Bootcamp Ciberseguridad
Práctica Criptografía
Carlos Gutiérrez, Torrejón
Ejercicio 3
'''

import jks
import os

from Crypto.Cipher import ChaCha20
from base64 import b64decode, b64encode

# ====================================
#  Obtener clave del KeyStore
# ====================================
# Definimos la ruta del KeyStore
path = os.path.dirname(__file__)
keystore = path + "/KeyStorePracticas"
# Cargamos el keystore
ks = jks.KeyStore.load(keystore, "123456")
# Lo recorremos hasta encontrar el que buscamos
for alias, sk in ks.secret_keys.items():
    if sk.alias == "cifrado-sim-aes-256":
        clave_ks = sk.key
# =====================================

textoPlano_bytes = bytes('KeepCoding te enseña a codificar y a cifrar', 'UTF-8')
# No debe fijarse el nonce, aquí lo hacemos por motivos prácticos
nonce_mensaje = b64decode('9Yccn/f5nJJhAt2S')

# Con la clave y con el nonce se cifra. El nonce debe ser único por mensaje
cipher = ChaCha20.new(key=clave_ks, nonce=nonce_mensaje)
texto_cifrado_bytes = cipher.encrypt(textoPlano_bytes)
print("---------------------\nPráctica Criptografía\nEjercicio 3\n---------------------")
print('Mensaje cifrado en HEX = ', texto_cifrado_bytes.hex() )
print('Mensaje cifrado en B64 = ', b64encode(texto_cifrado_bytes).decode())

# Desciframos para verificar el correcto cifrado
decipher = ChaCha20.new(key=clave_ks, nonce=nonce_mensaje)
texto_claro = decipher.decrypt(texto_cifrado_bytes)
print("---Verificando---")
print('Mensaje en claro = ',texto_claro.decode('utf-8'))