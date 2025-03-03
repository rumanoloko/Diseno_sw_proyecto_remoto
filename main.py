import time
from machine import Pin
from pysense import Pysense
from lps22hb import LPS22HB
from si7021 import SI7021
from light_sensor import LightSensor

# Inicialización de los sensores
pysense = Pysense()  # Inicializa la placa Pysense
sensor_temp = SI7021(pysense)  # Sensor de temperatura y humedad
sensor_pres = LPS22HB(pysense)  # Sensor de presión
sensor_light = LightSensor(pysense)  # Sensor de luminosidad

# LED conectado al pin 15 (puedes cambiarlo si es necesario)
led = Pin(15, Pin.OUT)

# Umbral de luminosidad
luminosidad_umbral = 100  # 100 lux


# Función para obtener y mostrar los datos de los sensores
def obtener_datos_sensores():
    # Leer datos de los sensores
    temperatura = sensor_temp.temperature()  # Temperatura en grados Celsius
    humedad = sensor_temp.humidity()  # Humedad relativa
    presion = sensor_pres.pressure()  # Presión atmosférica
    luminosidad = sensor_light.light()  # Lux

    # Mostrar los datos en la terminal
    print(f"Temperatura: {temperatura} °C")
    print(f"Humedad: {humedad} %")
    print(f"Presión: {presion} hPa")
    print(f"Luminosidad: {luminosidad} lux")

    # Encender el LED si la luminosidad es menor que el umbral
    if luminosidad < luminosidad_umbral:
        print("Luminosidad baja, encendiendo LED...")
        led.value(1)  # Encender el LED
    else:
        print("Luminosidad suficiente, apagando LED...")
        led.value(0)  # Apagar el LED

    print("-------------------------------")


# Bucle principal para obtener datos cada 5 segundos
while True:
    obtener_datos_sensores()
    time.sleep(5)  # Esperar 5 segundos antes de leer los sensores nuevamente

