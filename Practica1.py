# -*- coding: utf-8 -*-
"""
Created on Wed Feb 12 00:18:14 2020

@author: booed_000
"""

"""Practica 1"""
print('ejercicio 1, practica 1')
print('Probar lineas de codigo')
bicycles=['trek', 'cannondale', 'redline', 'specialized']
print(bicycles)
print()
print('ejercicio 1.1, practica 1')
print('Probar lineas de codigo')
bicycles=['trek', 'cannondale', 'redline', 'specialized']
print(bicycles[1])


print('Tarea 1.2,listas')

"""Nombres"""
name=['Sabino','Luis','Daniel','Heriberto']
print(name[0].title())
print(name[1].title())
print(name[2].title())
print(name[3].title())

"""Mensaje"""
print(name[0].title(), 'Crack')
print(name[1].title(), 'Gordo')
print(name[2].title(), 'Rifle')
print(name[3].title(), 'Jerry')

"""Lista de deseos"""
Lista_Deseos=['XboxSeries','Playstation5','PokemonReal','Dinero','AmericaJersey','Helado','Papas','Perros','Tacos','Hamburguesas','CocaCola','Pepsi','Sandia','Mango','MiTitulo']
print('Me gustaria tener', Lista_Deseos[0])
print('Me gustaria tener', Lista_Deseos[1])
print('Me gustaria tener', Lista_Deseos[2])
print('Me gustaria tener', Lista_Deseos[3])
print('Me gustaria tener', Lista_Deseos[4])
print('Me gustaria tener', Lista_Deseos[5])
print('Me gustaria tener', Lista_Deseos[6])
print('Me gustaria tener', Lista_Deseos[7])
print('Me gustaria tener', Lista_Deseos[8])
print('Me gustaria tener', Lista_Deseos[9])
print('Me gustaria tener', Lista_Deseos[10])
print('Me gustaria tener', Lista_Deseos[11])
print('Me gustaria tener', Lista_Deseos[12])
print('Me gustaria tener', Lista_Deseos[13])
print('Me gustaria tener', Lista_Deseos[14])


print()
print('Tarea 3.4, funciones')

def make_shirt(size, message):
    print("Que sea de talla," + size + " mi camisa.")
    print('Que diga, "' + message + '"')
make_shirt('Grande', 'Quiero pasar programacion avanzada')

"""Mensaje y tamaño predeterminado"""
def make_shirt(size='Grande', message='I love Python!'):
    print("Que sea talla" + size + " mi camisa.")
    print('Que diga, "' + message + '"')
make_shirt()
make_shirt(size='Mediana')
make_shirt('Chica', 'Arriba la programacion.')

"""Ciudades y paises"""
def describe_city(ciudad, pais='Mexico'):
    """Describe a city."""
    mensaje = ciudad.title() + " esta en " + pais + "."
    print(mensaje)
describe_city('cdmx')
describe_city('madrid', 'España')
describe_city('puebla')


"""Clases, Tarea 4.2"""
print('Restaurante')
class Restaurant():
    def __init__(self, nombre, tipo_Restaurante):
        """Initialize the restaurant."""
        self.nombre = nombre.title()
        self.tipo_Restaurante = tipo_Restaurante

    def describe_restaurant(self):
        msg = self.nombre + " el mejor servio de " + self.tipo_Restaurante + "."
        print(msg)

    def open_restaurant(self):
        msg = self.nombre + " abierto ahora, adelante!"
        print(msg)

restaurant = Restaurant('Mario´s', 'pizza')
print(restaurant.nombre)
print(restaurant.tipo_Restaurante)

restaurant.describe_restaurant()
restaurant.open_restaurant()

""""3 Restaurantes"""
print( )
print('3 Restaurantes')
class Restaurant():

    def __init__(self, nombre, tipo_Restaurante):
        self.nombre = nombre.title()
        self.tipo_Restaurante = tipo_Restaurante

    def describe_restaurant(self):
        msg = self.nombre + " el mejor servicio de " + self.tipo_Restaurante + "."
        print(msg)

    def open_restaurant(self):
        msg = self.nombre + " abierto ahora, adelante!"
        print(msg)

Elperro_loco = Restaurant('EL perro loco', 'tacos')
Elperro_loco.describe_restaurant()
Elperro_loco.open_restaurant()

Dona_pelos = Restaurant("Doña pelos", 'quesadillas')
Dona_pelos.describe_restaurant()
Dona_pelos.open_restaurant()

Programando = Restaurant('Programando', 'Hamburguesas')
Programando.describe_restaurant()
Programando.open_restaurant()


"""Usuarios"""
print('10 usuarios')
class User():

    def __init__(self, first_name, last_name, username, correo, localidad):
        self.first_name = first_name.title()
        self.last_name = last_name.title()
        self.username = username
        self.correo = correo
        self.localidad = localidad.title()

    def describe_user(self):
        print(self.first_name + " " + self.last_name)
        print("  Username: " + self.username)
        print("  Correo: " + self.correo)
        print("  Localidad: " + self.localidad)

    def greet_user(self):
        print("Hola de nuevo, " + self.username + "!")

Goku = User('Goku', 'Son', 'kakaroto', 'Goku@programacion.com', 'miravalle')
Goku.describe_user()
Goku.greet_user()

Sixto = User('Sixto', 'Uribe', 'Sixtin', 'Sixtin@programacion.com', 'bambu')
Sixto.describe_user()
Sixto.greet_user()

Luisito = User('Luisito', 'Aguilar', 'LuisitoRey', 'Lr@programacion.com', 'cdmx')
Luisito.describe_user()
Luisito.greet_user()

Berto = User('Berto', 'Martinez', 'Ber', 'Bm@programacion.com', 'GAM')
Berto.describe_user()
Berto.greet_user()

Danielsito = User('Daniel', 'Uribe', 'Rifle', 'Rifle@programacion.com', 'bambu')
Danielsito.describe_user()
Danielsito.greet_user()

Brian = User('Brian', 'Reus', 'Messi', 'Br@programacion.com', 'Tepito')
Brian.describe_user()
Brian.greet_user()

Jerry = User('Jerry', 'Darwin', 'Nigga', 'Darwin@programacion.com', 'campo')
Jerry.describe_user()
Jerry.greet_user()

Negrete = User('Negrete', 'Uribe', 'Nutria', 'Nu@programacion.com', 'Ecatepec')
Negrete.describe_user()
Negrete.greet_user()

Sireno = User('Sireno', 'Bega', 'Ariel', 'Bega@programacion.com', 'el oyo')
Sireno.describe_user()
Sireno.greet_user()

