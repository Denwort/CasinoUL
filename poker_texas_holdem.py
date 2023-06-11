import login_y_register
import os
import guardar_info as db
from random import randrange
import evaluar_valores_final

clear = lambda: os.system('cls')

def crear_baraja():
    palos = ["♠", "♥", "♦", "♣"]
    numeros = ["A",2,3,4,5,6,7,8,9,10,"J","Q","K"]
    baraja = []
    for i in range(len(palos)):
        for j in range(len(numeros)):
            baraja.append(str(numeros[j])+ palos[i])
    return baraja

def sacar_carta_aleatoria(baraja):
    aleatorio = randrange(len(baraja))
    carta = baraja.pop(aleatorio)
    return carta

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

def obtener_valor(carta):

    if carta == "A":

        return 1

    if carta == "K":

        return 13

    elif carta == "Q":

        return 12

    elif carta == "J":

        return 11

    else:

        return int(carta)

def aumentar_apuesta(user_usuario, apuesta):
    print('--------------subir apuesta-----------------')
    print('1.subir apuesta (saldo:', int(db.leer_usuario(user_usuario)[2]), "fichas)" )
    print('2.mantener apuesta')
    print('3.retirarse')
    opcion=int(input('elija una opcion: '))
    if opcion==1:
        aumento_de_apuesta=int(input('cantidad a subir (numero entero): '))
        aumento_auxiliar = aumento_de_apuesta+apuesta
        if db.acepta_apuesta(user_usuario, aumento_auxiliar):
            suma_final=aumento_de_apuesta+apuesta
            print('Apuesta actual: ',suma_final)
            apuesta=suma_final
            return round(apuesta)
        else:
            print("Apuesta no aceptada, saldo insuficiente")
            aumentar_apuesta(user_usuario, apuesta)
        
    elif opcion==2:
        print('sigue el juego')
        print('--------------------------------------------------------')
        
    elif opcion==3:
        print('fin del juego')
        print('--------------------------------------------------------')
        apuesta = apuesta * (-1)
        print(apuesta)
        return round(apuesta)

    else:
        print('-----------------------error-----------------------------')

    return round(apuesta)    

def poker_texas(user_usuario, apuesta):

    baraja = crear_baraja()
    mano_jugador= []
    mano_mesa_completa=[]
    mano_mesa_falso=[]
    mano_bot=[]

    for i in range(5):
        mano_mesa_completa.append(sacar_carta_aleatoria(baraja))
    for b in range(2):
        mano_jugador.append(sacar_carta_aleatoria(baraja))
    for c in range(2):
        mano_bot.append(sacar_carta_aleatoria(baraja))
    
    print() 
    print("Apuesta inicial:", apuesta)

    for a in range (1):
        mano_mesa_falso.append(mano_mesa_completa)
    for f in range (1):
        mano_mesa_completa.pop()
        mano_mesa_completa.pop()

        print('mesa: ', mano_mesa_completa  )
    for b in range (1):
        
        print('tu mano es: ', mano_jugador)

    apuesta=aumentar_apuesta(user_usuario, apuesta)
    
    if apuesta >= 0:
        for a in range (1):
            mano_mesa_completa.insert(3,sacar_carta_aleatoria(baraja))
        print()
        print('mesa: ', mano_mesa_completa  )
        for b in range (1):
            
            print('tu mano es: ', mano_jugador)
    else:
        print("Te has rendido. Fin del juego. Pierdes: ", apuesta, "fichas.")
        return round(apuesta)

    apuesta=aumentar_apuesta(user_usuario, apuesta)


    if apuesta >= 0:
        for a in range (1):
            mano_mesa_completa.insert(4,sacar_carta_aleatoria(baraja))
        
        print()
        print('mesa: ', mano_mesa_completa  )
        for b in range (1):
            
            print('tu mano es: ', mano_jugador)
            print('La mano del bot es: ', mano_bot)
    else:
        print("Te has rendido. Fin del juego. Pierdes: ", apuesta, "fichas.")
        return round(apuesta)

    resjugador=evaluar_valores_final.evaluar_mano(mano_jugador,mano_mesa_completa)
    resbot=evaluar_valores_final.evaluar_mano(mano_bot,mano_mesa_completa)

    print()
    resapuesta=0
    if resjugador[0] > resbot[0]:
        print("GANASTE")
        resapuesta=apuesta
        print('has ganado', resapuesta, 'fichas')

    elif resjugador[0] < resbot[0]:
        print("PERDISTE")
        resapuesta=apuesta*-1
        print('has perdido', resapuesta, 'fichas')
    else:
        if resjugador[1] > resbot[1]:
            print("YO GANO CON EL MISMO GRUPO PERO MAYOR CARTA")
            resapuesta=apuesta
            print('has ganado', resapuesta, 'fichas')
        elif resjugador[1] < resbot[1]:
            print("PERDISTE POR EL MISMO GRUPO PERO MENOR CARTA")
            resapuesta=apuesta*-1
            print('has perdido', resapuesta, 'fichas')
        else:
            print("EMPATE")
            resapuesta=0
            print('No has perdido ni ganado ninguna ficha')
    
    return round(resapuesta)
