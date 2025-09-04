#Conjuntos
A = {"Scorpion", "Kung Lao", "Sub-Zero", "Liu Kang", "Raiden"}
B = {"Johnny Cage", "Onaga", "Sonya Blade", "Liu Kang", "Raiden"}
#Dados dos conjunto, A y B, escribe un programa en Python que imprima los elementos que se encuentren en A o en B, o en ambos.
print(A | B)
#Dados dos conjutnos, A y B, escribe un programa en Python que imprima los elementos que se encuentren en A y en B.
print(A & B)
#Dados dos conjutnos, A y B, escribe un programa en Python que imprima el conjunto de los elementos que se encuentran en A o en B, pero no en ambos.
print(A.symmetric_difference(B))
#Dados un conjunto, A, escribe un programa en Python que imprima si el conjunto es un subconjunto de otro conjunto, B.
print(A.issubset(B))
#Dados un conjunto, A, escribe un programa en Python que imprima el número de elementos del conjunto
print(len(A))