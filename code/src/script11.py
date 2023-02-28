"""
Clases
"""

class Alumno:
    universidad = 'UPQROO'

    def __init__(self, nombre):
        self.nombre = nombre

    def saludar(self):
        """
        Imprime un saludo en pantalla
        """
        print("Hola, {nombre}".format(nombre=self.nombre))

alumno = Alumno("Pablo")
alumno.saludar()
print(alumno.universidad)
