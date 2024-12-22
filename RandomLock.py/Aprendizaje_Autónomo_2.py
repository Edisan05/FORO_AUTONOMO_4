# Importación de módulos necesarios

import random  # Para generar números aleatorios (utilizados en contraseñas)
import string  # Para acceder a caracteres como mayúsculas, minúsculas, dígitos y caracteres especiales
import getpass  # Para ingresar contraseñas de manera segura (sin que se muestren en pantalla)
import pyperclip  # Para copiar contraseñas generadas al portapapeles

# Diccionarios para almacenar usuarios y contraseñas generadas

usuarios = {}  # Almacena los usuarios registrados con su correo y contraseña maestra
contraseñas_generadas = {}  # Almacena las contraseñas generadas para los usuarios

# Función para validar el formato del correo electrónico
def validar_correo(correo):
    # Verifica si el correo tiene el carácter '@' y termina en '.com' o '.COM'
    return '@' in correo and (correo.endswith('.com') or correo.endswith('.COM'))

# Función para generar contraseñas seguras
def generar_contraseña(longitud, incluir_mayusculas, incluir_minusculas, incluir_numeros, incluir_caracteres_especiales):
    caracteres = ""  # Inicializamos una variable para almacenar los tipos de caracteres que se usarán
    if incluir_mayusculas:
        caracteres += string.ascii_uppercase  # Añade mayúsculas
    if incluir_minusculas:
        caracteres += string.ascii_lowercase  # Añade minúsculas
    if incluir_numeros:
        caracteres += string.digits  # Añade números
    if incluir_caracteres_especiales:
        caracteres += string.punctuation  # Añade caracteres especiales
    
    # Si no se seleccionó ningún tipo de caracteres, muestra un error y retorna None
    if not caracteres:
        print("Debes seleccionar al menos un tipo de caracteres.")
        return None

    # Genera y retorna la contraseña aleatoria utilizando los caracteres seleccionados
    return ''.join(random.choice(caracteres) for _ in range(longitud))

# Función para registrar un nuevo usuario
def registrar_usuario():
    print("---- Registro ----")
    celular = input("Ingresa tu número de celular: ")  # Solicita el número de celular
    
    # Validación del correo electrónico
    while True:
        correo = input("Ingresa tu correo electrónico: ")
        if validar_correo(correo):
            break  # Si el correo es válido, sale del bucle
        else:
            print("Correo inválido. Asegúrate de que contenga '@' y termine en '.com'.")

    # Solicita la contraseña maestra de forma segura
    contraseña_maestra = getpass.getpass("Ingresa tu contraseña maestra: ")

    # Almacena la información del usuario en el diccionario
    usuarios[celular] = {"correo": correo, "contraseña": contraseña_maestra}
    print("\n¡Registro exitoso!\n")

# Función para recuperar la contraseña maestra
def recuperar_contraseña_maestra():
    print("---- Recuperar Contraseña ----")
    celular = input("Ingresa tu número de celular: ")
    correo = input("Ingresa tu correo electrónico: ")
    
    # Verifica si el celular y correo coinciden con los registrados
    if celular in usuarios and usuarios[celular]["correo"] == correo:
        print(f"\nLa contraseña asociada a tu número de celular {celular} es: {usuarios[celular]['contraseña']}")
    else:
        print("\nNúmero de celular o correo incorrecto.")

# Función para iniciar sesión
def iniciar_sesion():
    print("---- Iniciar sesión ----")
    celular = input("Ingresa tu número de celular: ")
    
    # Verifica si el celular está registrado
    if celular in usuarios:
        contraseña = getpass.getpass("Ingresa tu contraseña maestra: ")  # Solicita la contraseña
        
        # Verifica si la contraseña ingresada es correcta
        if usuarios[celular]["contraseña"] == contraseña:
            print("\n¡Bienvenido a RandomLook!")  
            menu_usuario(celular)  # Llama al menú del usuario
        else:
            print("\nContraseña incorrecta.")
    else:
        print("\nNúmero de celular no registrado.")

