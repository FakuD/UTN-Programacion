#Ejercicio 1

print("Hola Mundo!")


#Ejercicio 2

nombre = input("Introduce tu nombre: ")
print(f"Hola {nombre}!")



#Ejercicio 3

nombre = input("Introduce tu nombre: ")
apellido = input("Introduce tu apellido: ")
edad = input("Introduce tu edad: ")
pais = input("Ingresa tu lugar de residencia: ")
print(f"Soy {nombre} {apellido}, tengo {edad} años y vivo en {pais}")

#Ejercicio 4

radio = int(input("Por favor digita el radio del circulo: "))
perimetro = 2*3.14*radio
area = 3.14 * radio ** 2 
print(f"El perimetro de un circulo es: {perimetro}")
print(f"El area de un circulo es: {area}")

#Ejercicio 5

segundos = int(input("Por favor digite una cantidad de segundos: "))
horas = segundos /3600
if horas <= 1:
    print(f"Según la cantidad de segundos dadas por el usario equivale a {horas} hora")
else:
    print(f"Según la cantidad de segundos dadas por el usario equivale a {horas} horas")


#Ejercicio 6

num = int(input("Introduce un numero para saber su tabla de multiplicar: "))
for i in range (1,11):
    print(f"{num} * {i} = {num*i}")

#Ejercicio 7

num1 = int(input("Por favor ingrese un numero distinto de 0: "))
if num1 == 0:
    num1 = int(input("por favor introduzca un numero distinto de 0"))

num2 = int(input("Por favor ingrese otro numero distinto de 0: "))
if num2 == 0:
    num2 = int(input("por favor introduzca un numero distinto de 0"))

suma = num1 + num2
resta = num1 - num2 
division = num1 / num2 
multiplicacion = num1 * num2 

print(f"el resultado de sumar los numeros es {suma}")
print(f"el resultado de restar los numeros es {resta}")
print(f"el resultado de multiplicar los numeros es {multiplicacion}")
print(f"el resultado de dividir los numeros es {division}")

#Ejercicio 8

peso = float(input("Por favor introduzca su peso en kg: "))
estatura = float(input("Por favor introduzca su estatura en metros: "))
masa = peso / estatura **2
print(f"Su indice de masa corporal es: {masa}")

#Ejercicio 9

grados = int(input ("Por favor introduzca la temperatura en grados celsius: "))
fahrenheit = (grados * 9/5) + 32
print(f"La temperatura en Fahrenheit es {fahrenheit}")

#Ejercicio 10

num1 = int(input("Introduzca el primer numero: "))
num2 = int(input("Introduzca el segundo numero: "))
num3 = int(input("Introduzca el tercer numero: "))
promedio = (num1 + num2 + num3)/3
print(f"El promedio de los 3 numero es {promedio}")


