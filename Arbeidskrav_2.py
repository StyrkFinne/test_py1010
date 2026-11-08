
"""
Arbeidskrav 2

Styrk Finne, 8. nov 2026

"""

# Oppgave 1
alder = int(input("Hvilket år er du født? "))

aar     = 2024
ant_aar = aar - alder

print("Personen blir", ant_aar , "år i løpet av", aar)


# Oppgave 2
import math as mm

ant_elever = int(input("Skriv inn antall elever: "))

ant_pizza   = mm.ceil(ant_elever / 4)

print("Det må handles inn", ant_pizza , "pizzaer til festen")


# Oppgave 3
import numpy as np

# Omregnings funksjon --> grader til radianer
def omregning_grad_radianer(v_grad):
    v_rad = v_grad * np.pi / 180
    return v_rad

v_grad = float(input("Skriv inn gradtallet: "))

v_rad = omregning_grad_radianer(v_grad) 

print("Vinkel", f"{v_grad} gir {v_rad:.2f} radianer")


# Oppgave 4
# 4.a
data = {
        "Norge":      ["Oslo",0.634],
        "England":    ["London",8.982],
        "Frankrike":  ["Paris",2.161],
        "Italia":     ["Roma",2.873]
        }

# 4.b
land = input("Skriv inn et land: ")

hovedstad      = data[land][0]
ant_innbyggere = data[land][1]

print(f"{hovedstad} er hovedstaden i {land} og det er {ant_innbyggere} mill. innbyggere i {hovedstad}")

#4.c
land           = input("Skriv inn et nytt land: ")
hovedstad      = input("Skriv inn hovedstaden: ")
ant_innbyggere = float(input("Skriv inn antall innbyggere: "))

data[land] = [hovedstad, ant_innbyggere]

print("\nOppdatert dictionary:")
print(data)


# Oppgave 5
#import numpy as np

# funksjon --> regner ut arealet og «ytre» omkrets
def figur(a, b):
    r = a / 2

    areal   = (a * b) / 2 + (np.pi * r**2) / 2
    omkrets = b + np.sqrt(a**2 + b**2) + np.pi * r

    return areal, omkrets


a = float(input("Skriv inn a: "))
b = float(input("Skriv inn b: "))

areal, omkrets = figur(a, b)

print(f"Arealet er      {areal:.2f}")
print(f"Ytre omkrets er {omkrets:.2f}")


# Oppgave  6
#import numpy as np
import matplotlib.pyplot as plt

x = np.linspace(-10, 10, 200)
y = -x**2 - 5

plt.plot(x, y)
plt.title("f(x) = -x² - 5")
plt.xlabel("x")
plt.ylabel("f(x)")
plt.grid()

plt.show()

