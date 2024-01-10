# Bienvenidos a Sys On Chip
# ==============================
# Ejercicio No.2
# En este programa vamos a encender y apagar un led que se encuentra conectado a una raspberry 
# a traves del puuerto GPIO 2. El programa crea una ventana con una etiqueta y dos botones. En
# la etiqueta se muestra el estado del led. El primer botón permite cambiar el estado al led,
# ya sea, de activo a apagado o, viseversa. El segundo botón cierra y finaliza el programa.
# ==============================================================================================

import RPi.GPIO as GPIO     # importa la libreria del GPIO de la raspberry
import time                 # importa la libreria para controlar el reloj
import tkinter as tk        # importa la libreria para crear las ventanas

# Configura el modo de GPIO
GPIO.setmode(GPIO.BCM)

# Define el número del puerto GPIO al que está conectado el LED (en este caso, GPIO2)
led_pin = 2

# Configura el puerto GPIO como salida
GPIO.setup(led_pin, GPIO.OUT)

# Función para cambiar el estado del LED
def toggle_led():
    current_state = GPIO.input(led_pin)
    new_state = not current_state
    GPIO.output(led_pin, new_state)
    update_label()

# Función para actualizar la etiqueta de estado en la ventana
def update_label():
    current_state = GPIO.input(led_pin)
    if current_state:
        label.config(text="Estado del LED: Encendido")
    else:
        label.config(text="Estado del LED: Apagado")

# Configura la ventana Tkinter
root = tk.Tk()
root.title("Control de LED")

# Etiqueta para mostrar el estado del LED
label = tk.Label(root, text="Estado del LED: Apagado", font=("Helvetica", 16))
label.pack(pady=20)

# Botón para cambiar el estado del LED
button = tk.Button(root, text="Cambiar Estado del LED", command=toggle_led, font=("Helvetica", 14))
button.pack(pady=10)

# Botón para salir del programa
exit_button = tk.Button(root, text="Salir", command=root.destroy, font=("Helvetica", 14))
exit_button.pack(pady=10)

try:
    # Bucle principal de la interfaz gráfica
    root.mainloop()

except KeyboardInterrupt:
    # Maneja la interrupción del teclado (Ctrl+C)
    pass

finally:
    # Limpia y apaga el LED al finalizar
    GPIO.cleanup()
    print("GPIO limpio. Programa finalizado.")
