"""
Tipado dinámico/debil
"""

var1 = "Mi variable es un string que contiene este texto"
print("Hasta este primer momento la variable es del tipo: ", type(var1))

var1 = True
print("Hasta este segundo momento la variable es del tipo: ", type(var1))

var1 = 0
print("Hasta este tercer momento la variable es del tipo: ", type(var1))

var1 = str(var1)  # Con str() python cambia la variable a un string "0"
print("Hasta este cuarto momento la variable es del tipo: ", type(var1))

