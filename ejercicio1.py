# Bienvenidos a Sys On Chip
# ==============================
# Ejercicio No.1
# En este programa vamos a encender y apagar un led que se encuentra conectado a una raspberry 
# a traves del puuerto GPIO 2. A traves de un bucle infinito donde se controla el encendido
# y apagado del led para que emita luz intermitentemente
# ==============================================================================================

import RPi.GPIO as GPIO
import time

# Configura el modo de GPIO
GPIO.setmode(GPIO.BCM)

# Define el número del puerto GPIO al que está conectado el LED (en este caso, GPIO2)
led_pin = 2

# Configura el puerto GPIO como salida
GPIO.setup(led_pin, GPIO.OUT)

# Ingresa a un bucle infinito hasta que ocurra una interrupción de teclado (Ctrl+C)
try:
    while True:
        # Enciende el LED
        print("Encendiendo el LED...")
        GPIO.output(led_pin, GPIO.HIGH)
        time.sleep(1)  

        # Apaga el LED
        print("Apagando el LED...")
        GPIO.output(led_pin, GPIO.LOW)
        time.sleep(1)  

except KeyboardInterrupt:
    # Maneja la interrupción del teclado (Ctrl+C)
    pass

finally:
    # Limpia y apaga el LED al finalizar
    GPIO.cleanup()
    print("GPIO limpio. Programa finalizado.")
