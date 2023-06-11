import os
import guardar_info as db
clear = lambda: os.system('cls')

def register_u():
    clear()
    print("     Registro de usuario ")
    print("")
    usuario = input("nombre de usuario: ")

    if len(usuario) < 1:
        print("ingrese nombre valido")
        input("enter para reintentar")
        clear()
        register_u()

    elif len(usuario) > 20:
        
        print("ingrese un nombre de usuario más corto")
        input("enter para reintentar")
        clear()
        register_u()

    elif db.existe_usuario(usuario):
        print("nombre de usuario existente")
        print("intente otro nombre")
        input("enter para reintentar")
        clear()
        register_u()        
        
    else:
        contraseña = register_p(usuario)
        print("Usuario creado")
        input("Enter para continuar")
        db.registrar_usuario(usuario, contraseña)
        menu_login_register()
        
def register_p(usuario):
    contraseña = input("Ingrese contraseña: ")

    if len(contraseña) < 1:

        print("ingrese contraseña valida")
        input("enter para reintentar")
        clear()
        register_p(usuario)

    elif len(contraseña) > 20:
        
        print("ingrese una contraseña más corta")
        input("enter para reintentar")
        clear()
        register_p(usuario)
        
    else:
        return contraseña

    menu_login_register()

def login_u():

    clear()
    print("     Logueo de usuario ")
    print("")
         
    usuario = input("nombre de usuario: ")

    if db.existe_usuario(usuario):
        login_p(usuario)
        return usuario
        
    else:
        print("Nombre de usuario no encontrado")
        input("enter para reintentar")
        clear()
        login_u()

def login_p(usuario):

    contraseña = input("ingrese su contraseña: ")

    if contraseña == db.leer_usuario(usuario)[1]:
        print("logueo exitoso")

    else:
        print("Contraseña incorrecta")
        input("enter para reintentar")
        clear()
        login_p(usuario)
        
def menu_login_register():
    clear()
    print("Bienvenido al Casino Ulima")
    print("")
    print("1. Registrarse")
    print("2. Iniciar Sesión")
    print("")
    a = int(input("seleccione opción: "))

    if a < 1 or a > 2:
        print('Seleccione una opcion válida')
        input("Enter para reintentar")
        menu_login_register()

    elif a == 1:
        register_u()

    elif a == 2:
        info = login_u()
        return info
    

