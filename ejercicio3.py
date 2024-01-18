# Bienvenidos a Sys On Chip
# ==============================
# Ejercicio No.3
# programa en python con tkinter con una ventana que monitorea un semaforo conectado al puerto gpio de una raspberry pi 4.
# La ventana debe tener un semaforo que cambia de color segun se activen las salidas del puerto. 
# La ventana permitira establecer modo automatico o manual.
# La secuencia del modo automatico debe ser primero el rojo 3 segundos, luego verde 4 segundos y por ultimo ambar 1 segundo.
# En el modo manual debe permitir ponerlo intermitente en rojo o intermitente en amarillo.
# ==============================================================================================

import RPi.GPIO as GPIO
import time

# Configuración de pines
pin_rojo = 17
pin_amarillo = 27
pin_verde = 22

# Configuración de la librería GPIO
GPIO.setmode(GPIO.BCM)

# Configuracion de puertos GPIO
GPIO.setup(pin_rojo, GPIO.OUT)
GPIO.setup(pin_amarillo, GPIO.OUT)
GPIO.setup(pin_verde, GPIO.OUT)

def encender_led(pin):
    GPIO.output(pin, GPIO.HIGH)

def apagar_led(pin):
    GPIO.output(pin, GPIO.LOW)

def semaforo():
    try:
        while True:
            # Fase de luz verde
            encender_led(pin_verde)
            time.sleep(5)

            # Fase de luz amarilla
            apagar_led(pin_verde)
            encender_led(pin_amarillo)
            time.sleep(2)

            # Fase de luz roja
            apagar_led(pin_amarillo)
            encender_led(pin_rojo)
            time.sleep(5)

            # Reiniciar ciclo
            apagar_led(pin_rojo)

    except KeyboardInterrupt:
        # Limpiar pines GPIO al interrumpir con Ctrl+C
        GPIO.cleanup()

if __name__ == "__main__":
    semaforo()
list
