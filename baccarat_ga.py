from random import randrange

def crear_barajabaca():
    numeros = ["A",2,3,4,5,6,7,8,9,10,"J","Q","K"]
    baraja = []
    for i in range(len(numeros)):
            baraja.append(str(numeros[i]))
    return baraja

def sacar_carta_aleatoria(baraja):
    aleatorio = randrange(len(baraja))
    carta = baraja.pop(aleatorio)
    return carta

def numero_de_cartabaccarat(carta):
    numero = carta
    if numero == "A":
        return 1
    elif numero == 10:
        return 0
    elif numero == "J":
        return 0
    elif numero == "Q":
        return 0
    elif numero == "K":
        return 0
    else:
        return int(numero)

def baccarat(apuesta):

    baraja_ba = crear_barajabaca()
    jugador_mano = []
    banca_mano = []

    print('>>> BIENVENIDO A BACCARAT <<<')
    print('¿POR QUIEN APOSTARÁ?')
    print('')
    print('1. Jugador')
    print('2. Empate')
    print('3. Banca')
    print('')

    apuest = int(input('>> '))
    

    print('-------------------------------------')
    print('El Crupier sacó las siguientes cartas')
    print('-------------------------------------')
    for i in range(2):
        jugador_mano.append(sacar_carta_aleatoria(baraja_ba))
    for i in range(2):
        banca_mano.append(sacar_carta_aleatoria(baraja_ba))
    print('Mano del jugador: ',jugador_mano)
    print('Mano del banca: ',banca_mano)

    sumajugador = numero_de_cartabaccarat(jugador_mano[0]) + numero_de_cartabaccarat(jugador_mano[1])
    sumabanca = numero_de_cartabaccarat(banca_mano[0]) + numero_de_cartabaccarat(banca_mano[1])

    if sumajugador >= 10:
        sumajugador = sumajugador % 10
    if sumabanca >= 10:
        sumabanca = sumabanca % 10
    print('Puntaje del jugador: ',sumajugador)
    print('Puntaje del banca: ',sumabanca)

    if sumajugador > sumabanca:
            print('-'*30)
            print('   >> Ha ganado el jugador <<')
            print('-'*30)
            print('')
            result = 1
            
    elif sumajugador == sumabanca:
            print('-'*30)
            print("   >> Ha quedado en empate <<")
            print('-'*30)
            result = 2
            

    elif sumajugador < sumabanca:
            print('-'*30)
            print('   >> Ha ganado el banca <<')
            print('-'*30)
            result = 3
            

    if result == apuest:
        print('   >> APUESTA GANADA <<')
        return round(apuesta)
    elif result != apuest:
        print('   >> APUESTA PERDIDA <<')
        return round(apuesta*(-1))

    print("Gracias por jugar")

