while True:
    #PARTE PRINCIPAL DEL PROGRAMA, PRIMERA INTERFAZ SELECCIÓN DE OPCIONES.
    print("############################################################")
    print("Bienvido! al medidor multifuncional")
    print("Seleccione una alrnativa:")
    print("\n","1- Calcular velocidad promedio \n","2- Calcular distancia recorrida \n","3- Salir del programa")

    print("\n")

    variable1 = int(input("Ingrese una opcion:"))

    #SI LA OPCION INGRESADA FUE 1, ENTONCES INGRESO A LA CALCULADORA DE VELOCIDAD PROMEDIO
    if variable1 == 1:
        while True:
            print("############################################################")
            print("Bienvenido al sistema de calculadora de velocidad promedio");
            kilometros = int(input("Ingrese los kilometros: "))
            tiempo = int(input("Ingrese el tiempo transcurrido:"))

            #OPERACIÓN MATEMATICA PARA LA VELOCIDAD PROMEDIO. 
            calculoVe = kilometros/tiempo; 
            print(f"la velocidad promedio fue de:{calculoVe} km/h")
            print("###########################################################")
            print("\n")
            #INTERFAZ DONDE SE LE PREGUNTA AL USUARIO QUE QUIERE HACER.
            print("Que desea hacer?")
            print("1-Volver a ingresar datos")
            print("2-Volver al menu principal")
            tecla = int(input("ingrese una opción:"))
            #FLUJO DEL PROGRAMA DEPENDIENDO DE LA OPCION A ELEGIR. 
            if tecla == 1:
                input("presione enter..")
            elif tecla == 2:
                break
    #SI LA OPCION INGRESADA FUE 2, ENTONCES INGRESO A LA CALCULADORA DE DISTANCIA RECORRIDA
    elif variable1 == 2:
        while True:
            print("############################################################")
            print("Bienvenido al sistema de calculadora de distancia recorrida")
            kmh = int(input("ingrese los km/h: "))
            tiempo = int(input("ingrese el tiempo recorrido: "))

            #OPERACIÓN MATEMATICA PARA LA DISTANCIA RECORRIDA.
            divisions = kmh*tiempo 
            print(f"Ha recorrido una distanicia de {divisions} kilometros")
            print("############################################################")
            #INTERFAZ DONDE SE LE PREGUNTA AL USUARIO QUE QUIERE HACER.
            print("Que desea hacer?")
            print("1-Volver a ingresar datos")
            print("2-Volver al menu principal")
            tecla = int(input("ingrese una opción:"))
            #FLUJO DEL PROGRAMA DEPENDIENDO DE LA OPCION A ELEGIR. 
            if tecla == 1:
                input("presione enter..")
            elif tecla == 2:
                break
    #SI LA OPCION INGRESADA FUE 3 O CUALQUIER OTRA, ENTONCES INGRESO SALIR DEL PROGRAMA. 
    else:
        print("saliste del programa")
        break

