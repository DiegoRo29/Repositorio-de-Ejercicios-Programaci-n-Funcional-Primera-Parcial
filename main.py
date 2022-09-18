# un array solamente puede tener tipos de datos del mismo, un array dinamico significa que puede 
# crecer, una lista sin elementos es una lista vacia */
# Las listas tienen funciones, unas de las mas usadas es len
# los parentesis son tuplas, las llaves son conjuntos, los corchetes son listas
# todas las listas empiezan en 0
# Como no es inclusive se toma en cuenta el numero anterior
# Reverse Imprime la lista al revés
#

from audioop import reverse
from re import M


mi_lista = [1,2,3,4]
print()      
lista_vacia = []
print(lista_vacia)

mi_lista2 =[1, "hola", True, 3.14, [1,2,3], (1,2,3), {4,5,6}]
print(mi_lista2)

print(len(mi_lista2))
print(f"Mi lista: {mi_lista}")

print(f"No de elementos: {len(mi_lista)}")
print(f"Primer elemento: {mi_lista[-1]},{mi_lista[-2]},{mi_lista[-3]},{mi_lista[-4]}")

print(mi_lista[0:-1])
print(mi_lista[0:3])
print(mi_lista[0:])
print(mi_lista[:])

# modificar elementos de la lista

mi_lista[2]= "tres"
print(mi_lista)

# Insertar la lista [5,"seis",7,8] al final de la lista mi_lista
#Todos los elementos a partir de aqui, me pone esto
mi_lista[len(mi_lista):] = [5,"seis",7,8] 
print(mi_lista)
#slices (rebanadas)

mi_lista = [1,2,3,4]
mi_lista.append("cinco")
print(mi_lista)

ml = []
for i in range(1,5):
    ml.append(i)
print(ml)

#ml.append([6,7,8])
#print(ml)
ml.extend([6,7,8,9,8,5])
print(ml)
#insertar un elemento en la posicion 1,2,3,4
ml.insert(4,"5")
print(ml)

# del ml[5]
print(ml)

ml.remove(8)
print(ml)

ml.remove
print(ml)

ml.reverse()
print(ml)

l1 = [1,2,3,4,5,6,7,8,9,10]
l2 = l1[:]
print(l1)
l1.reverse()
print(id(l1))
print(id(l2))

ld = [[5,4,6],[7,8,2],[1,3,4,5],[6,7]]
print(f"Desordenado: {ld}")
ld.sort()
print(f"Ordenado: {ld}")
ld = [5,4,6,7,8,2,1,3,4,5,6,7]
s1 = sorted(ld)
print(s1)
s2 = sorted(ld,reverse=True)  #Iterable es una coleccion o estructura de datos que tiene varios caracteres que se pueden recorrer
print(s2)
ld

ceros = [0,0,0,0,0,0,0,0,0,0]
print(ceros)
ceros = [[0]*9]*9
print(ceros)

valor_max = max(ld)
print(valor_max)

valor_min = min(ld)
print(valor_min)
cuatros = ld.count(4)
print(cuatros)
repetidos = []
print("----------------")
for i in range(1,9):
    repetidos.append (ld.count(i))

print(repetidos)