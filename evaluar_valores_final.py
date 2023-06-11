
def numero_de_carta(carta):
    numero = carta[-2]
    if numero == "A":
        return 1
    elif numero == "0":
        return 10
    elif numero == "J":
        return 11
    elif numero == "Q":
        return 12
    elif numero == "K":
        return 13
    else:
        return int(numero)

def palo_de_carta(carta):
    palo = carta[-1]
    return palo

def pk_escalera_real(mano):
    lo_tiene = True
    diff = 0
    palos = {"treboles":[],"espadas":[],"corazones":[],"diamantes":[]}
    palo_elegido = ""
    cartas_escogidas = []
    for i in range(len(mano)):
        if palo_de_carta(mano[i]) == "♣":
            palos["treboles"].append(mano[i])
        elif palo_de_carta(mano[i]) == "♠":
            palos["espadas"].append(mano[i])
        elif palo_de_carta(mano[i]) == "♥":
            palos["corazones"].append(mano[i])
        elif palo_de_carta(mano[i]) == "♦":
            palos["diamantes"].append(mano[i])

    for clave in palos.keys():
        if len(palos[clave]) >= 5:
            palo_elegido = clave

    if palo_elegido in palos.keys():
        cartas_maximas = palos[palo_elegido]
    else:
        lo_tiene = False
        return [lo_tiene, diff]

    objetivo = [False, False, False, False, False]

    for i in range(len(cartas_maximas)):
        n = numero_de_carta(cartas_maximas[i])
        if n == 10:
            objetivo[0] = True
        elif n == 11:
            objetivo[1] = True
        elif n == 12:
            objetivo[2] = True
        elif n == 13:
            objetivo[3] = True
        elif n == 1:
            objetivo[4] = True
    
    for i in range(len(objetivo)):
        if objetivo[i] == False:
            lo_tiene = False

    return [lo_tiene, diff]

def pk_escalera_de_color(mano):
    lo_tiene = False
    diff = 0
    palos = {"treboles":[],"espadas":[],"corazones":[],"diamantes":[]}
    palo_elegido = ""
    cartas_escogidas = []
    for i in range(len(mano)):
        if palo_de_carta(mano[i]) == "♣":
            palos["treboles"].append(mano[i])
        elif palo_de_carta(mano[i]) == "♠":
            palos["espadas"].append(mano[i])
        elif palo_de_carta(mano[i]) == "♥":
            palos["corazones"].append(mano[i])
        elif palo_de_carta(mano[i]) == "♦":
            palos["diamantes"].append(mano[i])

    # Busca si alguno es mayor de 5
    for clave in palos.keys():
        if len(palos[clave]) >= 5:
            palo_elegido = clave

    # Si algun palo supera las 5 cartas, hace lo de dentro del if
    if palo_elegido in palos.keys():
        cartas_maximas = palos[palo_elegido]
    else:
        lo_tiene = False
        return [lo_tiene, diff]
    
    numeros = []

    for i in range(len(cartas_maximas)):
        numeros.append(numero_de_carta(cartas_maximas[i]))

    # BUSQUEDA!!!
    numeros.sort()

    def comparar_5(lista_de_5):
        seguidos = True
        for i in range(len(lista_de_5)-1):
            if lista_de_5[i] + 1 != lista_de_5[i+1]:
                seguidos = False
        return seguidos

    def hallar_maximo_5(lista_de_5):
        mayor = lista_de_5[0]
        for i in range(len(lista_de_5)):
            if lista_de_5[i] > mayor:
                mayor = lista_de_5[i]
        return mayor

    # Compara casos de 5 cartas, 6 o 7

    if len(numeros) == 5:
        if comparar_5(numeros):
            lo_tiene = True
            diff = hallar_maximo_5(numeros)

    elif len(numeros) == 6:
        if numeros[1] + 1 == numeros[2]:
            if comparar_5(numeros[1:6]):
                lo_tiene = True
                diff = hallar_maximo_5(numeros[1:6])
        elif numeros[0] + 1 == numeros[1]:
            if comparar_5(numeros[0:5]):
                lo_tiene = True
                diff = hallar_maximo_5(numeros[0:5])
                
        

    elif len(numeros) == 7:
        if numeros[2] + 1 == numeros[3]:
            if comparar_5(numeros[2:7]):
                lo_tiene = True
                diff = hallar_maximo_5(numeros[2:7])
        elif numeros[1] + 1 == numeros[2]:
            if comparar_5(numeros[1:6]):
                lo_tiene = True
                diff = hallar_maximo_5(numeros[1:6])
        elif numeros[0] + 1 == numeros[1]:
            if comparar_5(numeros[0:5]):
                lo_tiene = True
                diff = hallar_maximo_5(numeros[0:5])
        
    
    return [lo_tiene, diff]

