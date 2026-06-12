import csv

def agregar_pais(paises):
    """Agrega un pais nuevo"""
    while True:
        try:
            opcion = input("""Ingrese la opcion correspondiente:
                    1 - Agregar pais
                    2 - Volver al menu principal
                    """).strip()
            
            if not opcion.isdigit():
                raise ValueError("[ERROR]Ingrese solo numeros")
            if int(opcion) < 1 or int(opcion) > 2:
                raise ValueError("[ERROR]Ingrese solo el numero 1 ó 2")
        
        except ValueError as e:
            print(e)
            continue

        match int(opcion):
            case 1:
                nombre = input ("Ingrese el nombre del pais: ")
                poblacion = input (f"Ingrese la poblacion de {nombre}: ")
                superficie = input (f"Ingrese la superficie de {nombre}")
                continente = input (f"Ingrese a que continente pertenece {nombre}: ")
                pais_agregado = (f"{nombre},{poblacion},{superficie},{continente}")
                print(pais_agregado)
                while True:
                    try:
                        confirmar = input("Guardar los cambios? si/no: ").lower().strip()

                        if confirmar not in ("si", "no"):
                            raise ValueError("Ingrese solo si o no")

                        break

                    except ValueError as e:
                        print(e)
                nuevo_pais = {
                    "nombre": nombre,
                    "poblacion": poblacion,
                    "superficie": superficie,
                    "continente": continente
                }
                if confirmar == "si":
                    paises.append(nuevo_pais)
                    
            case 2:
                break


def buscar_pais(paises):
    while True:
        try:
            nombre_buscado = input("Ingrese el nombre del pais a buscar: ").strip().lower()

            if not nombre_buscado.isalpha():
                raise ValueError("[ERROR]Ingrese solo letras, no numeros ni caracteres invalidos")
        except ValueError as e:
            print(e)
            continue

        sin_coincidencias = True
        for pais in paises:
            if nombre_buscado in pais["nombre"].lower().strip():
                print(f"Pais:{pais["nombre"]},Poblacion: {pais["poblacion"]}, Superficie: {pais["superficie"]}, Continente: {pais["continente"]}")
                sin_coincidencias = False
        if sin_coincidencias:
            print("No se encontraron paises")
        break


def actualizar_pais(paises):
    #Creo que esta funcion ya esta, testear.
    while True:
        try:
            nombre = input("Ingrese el nombre del pais para modificar su poblacion y/o superficie: ").strip().lower()

            if not nombre.isalpha():
                raise ValueError("Ingrese solo letras para el nombre del pais")
    
        except ValueError as e:
            print(e)
            continue
        
        pais_encontrado = False
        for pais in paises:
            if pais["nombre"].lower().strip() == nombre:
                pais_encontrado = True
                while True:
                    try:
                        opcion = input("""Ingese la opcion correspondiente:
                                1 - Modificar poblacion
                                2 - Modificar superficie
                                3 - Volver al menu princiapal
                                """)
                        if not opcion.isdigit():
                            raise ValueError("[ERROR]Ingrese solo numeros")

                        if int(opcion) > 3 or int(opcion) == 0:
                            raise ValueError("[ERROR]Ingrese solo los numeros 1, 2 ó 3") 
                    except ValueError as e:
                        print(e)
                        continue
                    
                    match int(opcion):
                        case 1: 
                            while True:
                                try: 
                                    pais["poblacion"] = input(f"Ingrese la nueva poblacion de {pais["nombre"]}: ")
                                
                                    if pais["poblacion"].strip() == "":
                                        raise ValueError("[ERROR]No se detectaron caracteres, ingrese un numero valido")
                                    if not pais["poblacion"].isdigit():
                                        raise ValueError("[ERROR] Ingrese solo numeros enteros positivos para la poblacion del pais")
                                    if pais["poblacion"] == 0:
                                        raise ValueError("[ERROR]La poblacion no puede ser cero")
                                
                                except ValueError as e:
                                    print(e)
                                    continue

                                print(f"El pais {pais["nombre"]} actualizo su valor de poblacion a {pais["poblacion"]}")
                                return

                        case 2:
                                while True:
                                    try: 
                                        pais["superficie"] = input(f"Ingrese la nueva superficie de {pais["nombre"]}: ")
                                    
                                        if pais["superficie"].strip() == "":
                                            raise ValueError("[ERROR]No se detectaron caracteres, ingrese un numero valido")
                                        if not pais["superficie"].isdigit():
                                            raise ValueError("[ERROR] Ingrese solo numeros enteros positivos para la superficie del pais")
                                        if pais["superficie"] == 0:
                                            raise ValueError("[ERROR]La superficie no puede ser cero")
                                    
                                    except ValueError as e:
                                        print(e)
                                        continue
                                    
                                    print(f"El pais {pais["nombre"]} actualizo su valor de superficie a {pais["superficie"]}")
                                    return
                                        
                        case 3:
                            return
        if not pais_encontrado:
            print("[ERROR]Pais no encontrado, ingrese un nombre valido")
            continue
            

