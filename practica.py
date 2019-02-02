#definir clase animal
class Animal:
    #método constructor
    def __init__(self, raza, altura, peso):
        self.raza = raza
        self.altura = altura
        self.peso = peso

    #definir funciones
    def comer(self, dormir):
        self.dormir = dormir

    def jugar(self, correr):
        self.correr = correr

#crear objeto animal
Perro = Animal('Canina',200,100)

#imprimir atributos
print('Atributos de la clase animal:', Perro.raza, Perro.altura, Perro.peso)

#llamar funciones
Perro.comer('dormir')
Perro.jugar('correr')

#hacer actividades
print('\nCuando el perro termina de comer se va a', Perro.dormir)
print('\nAl perro le gusta jugar y', Perro.correr)

#definir clase plata
class Planta:
    #método constructor
    def __init__(self, especie, color, tam):
        self.especie = especie
        self.color = color
        self.tam = tam

    #definir funciones
    def crecer(self, altura):
        self.altura = altura

    def adornar(self, adorno):
        self.adorno = adorno

#crear objeto planta
Girasol = Planta('Herbácea', 'Amarillo', 10)

#imprimir atributos
print('\nAtributos de la clase planta:', Girasol.especie, Girasol.color, Girasol.tam)

#llamar funciones
Girasol.crecer('altos')
Girasol.adornar('adornarlas')

#hacer actividades
print('\nLos girasolos son plantas que llegan a crecer muy', Girasol.altura)
print('\nLos girasoles se utilizan en las casas para', Girasol.adorno)