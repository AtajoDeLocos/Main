'''
Bootcamp Ciberseguridad
Práctica Criptografía
Carlos Gutiérrez, Torrejón
Ejercicio 3
'''

from Crypto.Cipher import ChaCha20_Poly1305
from base64 import b64decode, b64encode
from Crypto.Random import get_random_bytes
import json

try:
    textoPlano = bytes('KeepCoding te enseña a codificar y a cifrar', 'UTF-8')
    # Se requiere o 256 o 128 bits de clave, por ello usamos 256 bits que se transforman en 64 caracteres hexadecimales
    clave = bytes.fromhex('AF9DF30474898787A45605CCB9B936D33B780D03CABC81719D52383480DC3120')
    nonce_mensaje = b64decode('9Yccn/f5nJJhAt2S')
    # Autenticamos el mensaje a tra vés del usuario "carlos.gutierrez"
    datos_asociados = bytes('carlos.gutierrez', 'utf-8')

    # Instanciamos el cifrador
    cipher = ChaCha20_Poly1305.new(key=clave, nonce=nonce_mensaje)
    # Añadimos el MAC
    cipher.update(datos_asociados)
    # Ciframos
    texto_cifrado_bytes, tag = cipher.encrypt_and_digest(textoPlano)

    # Pintamos
    print("---------------------\nPráctica Criptografía\nEjercicio 3\n---------------------")
    print("nonce: ", nonce_mensaje.hex())
    print("criptograma: ", texto_cifrado_bytes.hex())
    print("MAC: ", tag.hex())
 
except (ValueError, KeyError) as error: 
    print("Problemas al descifrar....")
    print("El motivo del error es: ", error)

# Verificando
try:
    print("--- VERIFICANDO ---")
    decipher = ChaCha20_Poly1305.new(key=clave, nonce=nonce_mensaje)
    decipher.update(datos_asociados)
    plaintext = decipher.decrypt_and_verify(texto_cifrado_bytes,tag)
    print('Datos cifrados en claro = ',plaintext.decode('utf-8'))

except (ValueError, KeyError) as error: 
    print("Problemas al descifrar....")
    print("El motivo del error es: ", error)