def pk_poker(cartas):
    lotiene=False
    diff=0
    #pasar de strg a numeros
    numeros = []

    for i in range(len(cartas)):
        numeros.append(numero_de_carta(cartas[i]))

    numeros.sort()
    
    #diccionario con los clave=numero y valor= n repeticiones
    cartas_y_repeticiones = {}
    for i in range(len(numeros)):
        cartas_y_repeticiones[numeros[i]]=1
        for j in range(len(numeros)):
            if i != j:
                if numeros [i] == numeros[j]:
                    cartas_y_repeticiones[numeros[i]]+=1
    
    #seoarando pares
    pares=[]
    for i in (cartas_y_repeticiones.keys()):
        carta=i
        repeticiones=cartas_y_repeticiones[i]
        if repeticiones == 4:
            pares.append(carta)
            lotiene=True
            diff=carta

    
    # consideraciones
    return [lotiene, diff]

def pk_full(cartas):
    # Trio + doble

    lotiene=False
    diff=0
    #pasar de strg a numeros
    numeros = []

    for i in range(len(cartas)):
        numeros.append(numero_de_carta(cartas[i]))

    numeros.sort()
    
    #diccionario con los clave=numero y valor= n repeticiones
    cartas_y_repeticiones = {}
    for i in range(len(numeros)):
        cartas_y_repeticiones[numeros[i]]=1
        for j in range(len(numeros)):
            if i != j:
                if numeros [i] == numeros[j]:
                    cartas_y_repeticiones[numeros[i]]+=1
    
    #seoarando pares
    
    pares=[]
    trios=[]
    for i in (cartas_y_repeticiones.keys()):
        carta=i
        repeticiones=cartas_y_repeticiones[i]
        if repeticiones == 2:
            pares.append(carta)
        elif repeticiones == 3:
            trios.append(carta)

    # Consideracion de caso 2 trios en el que un trio va a ser considerado como un par
    if len(trios) == 2:
        trios.sort()
        pares.append(trios[0])
        trios.pop(0)

    # Hallando si tiene trio + par
    if len(pares) > 0 and len(trios) > 0:
        lotiene = True
        # hallar diff
        diff = trios[0]
        return [lotiene, diff]

    else:
        return [False, 0]

def pk_color(mano):
    pass
    # Lo mismo que el inicio de escalera_real
    # Si alguna lista de algun palo tiene cartas >=5, lo_tiene = True diff=mayor
    lo_tiene = False
    diff = 0

    # Ordenar las cartas de acuerdo a sus palos
    palos = {"treboles":[],"espadas":[],"corazones":[],"diamantes":[]}
    palo_elegido = ""
    for i in range(len(mano)):
        if palo_de_carta(mano[i]) == "♣":
            palos["treboles"].append(mano[i])
        elif palo_de_carta(mano[i]) == "♠":
            palos["espadas"].append(mano[i])
        elif palo_de_carta(mano[i]) == "♥":
            palos["corazones"].append(mano[i])
        elif palo_de_carta(mano[i]) == "♦":
            palos["diamantes"].append(mano[i])

    # Busca si algun palo tiene mas de 5 cartas
    for clave in palos.keys():
        if len(palos[clave]) >= 5:
            palo_elegido = clave
            lo_tiene = True
    
    if lo_tiene == True:
        # Busca el diff
        cartas_maximas = palos[palo_elegido]

        numeros = []

        for i in range(len(cartas_maximas)):
            numeros.append(numero_de_carta(cartas_maximas[i]))

        # BUSQUEDA!!!
        numeros.sort()

        carta_mayor=numeros[0]
        
        for i in range (len(numeros)):
            if numeros[i] > carta_mayor:
                carta_mayor=numeros[i]
        
        diff = carta_mayor

        return [True, diff]

    else:
        return [False, 0]

