# Buscador de Paises

Trabajo Práctico Integrador (TPI) - Programación I

Alumnos 
Juan Ignacion Rodriguez (comision 14)
Guido Ignacio Toledo Gonzalez (comision 25)


## Descripción

Este proyecto consiste en el desarrollo de una aplicación en Python para la gestión de información de países utilizando un archivo CSV, listas, diccionarios y funciones.

El sistema permite realizar consultas, búsquedas, filtros, ordenamientos y estadísticas sobre un conjunto de datos de países, aplicando los conceptos estudiados durante la cursada de Programación I.

La información se almacena en memoria mediante una lista de diccionarios, permitiendo realizar operaciones de consulta, filtrado, ordenamiento y actualización de manera eficiente.

---

## Funcionamiento General

El programa se organiza a partir de una función principal que actúa como gestor del sistema. Al iniciarse, carga los datos desde un archivo CSV y muestra un menú de opciones desde el cual el usuario puede acceder a las distintas funcionalidades disponibles.

Cada opción del menú se encuentra implementada en una función específica e independiente, encargada de realizar una única tarea, como agregar países, actualizar información, realizar búsquedas, aplicar filtros, ordenar datos o generar estadísticas.

Además, el sistema incluye funciones auxiliares reutilizables destinadas a simplificar tareas comunes, como la validación de datos ingresados por el usuario, la búsqueda de países por nombre y la visualización de la información de un país. Esto permite evitar la duplicación de código, mejorar la legibilidad y facilitar el mantenimiento del programa.

---

## Objetivos

- Leer y procesar información desde archivos CSV.
- Utilizar listas y diccionarios como estructuras de almacenamiento.
- Implementar funciones para modularizar el código.
- Aplicar filtros y ordenamientos sobre conjuntos de datos.
- Generar estadísticas a partir de la información cargada.
- Incorporar validaciones y manejo básico de errores.

---

## Flujo del programa

1. Inicio del sistema.
2. Carga de datos desde el archivo CSV (si existe).
3. Visualización del menú principal.
4. Selección de una opción:
   - Agregar país.
   - Actualizar país.
   - Buscar país.
   - Filtrar países.
   - Ordenar países.
   - Mostrar estadísticas.
   - Guardar cambios y salir.
5. Fin del programa.             

---

## Dataset

Cada país contiene los siguientes atributos:

| Campo | Tipo |
|---------|---------|
| Nombre | String |
| Población | Integer |
| Superficie (km²) | Integer |
| Continente | String |

Los datos son cargados desde el archivo paises.csv utilizando la biblioteca csv de Python.

## Funcionalidades

### Gestión de Países

- Agregar país.
- Actualizar población y superficie.
- Buscar país por coincidencia parcial o exacta.

### Filtros

- Filtrar por continente.
- Filtrar por rango de población.
- Filtrar por rango de superficie.

### Ordenamientos

- Ordenar por nombre.
- Ordenar por población.
- Ordenar por superficie.
- Orden ascendente y descendente.

### Estadísticas

- País con mayor población.
- País con menor población.
- Promedio de población.
- Promedio de superficie.
- Cantidad de países por continente.

## Validaciones Implementadas

- Verificación de entradas numéricas.
- Control de campos vacíos o inválidos.
- Validación de rangos en filtros.
- Control de errores en la lectura del archivo CSV.
- Manejo de búsquedas sin resultados.
- Mensajes informativos de error y confirmación.
  
## Ejecución y Persistencia de datos

1. Abrir terminal en la carpeta del proyecto
2. Ejecutar:

```bash
python buscador_de_paises.py
```

- Carga automática de datos desde archivo CSV al iniciar el sistema.
- Guardado manual de cambios en archivo CSV mediante opción del menú.
  
## Tecnologías Utilizadas

- Python 3
- Archivos CSV
- Listas
- Diccionarios
- Funciones

## Video Demostrativo

Link al video:

[PEGAR ENLACE]

## Documentación

Informe PDF:

[PEGAR ENLACE]
