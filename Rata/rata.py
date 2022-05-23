"""Calcular cuando la ciudad A sobrepasa la ciudad B en su crecimiento"""

from tkinter import N


print("-------------------------------------------")
print("-------------Rata exponencial--------------")
print("-------------------------------------------")

#Processing
A = 3.5
B = 5.0
n = 1980
while (A < B):
    A = A + 0.07 * A
    B = B + 0.05 * B
    n = n + 1

#Output
print("El crecimiento de la rata A es mayor que la rata B en el año: " + str(n)) 