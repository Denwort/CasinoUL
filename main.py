import os
import random
import random
import guardar_info as db
import login_y_register
import blackjack as bj
import baccarat_ga as bc
import poker_texas_holdem as pk
import tutoriales as tuto
clear = lambda: os.system('cls')


def main():

    clear()
    print("CASINO ULIMA")

    usuario = login_y_register.menu_login_register()   

    datos_usuario = db.leer_usuario(usuario)
    user_usuario = datos_usuario[0]
    user_contraseña = datos_usuario[1]
    user_saldo = int(datos_usuario[2])
    user_partidas = datos_usuario[3]

    apuesta = 10
        
    while True:

        # Menu principal
        clear()
        print("            CASINO ULIMA            ")
        print("Bienvenido a la mejor casa de juegos")
        print("Saldo:", int(db.leer_usuario(user_usuario)[2]) , "fichas.")
        print()
        print("1. Compra y venta de fichas")
        print("2. Juegos disponibles")
        print("3. Perfil de usuario")
        print("4. Sobre nosotros")
        print("5. Salir")

        opcion = int(input("seleccione una opcion: "))

        if opcion < 1 or opcion > 5:
            print("--------")
            print("INVALIDO")
            print("--------")
            input("Enter para reintentar")

        # Menu 1
        elif opcion == 1:
            while True:
                clear() 
                user_saldo = int(db.leer_usuario(user_usuario)[2])
                print("  Compra y venta de fichas")

                print("1. Compra de fichas: Tienda Virtual Casino Ulima")
                print("2. Venta de fichas: Tienda Virtual Casino Ulima")
                print("3. Volver al menú principal")

                opc_1 = int(input("Seleccione una opción: "))

                if opc_1 < 1 or opc_1 > 3:
                    print("--------")
                    print("INVALIDO")
                    print("--------")
                    input("Enter para reintentar")
                
                # Menu 1.1
                elif opc_1 == 1:
                    clear()
                    print("  Compra de fichas: Tienda Virtual Casino Ulima")
                    print("Compra: 0.70 USD")
                    print("Su saldo actual es ", user_saldo)
                    fich = int(input("Ingrese la cantidad de fichas deseadas: "))
                    mont_fin = round(fich * 0.70 ,2)
                    print("El monto en dolares seria de: ", mont_fin, " dolares" )
                    input("Enter para confirmar compra ")
                    clear()
                    print("Se ha cargado ", mont_fin, " dolares a su tarjeta")
                    print("")
                    print("Su saldo actual es ", fich + user_saldo)
                    db.cambiar_saldo(user_usuario, fich)
                    input("Enter para volver al menú ")

                # Menu 1.2
                elif opc_1 == 2:
                    clear()
                    print("  Venta de fichas: Tienda Virtual Casino Ulima")
                    print("Venta: 0.65 USD")
                    print("Su saldo actual es", user_saldo)
                    f2 = int(input("Ingrese la cantidad de fichas a vender: "))
                    doll = round(f2 * 0.65 , 2)
                    if f2 == user_saldo:
                        print("Está retirando todas sus fichas") 
                        print("Ha recibido ", doll, " dolares" + " en su tarjeta")
                        input("Enter para confirmar transacción ")
                        db.cambiar_saldo(user_usuario, f2*(-1))                        

                    elif f2 < user_saldo:
                        print("Está retirando", f2, "fichas") 
                        print("Ha recibido ", doll, " dolares en su tarjeta")
                        input("Enter para confirmar transacción ")
                        db.cambiar_saldo(user_usuario, f2*(-1))                        

                    elif f2 > user_saldo:
                        print("No cuenta con fichas suficientes para retirar")
                        input("Enter para reintentar")

                # Menu 1.3
                elif opc_1 == 3:
                    clear()
                    print("Volviendo al menú")         
                    break

        # Menu 2
        elif opcion == 2:
            while True:
                clear() 
                print("  Juegos disponibles")

                print("1. Blackjack")
                print("2. Poker Texas")
                print("3. Baccarat")
                print("4. Volver al menú principal")

                ga_opcion = int(input("Seleccione una opción: "))
                
                # Menu 2.1
                if ga_opcion == 1:
                    while True:
                        clear() 
                        print("  Blackjack")
                        print("Apuesta actual: ",apuesta , " fichas.")
                        print("1. Tutorial")
                        print("2. Jugar Blackjack")
                        print("3. Cambiar apuesta")
                        print("4. Volver al menú principal")
                        bj_opcion = int(input("Seleccione una opción: "))

                        # Menu 2.1.1
                        if bj_opcion == 1:
                            clear()
                            tuto.tutorial_blackjack()

                        # Menu 2.1.2
                        elif bj_opcion == 2:
                            clear()
                            if db.acepta_apuesta(user_usuario, apuesta):
                                numero_partida = random.randint(10000, 99999)
                                resultado = bj.blackjack(numero_partida, apuesta)
                                # Ajustar dinero segun el resultado del juego y registrar partida
                                db.cambiar_saldo(user_usuario, resultado)
                                db.agregar_partida(user_usuario, "BJ", numero_partida, resultado)
                                input("Enter para volver")
                            else:
                                print("Saldo insuficiente para apostar, compra más en nuestra tienda virtual")
                                input("Enter para volver")

                        # Menu 2.1.3    
                        elif bj_opcion == 3:
                            clear()
                            print("2. Cambiar apuesta")
                            print("Su saldo actual es ", user_saldo)
                            apuesta = int(input("Introduzca un número entero para la cantidad de fichas que va a apostar: "))
                            
                        # Menu 2.1.4
                        elif bj_opcion == 4:
                            print("Volviendo al menú")
                            break
                        else:
                            print("Invalido")
                            input("Enter para reintentar")

                # Menu 2.2
                elif ga_opcion == 2:
                    while True:
                        clear() 
                        print("  Poker Texas")
                        print("Apuesta actual: ", apuesta, " fichas.")
                        print("1. Tutorial")
                        print("2. Jugar Poker Texas")
                        print("3. Cambiar apuesta")
                        print("4. Volver al menú principal")
                        pt_opcion = int(input("Seleccione una opción: "))

                        # Menu 2.2.1
                        if pt_opcion == 1:
                            clear()
                            tuto.tutorial_pkt()
                        
                        # Menu 2.2.2
                        elif pt_opcion == 2:
                            clear()
                            if db.acepta_apuesta(user_usuario, apuesta):
                                numero_partida = random.randint(10000, 99999)
                                resultado = pk.poker_texas(user_usuario,apuesta)
                                db.cambiar_saldo(user_usuario, resultado)
                                db.agregar_partida(user_usuario, "PK", numero_partida, resultado)
                                input("Enter para volver")
                            else:
                                print("Saldo insuficiente para apostar, compra más en nuestra tienda virtual")
                                input("Enter para volver")
                        
                        # Menu 2.2.3
                        elif pt_opcion == 3:
                            clear()
                            print("2. Cambiar apuesta")
                            print("Su saldo actual es ", user_saldo)
                            apuesta = int(input("Introduzca un número entero para la cantidad de fichas que va a apostar: "))

                        # Menu 2.2.4
                        elif pt_opcion == 4:
                            print("Volviendo al menú")
                            break
                        else:
                            print("Invalido")
                            input("Enter para reintentar")

                # Menu 2.3        
                elif ga_opcion == 3:
                    while True:
                        clear() 
                        print("  Baccarat")
                        print("Apuesta actual: ", apuesta, " fichas.")
                        print("1. Tutorial")
                        print("2. Jugar Baccarat")
                        print("3. Cambiar apuesta")
                        print("4. Volver al menú principal")
                        bj_opcion = int(input("Seleccione una opción: "))

                        # Menu 2.3.1        
                        if bj_opcion == 1:
                            clear()
                            tuto.tutorial_baccarat()

                        # Menu 2.3.2
                        elif bj_opcion == 2:
                            clear()
                            if db.acepta_apuesta(user_usuario, apuesta):
                                numero_partida = random.randint(10000, 99999)
                                resultado = bc.baccarat(apuesta)
                                db.cambiar_saldo(user_usuario, resultado)
                                db.agregar_partida(user_usuario, "BC", numero_partida, resultado)
                                input("Enter para volver")
                            else:
                                print("Saldo insuficiente para apostar, compra más en nuestra tienda virtual")
                                input("Enter para volver")
                        
                        # Menu 2.3.3
                        elif bj_opcion == 3:
                            clear()
                            print("2. Cambiar apuesta")
                            print("Su saldo actual es ", user_saldo)
                            apuesta = int(input("Introduzca un número entero para la cantidad de fichas que va a apostar: "))
                        
                        # Menu 2.3.4
                        elif bj_opcion == 4:
                            print("Volviendo al menú")
                            break
                        else:
                            print("Invalido")
                            input("Enter para reintentar")

                # Menu 2.4                  
                elif ga_opcion == 4:
                    print("Volviendo al menú")
                    break
                else:
                    print("Invalido")
                    input("Enter para reintentar")

        # Menu 3
        elif opcion == 3:
            clear()
            print("  Record de ganancias y perdidas")
            print()
            print("Saldo de la cuenta:", round(db.leer_usuario(user_usuario)[2]), "fichas" )
            print()
            print("Juego     Numero de partida     Resultado")
            partidas = db.leer_usuario(user_usuario)[3]
            if partidas != [['']]:
                partidas_ganadas = 0
                for i in range(len(partidas)):
                    partida = partidas[i]
                    nombre_juego = partida[0]
                    numero_partida = partida[1]
                    resultado_partida = partida[2]
                    print(" " + nombre_juego + "             " + numero_partida + "              " + resultado_partida)
                    if int(resultado_partida)> 0:
                        partidas_ganadas+=1
                winrate = round( partidas_ganadas*100/len(partidas), 2) 
                print("Winrate: " + str(winrate) + "%")

                print("Leyenda:  BJ - Blackjack, PK - Poker Texas Holdem, BC - Baccarat")
            print()
            input("Enter para continuar")

        # Menu 4
        elif opcion == 4:
            clear()
            print("  Sobre nosotros")
            print()
            print("Andres Anthony Churampi Guerrero - 20210670")
            print("Guido Alejandro Aquice Campos - 20213244")
            print("Moises David Mamani Medina - 20211589")
            print("Piero Alejandro Rozas Aleman - 20212407")
            print()
            print("         Misión                                                  Visión             ")
            print("    Satisfacer a cada usuario                         Ser de los casinos exclusivos ")
            print("    asegurando la seguridad de                        más reconocidos en el país, de")
            print("    lo mas valioso que guarda en                      manera que logremos incentivar")
            print("    sus bolsillos y garantizando                      este tipo de juegos sanamente ")
            print("    la sana diversionen cada juego                    en otro tipo de instituciones")           
            print()
            print("               Numero de atención al cliente: 939123623                   ")
            print()
            input("Enter para volver al menú")

        # Menu 5
        elif opcion == 5:

            clear()
            print("-----------------------------")
            print("--- Gracias por su visita ---")
            print("-----------------------------")
            break

if __name__ == "__main__":
    main()