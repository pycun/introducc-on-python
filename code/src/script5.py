"""
Condicionales
"""

# region Siempre verdadero
if True:
    print("Condicion #1: Siempre voy a entrar a la condición\n")
# endregion

# region Siempre falso
if False:
    print("Condicion #2: Nunca voy a entrar a esta condicional\n")
# endregion


# region Negacion
if not False:
    print("Condicion #3: Soy la negacion de falso, por eso soy verdadero\n")
# endregion


# region Condicion en variables
def pay_taxes():
    print("Condicion #4: Bienvenido al mundo de los impuestos\n")

adult = True or False

if adult:
    pay_taxes()
# endregion


# region Condiciones un poco más complejas
var1 = True
var2 = False
var3 = True
if (var1 and var2) or var3:
    # (True and False) or True
    # (False) or True
    # True
    print("Condicion #5: Es una condicion un poco más compleja, pero logramos entrar\n")
# endregion