# Función para mostrar el menú principal del usuario después de iniciar sesión
def menu_usuario(celular):
    while True:
        print("\n--- Menú de usuario ---")
        print("1. Ver perfil")
        print("2. Generar contraseña segura")
        print("3. Salir")
        opcion = input("Selecciona una opción: ")
        
        # Opción para ver el perfil del usuario
        if opcion == "1":
            print(f"Perfil de {celular} - Correo: {usuarios[celular]['correo']}")
        # Opción para generar una nueva contraseña segura
        elif opcion == "2":
            sub_menu_contraseñas()
        # Opción para salir del menú de usuario
        elif opcion == "3":
            print("¡Hasta luego!")
            break
        else:
            print("Opción no válida. Inténtalo de nuevo.")

# Submenú para manejar las contraseñas generadas
def sub_menu_contraseñas():
    while True:
        print("\n--- Menú de Contraseñas Seguras ---")
        print("1. Generar nueva contraseña")
        print("2. Ver contraseñas generadas")
        print("3. Salir")
        opcion = input("Selecciona una opción: ")
        
        # Opción para generar y almacenar una nueva contraseña
        if opcion == "1":
            generar_y_almacenar_contraseña()
        # Opción para ver las contraseñas generadas
        elif opcion == "2":
            ver_contraseñas_generadas()
        # Opción para salir del submenú
        elif opcion == "3":
            break
        else:
            print("Opción no válida. Inténtalo de nuevo.")

# Función para generar y almacenar una nueva contraseña segura
def generar_y_almacenar_contraseña():
    print("---- Generar Nueva Contraseña ----")
    try:
        longitud = int(input("Ingresa la longitud de la nueva contraseña: "))
        if longitud < 6:
            print("La longitud de la contraseña debe ser al menos 6 caracteres.")
            return
    except ValueError:
        print("Por favor ingresa un número válido para la longitud.")
        return
    
    # Solicita al usuario si desea incluir diferentes tipos de caracteres
    incluir_mayusculas = input("¿Incluir mayúsculas? (s/n): ").lower() == 's'
    incluir_minusculas = input("¿Incluir minúsculas? (s/n): ").lower() == 's'
    incluir_numeros = input("¿Incluir números? (s/n): ").lower() == 's'
    incluir_caracteres_especiales = input("¿Incluir caracteres especiales? (s/n): ").lower() == 's'
    
    # Solicita el destinatario de la contraseña generada
    destinatario = input("¿Para quién generaste esta contraseña?: ")
    
    # Genera la contraseña utilizando los parámetros ingresados
    nueva_contraseña = generar_contraseña(longitud, incluir_mayusculas, incluir_minusculas, incluir_numeros, incluir_caracteres_especiales)
    
    # Si la contraseña fue generada exitosamente, la muestra y la copia al portapapeles
    if nueva_contraseña:
        print(f"Contraseña generada para {destinatario}: {nueva_contraseña}")
        pyperclip.copy(nueva_contraseña)  # Copia la contraseña al portapapeles
        print("La nueva contraseña ha sido copiada al portapapeles.")
        
        # Pregunta si desea almacenar la contraseña generada
        almacenar = input("¿Quieres almacenar esta contraseña? (s/n): ").lower() == 's'
        
        if almacenar:
            contraseñas_generadas[destinatario] = nueva_contraseña  # Almacena la contraseña en el diccionario
            print(f"La contraseña ha sido almacenada para {destinatario}.")

# Función para ver las contraseñas generadas y almacenadas
def ver_contraseñas_generadas():
    print("\n--- Contraseñas Generadas ---")
    if contraseñas_generadas:
        # Muestra todas las contraseñas almacenadas
        for destinatario, contraseña in contraseñas_generadas.items():
            print(f"{destinatario}: {contraseña}")
    else:
        print("No hay contraseñas generadas almacenadas.")

# Menú principal donde el usuario puede registrarse, iniciar sesión o recuperar su contraseña
def menu_principal():
    while True:
        print("\n--- Menú Principal ---")
        print("1. Registrarse")
        print("2. Iniciar sesión")
        print("3. Recuperar contraseña")
        print("4. Salir")
        opcion = input("Selecciona una opción: ")

        # Opción para registrar un nuevo usuario
        if opcion == "1":
            registrar_usuario()
        # Opción para iniciar sesión con una cuenta registrada
        elif opcion == "2":
            iniciar_sesion()
        # Opción para recuperar la contraseña maestra
        elif opcion == "3":
            recuperar_contraseña_maestra()
        # Opción para salir del programa
        elif opcion == "4":
            print("¡Hasta luego!")
            break
        else:
            print("Opción no válida. Inténtalo de nuevo.")

# Ejecuta el menú principal
menu_principal()

