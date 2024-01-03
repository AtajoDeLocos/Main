'''
Bootcamp Ciberseguridad
Práctica Criptografía
Carlos Gutiérrez, Torrejón
Ejercicio 2
'''

import jks
import os

from base64 import b64decode
from Crypto.Cipher import AES
from Crypto.Util.Padding import unpad

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
        
# Definimos texto cifrado e IV
texto_cifrado_bytes = b64decode("TQ9SOMKc6aFS9SlxhfK9wT18UXpPCd505Xf5J/5nLI7Of/o0QKIWXg3nu1RRz4QWElezdrLAD5LO4USt3aB/i50nvvJbBiG+le1ZhpR84oI=")
iv_bytes = bytes.fromhex("00000000000000000000000000000000")

# Desciframos
try:
    cipher = AES.new(clave_ks, AES.MODE_CBC, iv_bytes)
    mensaje_des_x923 = unpad(cipher.decrypt(texto_cifrado_bytes), AES.block_size, style="x923")

    print("---------------------\nPráctica Criptografía\nEjercicio 2\n---------------------")
    print("Descifrado x923: ", mensaje_des_x923.decode("utf-8"))
    
except (ValueError, KeyError) as error:
    print('Problemas para descifrar....')
    print("El motivo del error es: ", error) 

