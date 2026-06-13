import csv

def mostrar_pais(pais):
# Proposito: mostrar los datos de un pais y reutilizar el formato de impresion.
    print(f"""
        Nombre: {pais["nombre"]}
        Poblacion: {pais["poblacion"]}
        Superficie: {pais["superficie"]}
        Continente: {pais["continente"]}
    """)


def seleccionar_sentido():
# Proposito: solicitar al usuario el sentido de ordenamiento
    while True:
        try:
            opcion = input("""
            1 - Ascendente
            2 - Descendente
            """).strip()

            if not opcion.isdigit():
                raise ValueError("Ingrese solo números.")

            opcion = int(opcion)

            if opcion not in (1, 2):
                raise ValueError("Ingrese 1 o 2.")

            return opcion == 2  # si la opcion coincide con el 2 devuelve true

        except ValueError as e:
            print(e)


def validar_nombre(nombre):
# proposito: esta funcion es para evitar errores con nombres con espacios como "Nueva Zelanda"
    for caracter in nombre: 
        if not (caracter.isalpha() or caracter == " "):
            return False
    return True


def agregar_pais(paises):   # Opcion 1
# Proposito: agregar un nuevo pais a la lista de paises.
    while True:
        try:
            opcion = input("""Ingrese la opcion correspondiente:
                    1 - Agregar pais
                    2 - Volver al menu principal
                    """).strip()
            
            if not opcion.isdigit():
                raise ValueError("[ERROR] Ingrese solo numeros.")
            if int(opcion) < 1 or int(opcion) > 2:
                raise ValueError("[ERROR] Ingrese solo el numero 1 ó 2.")
        
        except ValueError as e:
            print(e)
            continue

        match int(opcion):
            case 1: # primero solicito y valido los datos del nuevo pais
                nombre = input ("Ingrese el nombre del pais: ")
                continente = input (f"Ingrese a que continente pertenece {nombre}: ")
                while True:
                    try:
                        if not validar_nombre(nombre):
                            raise ValueError("Nombre de país inválido.")
                        if not validar_nombre(continente):
                            raise ValueError("Continente inválido.")
                        poblacion = int(input(f"Ingrese la poblacion de {nombre}: "))
                        superficie = int(input(f"Ingrese la superficie de {nombre}: "))
                        if poblacion <= 0:# Verificar que los valores sean mayores a cero
                            raise ValueError("La poblacion debe ser mayor a 0.")
                        if superficie  <=0:
                            raise ValueError("La superficie debe ser mayor a 0.")
                        break
                    except ValueError as e:
                        print(e)
                pais_agregado = (f"{nombre},{poblacion},{superficie},{continente}")
                print(pais_agregado)# Mostrar una vista previa de los datos ingresados
                while True:
                    try:
                        confirmar = input("Guardar los cambios? si/no: ").lower().strip()
                        # confirmar guardado, si no se descarta
                        if confirmar not in ("si", "no"):
                            raise ValueError("Ingrese solo si o no.")

                        break

                    except ValueError as e:
                        print(e)
                nuevo_pais = {
                    "nombre": nombre,
                    "poblacion": poblacion,
                    "superficie": superficie,
                    "continente": continente
                }
                if confirmar == "si":# solo se agrega el pais a la lista si fue confirmado
                    paises.append(nuevo_pais)
                    
            case 2:
                break


def actualizar_pais(paises):# Opcion 2
# Propocito: busca un pais por su nombre para actualizar poblacion o superficie
    while True:
        try:
            nombre = input("Ingrese el nombre del pais para modificar su poblacion y/o superficie: ").strip().lower()

            if not validar_nombre(nombre):
                raise ValueError("Ingrese solo letras para el nombre del pais.")
    
        except ValueError as e:
            print(e)
            continue
        
        pais_encontrado = False
        for pais in paises:#primero busca el pais
            if pais['nombre'].lower().strip() == nombre:
                pais_encontrado = True
                while True:
                    try:#y despues se pregunta que dato se desea actializar
                        opcion = input("""Ingese la opcion correspondiente:
                                1 - Modificar poblacion
                                2 - Modificar superficie
                                3 - Volver al menu princiapal
                                """)
                        if not opcion.isdigit():
                            raise ValueError("[ERROR] Ingrese solo numeros.")

                        if int(opcion) < 1 or int(opcion) > 3:
                            raise ValueError("[ERROR] Ingrese solo los numeros 1, 2 ó 3.") 
                    except ValueError as e:
                        print(e)
                        continue
                    
                    match int(opcion):
                        case 1: # Actualizar la poblacion del pais.
                            while True:
                                try: 
                                    pais['poblacion'] = int(input(f"Ingrese la nueva poblacion de {pais['nombre']}: "))
                                
                                    if pais['poblacion'] <= 0:
                                        raise ValueError("[ERROR] La poblacion debe ser mayor que cero.")
                                
                                except ValueError as e:
                                    print(e)
                                    continue

                                print(f"El pais {pais['nombre']} actualizo su valor de poblacion a {pais['poblacion']}")
                                return

                        case 2:# Actualizar la superficie del pais.
                                while True:
                                    try: 
                                        pais['superficie'] = int(input(f"Ingrese la nueva superficie de {pais['nombre']}: "))
                                    
                                        if pais['superficie'] <= 0:
                                            raise ValueError("[ERROR] La superficie debe ser mayor que cero.")
                                    
                                    except ValueError as e:
                                        print(e)
                                        continue
                                    
                                    print(f"El pais {pais['nombre']} actualizo su valor de superficie a {pais['superficie']}")
                                    return
                                        
                        case 3:
                            return
        if not pais_encontrado:# esto esta por si no se encontro el pais buscado
            print("[ERROR] Pais no encontrado, ingrese un nombre valido.")
            continue