def pk_escalera(cartas):
    # Sacar lista de numeros
    # Compara casos de 5, 6 o 7 cartas (escalera_de_color)
    lo_tiene = False
    diff = 0
    
    numeros_con_duplicados = []

    for i in range(len(cartas)):
        numeros_con_duplicados.append(numero_de_carta(cartas[i]))

    # BUSQUEDA!!!
    numeros_con_duplicados.sort()

    numeros = list(set(numeros_con_duplicados))


    #Compara si las 5 cartas introducidas son consecutivas
    def comparar_5(lista_de_5):
        seguidos = True
        for i in range(len(lista_de_5)-1):
            if lista_de_5[i] + 1 != lista_de_5[i+1]:
                seguidos = False
        return seguidos

    #Halla la carta máxima de las 5 cartas introducidas
    def hallar_maximo_5(lista_de_5):
        mayor = lista_de_5[0]
        for i in range(len(lista_de_5)):
            if lista_de_5[i] > mayor:
                mayor = lista_de_5[i]
        return mayor

    # Compara casos de 5 cartas, 6 o 7

    if len(numeros) == 5:
        if comparar_5(numeros):
            lo_tiene = True
            diff = hallar_maximo_5(numeros)

    elif len(numeros) == 6:
        if numeros[1] + 1 == numeros[2]:
            if comparar_5(numeros[1:6]):
                lo_tiene = True
                diff = hallar_maximo_5(numeros[1:6])
        elif numeros[0] + 1 == numeros[1]:
            if comparar_5(numeros[0:5]):
                lo_tiene = True
                diff = hallar_maximo_5(numeros[0:5])
                
        
    elif len(numeros) == 7:
        if numeros[2] + 1 == numeros[3]:
            if comparar_5(numeros[2:7]):
                lo_tiene = True
                diff = hallar_maximo_5(numeros[2:7])
        elif numeros[1] + 1 == numeros[2]:
            if comparar_5(numeros[1:6]):
                lo_tiene = True
                diff = hallar_maximo_5(numeros[1:6])
        elif numeros[0] + 1 == numeros[1]:
            if comparar_5(numeros[0:5]):
                lo_tiene = True
                diff = hallar_maximo_5(numeros[0:5])
        
    
    return [lo_tiene, diff]

def pk_trio(cartas):
    lotiene=False
    diff=0
    #pasar de strg a numeros
    numeros = []

    for i in range(len(cartas)):
        numeros.append(numero_de_carta(cartas[i]))

    numeros.sort()
    
    #diccionario con los clave=numero y valor= n repeticiones
    cartas_y_repeticiones = {}
    for i in range(len(numeros)):
        cartas_y_repeticiones[numeros[i]]=1
        for j in range(len(numeros)):
            if i != j:
                if numeros [i] == numeros[j]:
                    cartas_y_repeticiones[numeros[i]]+=1
    
    #seoarando pares
    trios=[]
    for i in (cartas_y_repeticiones.keys()):
        carta=i
        repeticiones=cartas_y_repeticiones[i]
        if repeticiones == 3:
            trios.append(carta)
            lotiene=True
    
    if len(trios) > 0:
        cartamatoy=trios[0]
        for i in range (len(trios)):
            if trios[i] > cartamatoy:
                cartamatoy=trios[i]
                diff=cartamatoy
    
        return [lotiene, diff]
    
    else:
        return [False, 0]
             
