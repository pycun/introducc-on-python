"""
Ciclos - Ciclo while
"""
variable_auxiliar = 0

while variable_auxiliar != 5:  # NOTE: Cuidado de cómo escribes tu condicional
    print("El valor de la variable auxiliar es de: ", variable_auxiliar)

    variable_auxiliar += 2

    # La anterior linea podemos escribirlo como
    # variable_auxiliar = variable_auxiliar + 1


# region No existe un solo camino. ¿cóomo reescribir el codigo del script 6?
variable_auxiliar = 0
while variable_auxiliar < 5:
    print("El valor de la variable auxiliar es de: ", variable_auxiliar)
    variable_auxiliar += 1


variable_auxiliar = 0
while True:
    print("El valor de la variable auxiliar es de: ", variable_auxiliar)
    variable_auxiliar += 1
    if variable_auxiliar >= 5:
        break
# endregion