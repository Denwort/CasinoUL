def tutorial_baccarat():
    print('-----------------REGLAS----------------')
    print('1) El juego consiste en apostar por un ganador: "jugador" , "banca" o "empate"')
    print('2) Las cartas en Baccarat tienen un valor peculiar:')
    print(  '2.1) La carta A vale 1 punto')
    print(  '2.2) Las cartas del 2 al 9 valen el mismo puntaje que indica el numero')
    print(  '2.3) Las cartas "10", "J" , "Q" , "k", valen 0 puntos')
    print('3) El Crupier repartira dos cartas al azar al jugador y al banca')
    print('4) Si los puntajes sumados de cada carta es mayor que 9, se resta 10 al puntaje')
    print('5) El que tenga mayor puntaje gana la ronda, a menos que quede en empate')
    print('6) El usuario gana su apuesta dependiendo a que opcion aposto')
    input("Enter para volver")

def tutorial_pkt():
    print('---------------------------------------REGLAS--------------------------------------------------------')
    print('1) El juego comienza revelando las cartas de la mano y las de la mesa')
    print('2) Apartir de este momento se da una eleccion entre mantener tu apuesta, aumentar tu apuesta ')
    print('   o rendirte en caso de irte solo perderas la apuesta inicial')
    print('3) luego de esto se agrgara una carta a la mesa y se volvera a repetir el paso 2')
    print('4) Al haber 5 cartas en mesa se evaluara tu mano y la de tu rival automaticamente para comparar')
    print('   el puntaje de ambos y dar un ganador')
    print('5) En este juego debes de buscar generar grupos para manteer ek puntaje mas alto posible, cada')
    print('   grupo tiene su respectivo valor y esta ordenado de mayor valor a mmenor')
    print(' 5.1) Escalera real de color: el grupo de mas valor se basa en una escalera de 10,J,Q,K,A ')
    print(' 5.2) Escalera de color: Una escalera de 5 cartas con el mismo palo ')
    print(' 5.3) PÃ³ker: cuatros cartas del mismo valor por ejemplo A,A,A,A,5 en este caso hay un poker de A ')
    print(' 5.4) Full: Tener tre cartas del mismo valor y un par, ejemplo A,A,A y 5,5 ')
    print(' 5.5) Color: Cinco cartas del mismo palo independientemente de la escalera')
    print(' 5.6) Escalera: cinco cartas en escalera en orden consecutico independiente de su palo')
    print(' 5.7) Trio: Conjunto de 3 cartas iguales ')
    print(' 5.8) Doble par: 2 conjuntos de 2 cartas iguales')
    print(' 5.9) Par: Conjunto de 2 cartas iguales')
    print(' 5.10) Carta alta: En caso de no haber cumplido cualquier requisito anterior se toma la carta con ')
    print('       el valor mas alto')
    print('6) Para formar los grupos puedes uusar 5 cartas bien sea  de la mesa o de tu mano')
    input("Enter para volver")

def tutorial_blackjack():
    print('---------------------------------------REGLAS--------------------------------------------------------')
    print("1) El juego consiste en alcanzar 21 o llegar lo mas cerca posible de esta cifra sin pasarse")
    print("2) En este juego eres tú contra el crupìer")
    print("3) La carta A vale 1 o 11 y las cartas Q J K valen 10")
    print("4) una vez se vea la mano del jugador y el crupier, el jugador tiene 4 opciones")
    print(" 4.1) Robar y probar suerte sacando una carta más pero arriesgandote a pasar de 21")
    print(" 4.2) Plantarse e ir por lo seguro arriesgandote a quedar abajo del crupier")
    print(" 4.3) Doblar la apuesta y sacar una carta más temiendo a quedarte sin nada")
    print(" 4.3.1) Solamente puedes doblar la apuesta en tu priumer turno y si tus cartas suman 9, 10, 11 ")
    print(" 4.4) Rendirse y ser penalizado con la mitad de tu apuesta inicial")
    print(" 4.4.1) Solamente puedes rendirte en tu primer turno")
    print("5) Puedes seguir sacando cartas mientras no te pases de 21")
    print("6) Obtienes blackjack si llegas a 21 con solo 2 cartas")
    print("7) Gana el jugador que se acerque más a 21 sin pasarse o el que obtenga blackjack")
    input("Enter para volver")