def buscar_pais(paises):    # Opcion 3
# Proposito: Buscar un pais en la base de datos y mostrar sus datos
    while True:
        try:#primero solicitar nombre
            nombre = input("Ingrese el nombre del pais a buscar: ").strip().lower()

            if not validar_nombre(nombre):
                raise ValueError("[ERROR] Ingrese solo letras, no numeros ni caracteres invalidos.")
        except ValueError as e:
            print(e)
            continue

        sin_coincidencias = True # testigo para buscar resultados
        for pais in paises:#buscar coincidencias por nombre
            if nombre in pais["nombre"].lower().strip():
                mostrar_pais(pais)
                sin_coincidencias = False
        if sin_coincidencias:
            print("No se encontraron paises.")
        break


def filtrar_paises(paises): # Opcion 4
# Propocito: sirve para mostrar paises segun criterio de busqueda
    while True:
        try:
            opcion = input("""Ingrese la opcion correspondiente: 
                1 - Filtrar paises por continente
                2 - Filtrar paises por poblacion
                3 - Filtrar paises por superficie
                4 - Volver al menu principal
                """)
            if not opcion.isdigit():
                raise ValueError("[ERROR] Ingrese solo numeros.")
            if int(opcion) < 1  or int(opcion) > 4:
                raise ValueError("[ERROR] Ingrese solo numeros del 1 al 4.")
        
        except ValueError as e:
            print(e)
            continue

        match int(opcion):
            case 1:#filtar por continente
                while True:
                    try:
                        nombre = input("Ingrese el continente a buscar: ").strip().lower()

                        if not validar_nombre(nombre):
                            raise ValueError("[ERROR] Ingrese solo caracteres validos.")
                        
                    except ValueError as e:
                        print(e)
                        continue
                    
                    sin_coincidencias = True
                    for pais in paises:
                        if nombre in pais["continente"].strip().lower():
                            mostrar_pais(pais)
                            sin_coincidencias = False
                    if sin_coincidencias:
                        print("No se encontraron paises.")
                    return
            case 2:#filtrar por rango de poblacion
                while True:
                    try:
                        minimo = input("Minimo: ")
                        maximo = input("Maximo: ")

                        if not minimo.isdigit() or not maximo.isdigit():
                            raise ValueError("Ingrese solo numeros enteros.")
                        if int(minimo) > int(maximo):
                            raise ValueError("El minimo no puede ser mayor al maximo.")

                    except ValueError as e:
                        print(e)
                        continue
                    sin_coincidencias = True
                    print(f"Los siguientes paises tienen una poblacion entre {minimo} y {maximo}")
                    for pais in paises:
                        if int(minimo) <= int(pais["poblacion"]) <= int(maximo):
                            mostrar_pais(pais)
                            sin_coincidencias = False
                    if sin_coincidencias:
                        print("No se encontraron paises.")
                    return
            case 3:#filtrar por rango de superficie
                while True:
                    try:
                        minimo = input("Minimo: ")
                        maximo = input("Maximo: ")

                        if not minimo.isdigit() or not maximo.isdigit():
                            raise ValueError("[ERROR] Ingrese solo numeros.")
                        if int(minimo) > int(maximo):
                            raise ValueError("El minimo no puede ser mayor al maximo.")
                    
                    except ValueError as e:
                        print(e)
                        continue
                    
                    sin_coincidencias = True #testigo para detectar resultados negativos
                    print(f"Los siguientes paises tienen una superficie entre {minimo} y {maximo}")
                    for pais in paises:
                        if int(minimo) <= int(pais["superficie"]) <= int(maximo):
                            mostrar_pais(pais)
                            sin_coincidencias = False
                    if sin_coincidencias:
                        print("No se encontraron paises.")
                    return
            case 4:
                return


