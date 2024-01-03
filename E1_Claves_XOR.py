'''
Bootcamp Ciberseguridad
Práctica Criptografía
Carlos Gutiérrez, Torrejón
Ejercicio 1
'''

# Claves dadas'B1EF2ACFE2BAEEFF'
clave_Fija_Codigo = 0xB1EF2ACFE2BAEEFF
clave_Final_Desarrollo = 0x91BA13BA21AABB12
clave_KM_Produccion = 0xB98A15BA31AEBB3F

# Punto 1
# Cálculo de la clave del Key Manager para el entorno de desarrollo
clave_KM_Desarrollo = hex(clave_Fija_Codigo^clave_Final_Desarrollo)
# Punto 2
# # Cálculo de la clave Final para el entorno de producción
clave_Final_Produccion = hex(clave_Fija_Codigo^clave_KM_Produccion)

print("---------------------\nPráctica Criptografía\nEjercicio 1\n---------------------")
print("1.1 Clave Key Manager (Desarrollo): ",clave_KM_Desarrollo[2:])
print("1.2 Clave Final (Producción): \t\t",clave_Final_Produccion[2:])
