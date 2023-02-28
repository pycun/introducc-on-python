"""
Ciclo For

Es usado para iterar sobre una secuencia como:
    - lista
    - tupla
    - sets
    - diccionario
    - strings
"""

# region ciclo for con listas
lista = [0, 1, 2, 3, 4]
for item in lista:
    print("El elemento es: ", item)
# endregion


# region ciclo for con tuplas
tupla = (0, 1, 2, 3, 4)
for item in tupla:
    print("El elemento es: ", item)
# endregion


# region ciclo for con sets
sets = {0, 1, 2, 3, 4, 2, 0}
for item in sets:
    print("El elemento es: ", item)
# endregion


# region ciclo for con diccionarios
diccionario = {
    'llave-a': "Valor A",
    'llave-b': "Valor B",
    'llave-c': "Valor C",
}
for item in diccionario:
    print("El elemento es: ", item)
# endregion


# region ciclo for con string
string = "Hola PyCun"
for item in string:
    print("El elemento es: ", item)
# endregion




# region Ciclo for
""" Código Javascript
lista = ['0, ..., 5]
for (let i = 0; i < 5; i++) {
  console.log("El elemento es: ", i);
}
"""
for item in range(5):
    print("El elemento es: ", item)
# endregion