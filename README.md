# Laberinto 24/25

Este proyecto consiste en un juego o simulador de laberinto desarrollado para el curso 2024/2025. Se ha diseñado utilizando varios **patrones de diseño** orientados a objetos con el objetivo de lograr un código limpio, escalable y mantenible.

Puedes ver el proyecto completo tamibie en mi [repositorio gitHub](https://github.com/rumanoloko/Diseno_sw_proyecto_remoto.git).

## Patrones de diseño utilizadosh

### 1. **Decorator**
**Definicion**

Asigna dinámicamente responsabilidades adicionales a un objeto. Los
 decoradores proporcionan una alternativa flexible a la subclasificación para extender
 la funcionalidad

**Ejemplo**

Se implemento en elementos como Pared Bomba que permite al funcionamiento por defecto de la pared, extender nuevas funcionalidades de forma dinamina vinculadas a las de bomba
### 2. **Strategy**
**Definicion**

Define una familia de algoritmos, encapsula cada uno en un objeto, de
 modo que son intercambiables. El Strategy permite cambiar el algoritmo sin que
 afecte al cliente.

**Ejemplo**

La implementacion de modos de cada bicho como puede ser Perezoso o Agresivo, que permiten cambiar el comportamiento del bicho sin modificar explicitamente codigo  clase bicho para varias las funcionalidades
### 3. **State**
**Definicion**

Permite a un objeto alterar su comportamiento cuando cambia su estado
 interno. El objeto parecerá cambiar de clase.

**Ejemplo**
En el juego del laberinto se implementó para controlar el comportamiento de los entes controlando si estado interno(**Vivo()** o **Muerto**())
### 4. **Composite**
**Definicion**

Compone objetos en una estructura de árbol para representar jerarquías
 todo-parte. El Composite permite que el cliente trate de manera uniforme tanto a
 objetos individuales como a objetos compuestos.

**Ejemplo**

Dentro del juego se implementa este patron para elemetos como pueden ser laberinto o habitacion que permiten encapsular dentro de
ellos más elementos.
### 5. **Singleton**
**Definicion**

Asegura que una clase solo tiene una instancia y proporciona un punto de
 acceso a la instancia

**Ejemplo**

Se implementó en as orientaciones como norte, sur, este u oeste que posibilita la existencia de instancias unicas de cada tipo de orientacion si la posibilidad de crear más orienciones de un mismo tipo.
### 6. **Builder**
**Definicion**

Separa la construcción de un objeto complejo de su representación, de
 modo que el mismo proceso de construcción se utiliza para crear diferentes
 representaciones.

**Ejemplo**
Dentro del juego se implementó para desglosar la crcon del laberinto.
Esto se aprecia a tréves de self.crearHabitaciones(self, dict["Laberinto"]), self.crearBhs(self, dict["Bichos"]), self.crearPuertas(self, dict["Puertas"])
que tras crearse cada parte se combinan dentro del metodo self.crearLaberinto(self, dict)