def filtrar_paises(paises):
    #Opcion 4
    while True:
        try:
            opcion = input("""Ingrese la opcion correspondiente: 
                1 - Filtrar paises por continente
                2 - Filtrar paises por poblacion
                3 - Filtrar paises por superficie
                4 - Volver al menu principal
                """)
            if not opcion.isdigit():
                raise ValueError("[ERROR]Ingrese solo numeros")
            if int(opcion) < 1  or int(opcion) > 4:
                raise ValueError("[ERROR]Ingrese solo numeros del 1 al 4")
        
        except ValueError as e:
            print(e)
            continue

        match int(opcion):
            case 1:
                while True:
                    try:
                        continente = input("Ingrese el continente a buscar: ").strip().lower()

                        if not continente.isalpha():
                            raise ValueError("[ERROR]Ingrese solo caracteres validos")
                        
                    except ValueError as e:
                        print(e)
                        continue
                    
                    sin_coincidencias = True
                    for pais in paises:
                        if continente in pais["continente"].lower():
                            print(pais["nombre"])
                            sin_coincidencias = False
                    if sin_coincidencias:
                        print("No se encontraron paises")
                    return
            case 2:
                while True:
                    try:
                        minimo = input("Minimo: ")
                        maximo = input("Maximo: ")

                        if not minimo.isdigit() or not maximo.isdigit():
                            raise ValueError("Ingrese solo numeros enteros")
                        if minimo > maximo:
                            raise ValueError("El minimo no puede ser mayor al maximo")

                    except ValueError as e:
                        print(e)
                        continue
                    sin_coincidencias = True
                    print(f"Los siguientes paises tienen una poblacion entre {minimo} y {maximo}")
                    for pais in paises:
                        if int(minimo) <= int(pais["poblacion"]) <= int(maximo):
                            print(pais["nombre"])
                            sin_coincidencias = False
                    if sin_coincidencias:
                        print("No se encontraron paises")
                    return
            case 3:
                while True:
                    try:
                        minimo = input("Minimo: ")
                        maximo = input("Maximo: ")

                        if not minimo.isdigit() or not maximo.isdigit():
                            raise ValueError("[ERROR]Ingrese solo numeros")
                        if minimo > maximo:
                            raise ValueError("El minimo no puede ser mayor al maximo")
                    
                    except ValueError as e:
                        print(e)
                        continue
                    
                    sin_coincidencias = True
                    print(f"Los siguientes paises tienen una superficie entre {minimo} y {maximo}")
                    for pais in paises:
                        if int(minimo) <= int(pais["superficie"]) <= int(maximo):
                            print(pais["nombre"])
                            sin_coincidencias = False
                    if sin_coincidencias:
                        print("No se encontraron paises")
                    return
            case 4:
                return
        
def ordenar_paises(paises):
    #Opcion 5
    while True:
        #Para estos ordenamientos usar bubble sort o binary sort
        opcion = input("""Ingrese la opcion correspondiente: 
                1 - Ordenar paises por nombre
                2 - Ordenar paises por poblacion
                3 - Ordenar paises por superficie
                4 - Volver al menu principal
                """)
        match int(opcion):
            case 1:
                pass
            case 2:
                pass
            case 3:
                pass
            case 4:
                break

def estadisticas(paises):
    #Paises con la menor y mayor poblacion
    minimo = int(paises[0]["poblacion"]) #Seteo el minimo como la poblacion del primer elemento de la lista.
    pais_min = None
    maximo = 0
    pais_max = None
    for pais in paises:
        if int(pais["poblacion"]) > maximo:
            maximo = int(pais["poblacion"])
            pais_max = pais["nombre"]
        if int(pais["poblacion"]) < minimo:
            minimo = int(pais["poblacion"])
            pais_min = pais["nombre"]
    print(f"El pais con la menor poblacion es {pais_min} con {minimo}")
    print(f"El pais con la mayor poblacion es {pais_max} con {maximo}")
    
    #Promedio de poblacion entre todos los paises
    acumulador_poblacion = 0
    for pais in paises:
        acumulador_poblacion += int(pais["poblacion"])
    print(f"El promedio de poblacion entre todos los paises es {(acumulador_poblacion/len(paises)):,.2f}")
    
    #Promedio de superficie
    acumulador_superficie = 0
    for pais in paises:
        acumulador_superficie += int(pais["superficie"])
    print(f"El promedio de superficie entre todos los paises es {(acumulador_superficie/len(paises)):,.2f} kilometros cuadrados")
    
    #Agregar cantidad de países por continente,ver como hago esto despues

def guardar_cambios(paises):
    #Esta es la funcion de la opcion del menu que guardara cambios.
    pass 

def menu():
    paises = []
    with open("../datos/paises.csv", "r") as archivo:
            lector = csv.DictReader(archivo)
    
            for i in lector:
                paises.append(i)
    #Agregar una opcion para guardar cambios que escriba la lista en el archivo csv
    #Por ahora todo esta en la lista paises = []
    #Tengo que poner una opcion que diga "guardar cambios?" , confirmar si desea guardar cambios
    #Y ahi recien con with open sobreescribir el archivo .csv con los nuevos datos.
    while True:
        print("""
1. Agregar pais
2. Actualizar pais
3. Buscar pais
4. Filtrar paises
5. Ordenar paises
6. Estadisticas
7. Salir
""")
        try:
            opcion = input("Ingrese una opcion: ")

            if not opcion.isdigit():
                raise ValueError("[ERROR] Ingresar solo numeros")
            if int(opcion) < 1 or int(opcion) > 8:
                raise ValueError("[ERROR] Ingresar solo numeros del 1 al 8")
        
        except ValueError as e:
            print(e)
            continue
        
        match int(opcion):
            case 1:
                agregar_pais(paises)

            case 2:
                actualizar_pais(paises)

            case 3:
                buscar_pais(paises)

            case 4:
                filtrar_paises(paises)

            case 5:
                ordenar_paises(paises)

            case 6:
                estadisticas(paises)
            #Agregar aca abajo uan nueva opcion para guardar datos.
            case 7:
                break

menu()