def pk_doble_pareja(cartas):
    lotiene=False
    diff=0
    #pasar de strg a numeros
    numeros = []

    for i in range(len(cartas)):
        numeros.append(numero_de_carta(cartas[i]))

    numeros.sort()
    
    #diccionario con los clave=numero y valor= n repeticiones
    cartas_y_repeticiones = {}
    for i in range(len(numeros)):
        cartas_y_repeticiones[numeros[i]]=1
        for j in range(len(numeros)):
            if i != j:
                if numeros [i] == numeros[j]:
                    cartas_y_repeticiones[numeros[i]]+=1
    
    #seoarando pares
    pares=[]
    for i in (cartas_y_repeticiones.keys()):
        carta=i
        repeticiones=cartas_y_repeticiones[i]
        if repeticiones == 2:
            pares.append(carta)


    if len(pares) >= 2:
        lotiene = True
    else:
        return [False, 0]

    # consideraciones

    cartamatoy=pares[0]
    
    #carta mayor
    for i in range (1,len(pares)):
        if pares[i] > cartamatoy:
            cartamatoy=pares[i]
            diff=cartamatoy
   
    return [lotiene, diff]  

def pk_pareja(cartas):
    lotiene=False
    diff=0
    #pasar de strg a numeros
    numeros = []

    for i in range(len(cartas)):
        numeros.append(numero_de_carta(cartas[i]))

    numeros.sort()
    
    #diccionario con los clave=numero y valor= n repeticiones
    cartas_y_repeticiones = {}
    for i in range(len(numeros)):
        cartas_y_repeticiones[numeros[i]]=1
        for j in range(len(numeros)):
            if i != j:
                if numeros [i] == numeros[j]:
                    cartas_y_repeticiones[numeros[i]]+=1
    
    #seoarando pares
    pares=[]
    for i in (cartas_y_repeticiones.keys()):
        carta=i
        repeticiones=cartas_y_repeticiones[i]
        if repeticiones == 2:
            pares.append(carta)
            lotiene=True
            diff=carta

    
    # consideraciones
    return [lotiene, diff]
    
def pk_carta_alta(cartas):
    numeros = []

    for i in range(len(cartas)):
        numeros.append(numero_de_carta(cartas[i]))

    numeros.sort()
    cartamatoy=numeros[0]
    
    for i in range (1,len(numeros)):
        if numeros[i] > cartamatoy:
            cartamatoy=numeros[i]
    return True ,cartamatoy

def evaluar_mano(mano, mesa):
    mano_completa = mano + mesa
    categoria = 0 
    diff = 0
    if pk_escalera_real(mano_completa)[0]:
        diff = pk_escalera_real(mano_completa)[1]
        categoria = 9
    elif pk_escalera_de_color(mano_completa)[0]:
        diff = pk_escalera_de_color(mano_completa)[1]
        categoria = 8
    elif pk_poker(mano_completa)[0]:
        diff = pk_poker(mano_completa)[1]
        categoria = 7
    elif pk_full(mano_completa)[0]:
        diff = pk_full(mano_completa)[1]
        categoria = 6
    elif pk_color(mano_completa)[0]:
        diff = pk_color(mano_completa)[1]
        categoria = 5
    elif pk_escalera(mano_completa)[0]:
        diff = pk_escalera(mano_completa)[1]
        categoria = 4
    elif pk_trio(mano_completa)[0]:
        diff = pk_trio(mano_completa)[1]
        categoria = 3
    elif pk_doble_pareja(mano_completa)[0]:
        diff = pk_doble_pareja(mano_completa)[1]
        categoria = 2
    elif pk_pareja(mano_completa)[0]:
        diff = pk_pareja(mano_completa)[1]
        categoria = 1
    elif pk_carta_alta(mano_completa)[0]:
        diff = pk_carta_alta(mano_completa)[1]
        categoria = 0
    return [categoria, diff]


