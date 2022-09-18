#codedex
A = int(input("Ingrese valor de A:"))
B = int(input("ingrese valor de B:"))
C = int(input("ingrese valor de C:"))
raiz1 = (-B + ((B*B - 4*A*C)**0.5)) / (2*A) #hay parentesis que se pueden quitar
raiz2 = (-B - ((B*B - 4*A*C)**0.5)) / (2*A)
print(raiz1)
print(raiz2)