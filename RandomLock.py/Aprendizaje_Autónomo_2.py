import random
import string
import getpass
import pyperclip

usuarios = {}

def validar_correo(correo):
    return '@' in correo and correo.endswith('.com')

def generar_contraseña(longitud, incluir_mayusculas, incluir_minusculas, incluir_numeros, incluir_caracteres_especiales):
    caracteres = ""
    if incluir_mayusculas:
        caracteres += string.ascii_uppercase
    if incluir_minusculas:
        caracteres += string.ascii_lowercase
    if incluir_numeros:
        caracteres += string.digits
    if incluir_caracteres_especiales:
        caracteres += string.punctuation

    if not caracteres:
        print("Debes seleccionar al menos un tipo de caracteres.")
        return None

    return ''.join(random.choice(caracteres) for _ in range(longitud))

def registrar_usuario():
    print("---- Registro ----")
    celular = input("Ingresa tu número de celular: ")
    
    while True:
        correo = input("Ingresa tu correo electrónico: ")
        if validar_correo(correo):
            break
        else:
            print("Correo inválido. Asegúrate de que contenga '@' y termine en '.com'.")

    contraseña_maestra = getpass.getpass("Ingresa tu contraseña maestra: ")

    usuarios[celular] = {"correo": correo, "contraseña": contraseña_maestra}
    print("\n¡Registro exitoso!\n")

def recuperar_contraseña_maestra():
    print("---- Recuperar Contraseña ----")
    celular = input("Ingresa tu número de celular: ")
    correo = input("Ingresa tu correo electrónico: ")
    
    if celular in usuarios and usuarios[celular]["correo"] == correo:
        print(f"\nLa contraseña asociada a tu número de celular {celular} es: {usuarios[celular]['contraseña']}")
    else:
        print("\nNúmero de celular o correo incorrecto.")

def iniciar_sesion():
    print("---- Iniciar sesión ----")
    celular = input("Ingresa tu número de celular: ")
    
    if celular in usuarios:
        contraseña = getpass.getpass("Ingresa tu contraseña maestra: ")
        
        if usuarios[celular]["contraseña"] == contraseña:
            print("\n¡Bienvenido a RandomLook!")  
            menu_usuario(celular)
        else:
            print("\nContraseña incorrecta.")
    else:
        print("\nNúmero de celular no registrado.")

def menu_usuario(celular):
    print("\n--- Menú de usuario ---")
    print("1. Ver perfil")
    print("2. Generar contraseña segura")
    print("3. Salir")
    opcion = input("Selecciona una opción: ")
    
    if opcion == "1":
        print(f"Perfil de {celular} - Correo: {usuarios[celular]['correo']}")
    elif opcion == "2":
       
        print("---- Generar Nueva Contraseña ----")
        try:
            longitud = int(input("Ingresa la longitud de la nueva contraseña: "))
            if longitud < 6:
                print("La longitud de la contraseña debe ser al menos 6 caracteres.")
                return
        except ValueError:
            print("Por favor ingresa un número válido para la longitud.")
            return
        
        incluir_mayusculas = input("¿Incluir mayúsculas? (s/n): ").lower() == 's'
        incluir_minusculas = input("¿Incluir minúsculas? (s/n): ").lower() == 's'
        incluir_numeros = input("¿Incluir números? (s/n): ").lower() == 's'
        incluir_caracteres_especiales = input("¿Incluir caracteres especiales? (s/n): ").lower() == 's'
        
        nueva_contraseña = generar_contraseña(longitud, incluir_mayusculas, incluir_minusculas, incluir_numeros, incluir_caracteres_especiales)
        
        if nueva_contraseña:
            print(f"Contraseña generada: {nueva_contraseña}")
            pyperclip.copy(nueva_contraseña) 
            print("La nueva contraseña ha sido copiada al portapapeles.")
    elif opcion == "3":
        print("¡Hasta luego!")
    else:
        print("Opción no válida. Saliendo...")

def menu_principal():
    while True:
        print("\n--- Menú Principal ---")
        print("1. Registrarse")
        print("2. Iniciar sesión")
        print("3. Recuperar contraseña")
        print("4. Salir")
        opcion = input("Selecciona una opción: ")

        if opcion == "1":
            registrar_usuario()
        elif opcion == "2":
            iniciar_sesion()
        elif opcion == "3":
            recuperar_contraseña_maestra()
        elif opcion == "4":
            print("¡Hasta luego!")
            break
        else:
            print("Opción no válida. Inténtalo de nuevo.")

menu_principal()