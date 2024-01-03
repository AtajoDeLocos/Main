'''
Bootcamp Ciberseguridad
Práctica Criptografía
Carlos Gutiérrez, Torrejón
Ejercicio 12
'''

from base64 import b64encode, b64decode
from Crypto.Cipher import AES

# Preparando los datos necesarios
textoPlano_bytes = bytes('He descubierto el error y no volveré a hacerlo mal', 'UTF-8')
clave = bytes.fromhex('E2CFF885901B3449E9C448BA5B948A8C4EE322152B3F1ACFA0148FB3A426DB74')
nonce = b64decode('9Yccn/f5nJJhAt2S')
datos_asociados_bytes = bytes("carlos.gutierrez", "UTF-8")

# Montando el cifrador
cipher = AES.new(clave, AES.MODE_GCM,nonce=nonce)
# Añadimos el TAG
cipher.update(datos_asociados_bytes)
texto_cifrado_bytes, tag = cipher.encrypt_and_digest(textoPlano_bytes)

print("Texto cifrado HEX: " + texto_cifrado_bytes.hex())
print("\nTexto cifrado BASE64: ", b64encode(texto_cifrado_bytes))