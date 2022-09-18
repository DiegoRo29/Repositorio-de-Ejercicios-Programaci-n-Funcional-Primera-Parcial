# # """ Hacer una funcion que reciba dos argumentos de tipo string, el primero que sea un mensaje de saludo, y el segundo
# # el primer nombre de una persona. y diga: <saludo> <persona>
# # """
# def mensaje(msg:str):
#     print("Dentro de la función",msg,id(msg))
#
# def saludo(msg:str, nombre:str):
#     print(msg, nombre)
#
# if __name__ == "__main__":
#     saludo("Buenos días", "Alex")
#     salud()
# """
# Función que calcula la edad de una persona dado el año de nacimiento, el mensaje de salida debe ser:
# "Hola <nombre>, tienes <n> años"
# """
def saludo(msg:str, nombre:str):
     print(msg, nombre)

def saludo_edad(nombre:str, a_nacimiento:int):
    edad = 2022-a_nacimiento
    print("Hola",nombre, "tienes", edad, "años")

def calcular_edad(a_actual:int, a_nacimiento:int)->int:
    return a_actual-a_nacimiento


def saludo(nombre:str, edad:int):
    print("Hola",nombre,"tienes", edad, "años")

if __name__ == "__main__":
    saludo("Alex", calcular_edad(2022,2003))

    edad = calcular_edad(2022,2003)
    saludo("Fer", edad)

    # print(calcular_edad(2022,1971))

    # saludo("Buenos días", "Alex")
    # saludo_edad("Alex",1971)

"""
Hacer una función que reciba dos números y retorne la suma del cuadrado de los números usando además una
función que haga el proceso del cuadrado
"""
def cuad(n:int)->int:
    return n*n
def suma(a:int, b:int)->int:
    return a+b
