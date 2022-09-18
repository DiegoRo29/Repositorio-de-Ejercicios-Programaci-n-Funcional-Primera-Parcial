from tkinter import N


def tablas(t: int, n: int):
    for i in range (1,t+1):
        tabla(i,n,10)

def tabla(t:int, n: int, spc: int):
    for i in range(1,n+1):
        for j in range (1,n+1):
        print(f"{t:^{spc}} x {i:^{spc}} = {t*i:^{spc}}")

t = int(input("¿Hasta que tablas quieres calcular?: "))
n = int(input("¿Hasta que tablas quieres calcular?: "))
tablas(t,n)