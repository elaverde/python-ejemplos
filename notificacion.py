import os
from win10toast import ToastNotifier

def notificacion():
    
    toast = ToastNotifier() # Instaciamos el objeto de ToastNotifier
    title = "Python"  # Definimos nuestro titulo
    message = "Hola mundo :)" #Definimos nuestro mensaje
    # Establecemos nuestro icono
    icon = "mi.ico"
    length = 30
    toast.show_toast(title, message, icon_path=icon, duration=length)

notificacion()