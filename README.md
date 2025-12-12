Este proyecto es un ejemplo básico de Programación Orientada a Objetos en Python, enfocado en el concepto de polimorfismo.

El programa define una superclase llamada Animal, que representa un animal de forma general. Esta clase contiene un atributo común (nombre) y un método llamado sonido, que describe el comportamiento básico de cualquier animal.

A partir de la superclase Animal se crean dos subclases: Vaca y Lobo. Estas clases heredan los atributos de Animal y redefinen el método sonido para que cada animal produzca su propio sonido característico.

El polimorfismo se observa cuando se llama al método sonido desde objetos que pertenecen a diferentes clases (Vaca y Lobo), pero que comparten la misma interfaz heredada de Animal. Aunque el método se llama de la misma forma, el comportamiento cambia según el tipo de objeto.

Para ejecutar el programa, basta con tener Python instalado y ejecutar el archivo que contiene las clases y la creación de los objetos. Al correr el programa, se mostrará en pantalla el sonido correspondiente de cada animal.