def ordenar_paises(paises): # Opcion 5 
# Proposito: Ordena todos los paises por nombre, poblacion o superficie
    while True:
        try:# menu de criterio de orden
            opcion = input("""Ingrese la opcion correspondiente: 
                    1 - Ordenar paises por nombre
                    2 - Ordenar paises por poblacion
                    3 - Ordenar paises por superficie
                    4 - Volver al menu principal
                    """)
            if not opcion.isdigit():
                raise ValueError("Ingrese solo numeros.")

            opcion = int(opcion)

            if opcion < 1 or opcion > 4:
                raise ValueError("Opcion fuera de rango.")

        except ValueError as e:
            print(f"[ERROR] {e}")
            continue
        match int(opcion):
            case 1:# ordenar alfabeticamente
                ordenados = sorted(
                    paises,
                    key=lambda pais: pais["nombre"]
                )
                print("\nPrimeros 10 paises ordenados por nombre:\n")
                for pais in ordenados[:10]:
                    mostrar_pais(pais)
            case 2:# ordenar poblacion de menor a mayor
                ordenados = sorted(
                    paises,
                    key=lambda pais: int(pais["poblacion"])
                )
                print("\nPrimeros 10 paises ordenados por población:\n")
                for pais in ordenados[:10]:
                    mostrar_pais(pais)
            case 3:
                ordenados = sorted(
                    paises,
                    key=lambda pais: int(pais["superficie"]),
                    reverse= seleccionar_sentido()#para cambiar el sentido
                )
                print("\nPrimeros 10 paises ordenados por superficie:\n")
                for pais in ordenados[:10]:
                    mostrar_pais(pais)
            case 4:
                break


def estadisticas(paises):   # Opcion 6
# Propposito: muestra estadisticas generales de los paises
    if not paises:
        print("No hay países cargados.")
        return
    # Inicializar minimos y maximos con el primer pais
    minimo = maximo = int(paises[0]["poblacion"])
    pais_min = pais_max = paises[0]["nombre"]

    acumulador_poblacion = 0
    acumulador_superficie = 0
    por_continente = {}# Diccionario para contar paises por continente

    for pais in paises:
        poblacion = int(pais["poblacion"])
        superficie = int(pais["superficie"])
        continente = pais["continente"]

        # busca el pais con mayor y menor poblacion
        if poblacion > maximo:
            maximo = poblacion
            pais_max = pais["nombre"]

        if poblacion < minimo:
            minimo = poblacion
            pais_min = pais["nombre"]

        # acumuladores
        acumulador_poblacion += poblacion
        acumulador_superficie += superficie

        # conteo por continente
        if continente in por_continente:
            por_continente[continente] += 1
        else:
            por_continente[continente] = 1

    print(f"El pais con la menor poblacion es {pais_min} con {minimo}.")
    print(f"El pais con la mayor poblacion es {pais_max} con {maximo}.")

    print(f"El promedio de poblacion entre todos los paises es {(acumulador_poblacion/len(paises)):,.2f} habitantes.")

    print(f"El promedio de superficie entre todos los paises es {(acumulador_superficie/len(paises)):,.2f} kilometros cuadrados.")

    print("Cantidad de países por continente: ")
    for continente, cantidad in por_continente.items():
        print(f"{(continente).strip()}: {cantidad}")


def guardar_cambios(paises):# Opcion 7
# Proposito: Guardar los cambios realizados en el archivo CSV
    with open("paises.csv", "w", encoding="utf-8") as archivo:

        archivo.write("nombre,poblacion,superficie,continente\n")
        for pais in paises:
            archivo.write(
                f"{pais['nombre']},{pais['poblacion']},{pais['superficie']},{pais['continente']}\n"
            )
    print("Cambios guardados correctamente.")


def menu():# Menu y gestion
# Propocito: muestra el menu y gestiona el flujo principal del programa
    paises = []
    # este bloque esta para recuperar los datos guardados previamente desde el archivo CSV
    # y manejar situaciones donde el archivo no existe o no contiene datos validos
    try:
        with open("paises.csv", "r", encoding="utf-8") as archivo:
            lector = csv.DictReader(archivo)

            # Verificar si el archivo esta vacio
            required = {"nombre", "poblacion", "superficie", "continente"}
            if not lector.fieldnames or not required.issubset(lector.fieldnames):
                print("[ERROR] Archivo vacio o sin datos validos.")
                print("Se recomienda usar la opcion 1 del menu para agregar paises manualmente.")
            else:
                for fila in lector:#esta parte recorre las filas de datos numericos y los pasa a enteros
                    try:
                        if not fila:  
                            continue
                        fila["poblacion"] = int(fila["poblacion"])
                        fila["superficie"] = int(fila["superficie"])
                        paises.append(fila)
                    except (ValueError, KeyError):
                        print(f"[ERROR] Registro inválido ignorado: {fila}")
    # Si el archivo no existe, iniciar el programa con una lista vacia
    except FileNotFoundError:
                    print("No existe el archivo, se inicia vacío.")

    while True:
        print("""
1. Agregar pais
2. Actualizar pais
3. Buscar pais
4. Filtrar paises
5. Ordenar paises
6. Estadisticas
7. Guardar cambios y salir
""")
        try:
            opcion = input("Ingrese una opcion: ").strip()

            if not opcion.isdigit():
                raise ValueError("[ERROR] Ingresar solo numeros.")
            if int(opcion) < 1 or int(opcion) > 7:
                raise ValueError("[ERROR] Ingresar solo numeros del 1 al 7.")
        
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

            case 7:
                confirmar = input("¿Desea guardar los cambios? (si/no): ").strip().lower()

                if confirmar == "si":
                    guardar_cambios(paises)

                print("Saliendo del programa...")
                break


menu()