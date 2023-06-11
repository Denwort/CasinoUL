
def leer_usuario(usuario):
    ubicacion_archivo = "db.txt"
    separador_general = "@"
    separador_entre_partidas = "/"
    separador_entre_info_partidas = "_"

    # Abre archivo
    db = open(ubicacion_archivo, "r")
    
    # Buscar la linea del usuario

    lineas = db.readlines()

    
    n_linea = -1
    for i in range(len(lineas)):
        palabras = lineas[i].split(separador_general)
        if palabras[0] == usuario:
            n_linea = i

    # Capturar la lista de partidas del usuario
    info_usuario = lineas[n_linea]
    datos = info_usuario.split(separador_general)
    user = datos[0]
    password = datos[1]
    saldo = int(datos[2])
    partidas_str = datos[3]
    partidas_list_str = partidas_str.split(separador_entre_partidas)
    partidas = []
    for partida in partidas_list_str:
        partidas.append(partida.split(separador_entre_info_partidas))

    db.close()
    return [user, password, saldo, partidas]

def existe_usuario(usuario):
    ubicacion_archivo = "db.txt"
    separador_general = "@"
    encontrado = False

    db = open(ubicacion_archivo, "r")

    lineas = db.readlines()

    for linea in lineas:
        if linea.split(separador_general)[0] == usuario:
            encontrado = True

    db.close()

    return encontrado

def registrar_usuario(usuario, contraseña):
    ubicacion_destino = "db.txt"    
    separador_general = "@"
    saldo_de_cuenta_nueva = 0

    db = open(ubicacion_destino, "a")

    nueva_linea = usuario + separador_general + contraseña + separador_general + str(saldo_de_cuenta_nueva) + separador_general

    db.write("\n" + nueva_linea)

    leer = open(ubicacion_destino, "r")

    db.close()
    leer.close()

def cambiar_saldo(usuario, aumento_o_disminucion):
    ubicacion_archivo = "db.txt"
    ubicacion_destino = "db.txt"
    separador_general = "@"

    # Abre archivo
    db = open(ubicacion_archivo, "r")
    
    # Buscar la linea del usuario

    lineas = db.readlines()

    n_linea = -1
    for i in range(len(lineas)):
        palabras = lineas[i].split(separador_general)
        if palabras[0] == usuario:
            n_linea = i

    # Capturar la lista de partidas del usuario
    info_usuario = lineas[n_linea]
    datos = info_usuario.split(separador_general)
    user = datos[0]
    password = datos[1]
    saldo = int(datos[2])
    partidas_str = datos[3]
    db.close()

    saldo = round(saldo + aumento_o_disminucion)

    escritura = open(ubicacion_destino, "w")

    lineas[n_linea] = user + separador_general + password + separador_general + str(saldo) + separador_general + partidas_str

    for linea in lineas:
        escritura.write(linea)

    escritura.close()

def agregar_partida(usuario, cod_juego, num_partida, resultado):
    ubicacion_archivo = "db.txt"
    ubicacion_destino = "db.txt"
    separador_general = "@"
    separador_entre_partidas = "/"
    separador_entre_info_partidas = "_"

    # Abre archivo
    db = open(ubicacion_archivo, "r")
    
    # Informacion a añadir de la nueva partida
    nueva_info = cod_juego + separador_entre_info_partidas + str(num_partida) + separador_entre_info_partidas + str(resultado)

    # Buscar la linea del usuario

    lineas = db.readlines()

    n_linea = -1
    for i in range(len(lineas)):
        palabras = lineas[i].split(separador_general)
        if palabras[0] == usuario:
            n_linea = i

    # Capturar la lista de partidas del usuario
    info_usuario = lineas[n_linea]
    datos = info_usuario.split(separador_general)
    user_pass_saldo = datos[0] + separador_general + datos[1] + separador_general + datos[2]
    partidas_str = datos[3]
    partidas_list_str = partidas_str.split(separador_entre_partidas)

    # Agregar nuevo registro a la lista de partidas (quitando el salto de linea)
    if len(partidas_list_str) < 10:
        partidas_list_str[len(partidas_list_str)-1] = partidas_list_str[len(partidas_list_str)-1][:-1]
        partidas_list_str.append(nueva_info)
    elif len(partidas_list_str) == 10:
        partidas_list_str.pop(0)
        partidas_list_str[len(partidas_list_str)-1] = partidas_list_str[len(partidas_list_str)-1][:-1]
        partidas_list_str.append(nueva_info)
    else:
        partidas_list_str.append("EXCESO: MAS DE 5 PARTIDAS ALMACENADAS")

    # Escribir la linea del usuario con el nuevo registro agregado
    linea_final = user_pass_saldo + separador_general
    for i in range(len(partidas_list_str)):
        partida_str = str(partidas_list_str[i])
        linea_final+= (partida_str)
        if i < len(partidas_list_str)-1:
            linea_final+=separador_entre_partidas
        else:
            linea_final+="\n"

    # Reescribir la linea en el txt

    lineas[n_linea] = linea_final

    edit = open(ubicacion_destino, "w")

    for linea in lineas:
        edit.write(linea)

    db.close()
    edit.close()

def acepta_apuesta(usuario, apuesta):
    aceptacion = False
    if apuesta > int(leer_usuario(usuario)[2]):
        print("No cuenta con saldo suficiente para apostar")
        print("")
        print("Compre más fichas en nuestra tienda virtual")
        input("")
        print("enter para continuar")
    
    elif apuesta == int(leer_usuario(usuario)[2]):
        print("Está apostando todas sus fichas")
        input("enter para continuar")
        aceptacion = True

    elif apuesta < int(leer_usuario(usuario)[2]):
        if apuesta > 0:
            print("Apuesta aceptada")
            aceptacion = True
        else:
            print("La apuesta no puede ser cero")
    return aceptacion
