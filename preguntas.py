"""
Laboratorio de Programación Básica en Python para Manejo de Datos
-----------------------------------------------------------------------------------------

Este archivo contiene las preguntas que se van a realizar en el laboratorio.

No puede utilizar pandas, numpy o scipy. Se debe utilizar solo las funciones de python
básicas.

Utilice el archivo `data.csv` para resolver las preguntas.


"""

# Importar las librerías necesarias
import csv

# Cargo el archivo csv
file_csv = "c:/Users/Gamer/Documents/GitHub/lab-01-python-basico-Carturo8/data.csv"


def pregunta_01():
    """
    Retorne la suma de la segunda columna.

    Rta/
    214

    """
    # Variable para almacenar la suma de la segunda columna
    resultados_1 = 0

    # Abrir el archivo CSV en modo lectura
    with open(file_csv, 'r') as file:
        # Crear un lector CSV con el delimitador especificado
        reader = csv.reader(file, delimiter='\t')
        
        # Leer cada fila del archivo CSV
        for row in reader:
            # Convertir el segundo elmento de cada fila (valores de la columna 2) a entero y sumarlo
            resultados_1 += int(row[1])

    return resultados_1


def pregunta_02():
    """
    Retorne la cantidad de registros por cada letra de la primera columna como la lista
    de tuplas (letra, cantidad), ordendas alfabéticamente.

    Rta/
    [
        ("A", 8),
        ("B", 7),
        ("C", 5),
        ("D", 6),
        ("E", 14),
    ]

    """
    # Diccionario para almacenar la cantidad de registros por cada letra
    diccionario_col_1 = {}

    # Abrir el archivo CSV en modo lectura
    with open(file_csv, 'r') as file:
        # Crear un lector CSV con el delimitador especificado
        reader = csv.reader(file, delimiter='\t')
        
        # Leer cada fila del archivo CSV
        for row in reader:
            # Verificar si la fila tiene elementos
            if row:
                # Obtener las letras de la columna 1
                letra = row[0]
                # Incrementar la cantidad para la letra correspondiente
                diccionario_col_1[letra] = diccionario_col_1.get(letra, 0) + 1

    # Convertir el diccionario en una lista de tuplas
    resultados_2 = [(letra, cantidad) for letra, cantidad in diccionario_col_1.items()]

    # Ordenar la lista de tuplas alfabéticamente
    resultados_2 = sorted(resultados_2, key=lambda x: x[0])

    return resultados_2


def pregunta_03():
    """
    Retorne la suma de la columna 2 por cada letra de la primera columna como una lista
    de tuplas (letra, suma) ordendas alfabeticamente.

    Rta/
    [
        ("A", 53),
        ("B", 36),
        ("C", 27),
        ("D", 31),
        ("E", 67),
    ]

    """
    # Diccionario para almacenar la suma de la columna 2 por cada letra
    diccionario_col_1_2 = {}

    # Abrir el archivo CSV en modo lectura
    with open(file_csv, 'r') as file:
        # Crear un lector CSV con el delimitador especificado
        reader = csv.reader(file, delimiter='\t')
        
        # Leer cada fila del archivo CSV
        for row in reader:
            # Verificar si la fila tiene elementos
            if row:
                # Obtener las letras de la columna 1
                letra = row[0]
                # Obtener el valor de la columna 2
                valor_col_2 = int(row[1])
                # Realizar e incrementar la suma para la letra correspondiente
                diccionario_col_1_2[letra] = diccionario_col_1_2.get(letra, 0) + valor_col_2

    # Convertir el diccionario en una lista de tuplas
    resultados_3 = [(letra, suma) for letra, suma in diccionario_col_1_2.items()]

    # Ordenar la lista de tuplas alfabéticamente
    resultados_3 = sorted(resultados_3, key=lambda x: x[0])

    return resultados_3


def pregunta_04():
    """
    La columna 3 contiene una fecha en formato `YYYY-MM-DD`. Retorne la cantidad de
    registros por cada mes, tal como se muestra a continuación.

    Rta/
    [
        ("01", 3),
        ("02", 4),
        ("03", 2),
        ("04", 4),
        ("05", 3),
        ("06", 3),
        ("07", 5),
        ("08", 6),
        ("09", 3),
        ("10", 2),
        ("11", 2),
        ("12", 3),
    ]

    """
    # Diccionario para almacenar la cantidad de registros por cada mes
    diccionario_col_3 = {}

    # Abrir el archivo CSV en modo lectura
    with open(file_csv, 'r') as file:
        # Crear un lector CSV con el delimitador especificado
        reader = csv.reader(file, delimiter='\t')
        
        # Leer cada fila del archivo CSV
        for row in reader:
            # Verificar si la fila tiene elementos
            if row:
                # Obtener la fecha de la columna 3
                fecha = row[2]
                # Obtener el mes de la fecha
                mes = fecha.split('-')[1]
                # Incrementar la cantidad para el mes correspondiente
                diccionario_col_3[mes] = diccionario_col_3.get(mes, 0) + 1
    
    # Convertir el diccionario en una lista de tuplas
    resultados_4 = [(mes, cantidad) for mes, cantidad in diccionario_col_3.items()]

    # Ordenar la lista de tuplas alfabéticamente
    resultados_4 = sorted(resultados_4, key=lambda x: x[0])
    
    return resultados_4


def pregunta_05():
    """
    Retorne una lista de tuplas con el valor maximo y minimo de la columna 2 por cada
    letra de la columa 1.

    Rta/
    [
        ("A", 9, 2),
        ("B", 9, 1),
        ("C", 9, 0),
        ("D", 8, 3),
        ("E", 9, 1),
    ]

    """
    # Diccionario para almacenar el valor máximo y mínimo de la columna 2 por cada letra
    diccionario_max_min_col_1_2 = {}

    # Abrir el archivo CSV en modo lectura
    with open(file_csv, 'r') as file:
        # Crear un lector CSV con el delimitador especificado
        reader = csv.reader(file, delimiter='\t')
        
        # Leer cada fila del archivo CSV
        for row in reader:
            # Verificar si la fila tiene elementos
            if row:
                # Obtener las letras de la columna 1
                letra = row[0]
                # Obtener el valor de la columna 2
                valor_col_2 = int(row[1])
                # Obtener el valor máximo y mínimo para la letra correspondiente
                maximo, minimo = diccionario_max_min_col_1_2.get(letra, (valor_col_2, valor_col_2))
                diccionario_max_min_col_1_2[letra] = (max(valor_col_2, maximo), min(valor_col_2, minimo))

    # Convertir el diccionario en una lista de tuplas
    resultados_5 = [(letra, maximo, minimo) for letra, (maximo, minimo) in diccionario_max_min_col_1_2.items()]

    # Ordenar la lista de tuplas alfabéticamente
    resultados_5 = sorted(resultados_5, key=lambda x: x[0])    

    return  resultados_5


def pregunta_06():
    """
    La columna 5 codifica un diccionario donde cada cadena de tres letras corresponde a
    una clave y el valor despues del caracter `:` corresponde al valor asociado a la
    clave. Por cada clave, obtenga el valor asociado mas pequeño y el valor asociado mas
    grande computados sobre todo el archivo.

    Rta/
    [
        ("aaa", 1, 9),
        ("bbb", 1, 9),
        ("ccc", 1, 10),
        ("ddd", 0, 9),
        ("eee", 1, 7),
        ("fff", 0, 9),
        ("ggg", 3, 10),
        ("hhh", 0, 9),
        ("iii", 0, 9),
        ("jjj", 5, 17),
    ]

    """
    # Diccionario para almacenar el valor asociado más pequeño y el valor asociado más grande por cada clave
    diccionario_col_5 = {}

    # Abrir el archivo CSV en modo lectura
    with open(file_csv, 'r') as file:
        # Crear un lector CSV con el delimitador especificado
        reader = csv.reader(file, delimiter='\t')
        
        # Leer cada fila del archivo CSV
        for row in reader:
            # Verificar si la fila tiene elementos
            if row:
                # Separar el diccionario de la columna 5 en claves y valores
                claves_valores = row[4].split(',')
                # Iterar sobre las claves y valores
                for clave_valor in claves_valores:
                    # Separar la clave y el valor
                    clave, valor = clave_valor.split(':')
                    # Convertir el valor a entero
                    valor = int(valor)
                    # Obtener el valor asociado más pequeño y el valor asociado más grande por cada clave
                    minimo, maximo = diccionario_col_5.get(clave, (valor, valor))
                    diccionario_col_5[clave] = (min(valor, minimo), max(valor, maximo))

    # Convertir el diccionario en una lista de tuplas
    resultados_6 = [(clave, minimo, maximo) for clave, (minimo, maximo) in diccionario_col_5.items()]

    # Ordenar la lista de tuplas alfabéticamente
    resultados_6 = sorted(resultados_6, key=lambda x: x[0])
      
    return resultados_6


def pregunta_07():
    """
    Retorne una lista de tuplas que asocien las columnas 0 y 1. Cada tupla contiene un
    valor posible de la columna 2 y una lista con todas las letras asociadas (columna 1)
    a dicho valor de la columna 2.

    Rta/
    [
        (0, ["C"]),
        (1, ["E", "B", "E"]),
        (2, ["A", "E"]),
        (3, ["A", "B", "D", "E", "E", "D"]),
        (4, ["E", "B"]),
        (5, ["B", "C", "D", "D", "E", "E", "E"]),
        (6, ["C", "E", "A", "B"]),
        (7, ["A", "C", "E", "D"]),
        (8, ["E", "D", "E", "A", "B"]),
        (9, ["A", "B", "E", "A", "A", "C"]),
    ]

    """
    # Diccionario para almacenar las letras asociadas a cada valor posible de la columna 2
    diccionario_col_2 = {}

    # Abrir el archivo CSV en modo lectura
    with open(file_csv, 'r') as file:
        # Crear un lector CSV con el delimitador especificado
        reader = csv.reader(file, delimiter='\t')
        
        # Leer cada fila del archivo CSV
        for row in reader:
            # Verificar si la fila tiene elementos
            if row:
                # Obtener el valor de la columna 2
                valor_col_2 = int(row[1])
                # Obtener la letra de la columna 1
                letra = row[0]
                # Obtener la lista de letras asociadas al valor de la columna 2
                letras = diccionario_col_2.get(valor_col_2, [])
                letras.append(letra)
                diccionario_col_2[valor_col_2] = letras

    # Convertir el diccionario en una lista de tuplas
    resultados_7 = [(valor, letras) for valor, letras in diccionario_col_2.items()]

    # Ordenar la lista de tuplas alfabéticamente
    resultados_7 = sorted(resultados_7, key=lambda x: x[0])

    return resultados_7


def pregunta_08():
    """
    Genere una lista de tuplas, donde el primer elemento de cada tupla contiene  el valor
    de la segunda columna; la segunda parte de la tupla es una lista con las letras
    (ordenadas y sin repetir letra) de la primera  columna que aparecen asociadas a dicho
    valor de la segunda columna.

    Rta/
    [
        (0, ["C"]),
        (1, ["B", "E"]),
        (2, ["A", "E"]),
        (3, ["A", "B", "D", "E"]),
        (4, ["B", "E"]),
        (5, ["B", "C", "D", "E"]),
        (6, ["A", "B", "C", "E"]),
        (7, ["A", "C", "D", "E"]),
        (8, ["A", "B", "D", "E"]),
        (9, ["A", "B", "C", "E"]),
    ]

    """
    # Diccionario para almacenar las letras asociadas a cada valor posible de la columna 2
    diccionario_col_2 = {}

    # Abrir el archivo CSV en modo lectura
    with open(file_csv, 'r') as file:
        # Crear un lector CSV con el delimitador especificado
        reader = csv.reader(file, delimiter='\t')
        
        # Leer cada fila del archivo CSV
        for row in reader:
            # Verificar si la fila tiene elementos
            if row:
                # Obtener el valor de la columna 2
                valor_col_2 = int(row[1])
                # Obtener la letra de la columna 1
                letra = row[0]
                # Obtener la lista de letras asociadas al valor de la segunda columna
                letras = diccionario_col_2.get(valor_col_2, [])
                letras.append(letra)
                diccionario_col_2[valor_col_2] = list(set(letras))

    # Convertir el diccionario en una lista de tuplas
    resultados_8 = [(valor, letras) for valor, letras in diccionario_col_2.items()]

    # Ordenar la lista de tuplas alfabéticamente
    resultados_8 = sorted(resultados_8, key=lambda x: x[0])
    # resultados_8 = sorted(resultados_8, key=lambda x:(x[0], x[1]))

    return resultados_8


def pregunta_09():
    """
    Retorne un diccionario que contenga la cantidad de registros en que aparece cada
    clave de la columna 5.

    Rta/
    {
        "aaa": 13,
        "bbb": 16,
        "ccc": 23,
        "ddd": 23,
        "eee": 15,
        "fff": 20,
        "ggg": 13,
        "hhh": 16,
        "iii": 18,
        "jjj": 18,
    }

    """
    # Diccionario para almacenar la cantidad de registros en que aparece cada clave de la columna 5
    resultados_9 = {}

    # Abrir el archivo CSV en modo lectura
    with open(file_csv, 'r') as file:
        # Crear un lector CSV con el delimitador especificado
        reader = csv.reader(file, delimiter='\t')
        
        # Leer cada fila del archivo CSV
        for row in reader:
            # Verificar si la fila tiene elementos
            if row:
                # Separar el diccionario de la columna 5 en claves y valores
                claves_valores = row[4].split(',')
                # Iterar sobre las claves
                for clave_valor in claves_valores:
                    # Separar la clave y el valor
                    clave, _ = clave_valor.split(':')
                    # Incrementar la cantidad para la clave correspondiente
                    resultados_9[clave] = resultados_9.get(clave, 0) + 1
    
    resultados_9 = dict(sorted(resultados_9.items()))

    return resultados_9


def pregunta_10():
    """
    Retorne una lista de tuplas contengan por cada tupla, la letra de la columna 1 y la
    cantidad de elementos de las columnas 4 y 5.

    Rta/
    [
        ("E", 3, 5),
        ("A", 3, 4),
        ("B", 4, 4),
        ...
        ("C", 4, 3),
        ("E", 2, 3),
        ("E", 3, 3),
    ]


    """
    # Lista para almacenar las tuplas con la letra de la columna 1 y la cantidad de elementos de las columnas 4 y 5
    resultados_10 = []

    # Abrir el archivo CSV en modo lectura
    with open(file_csv, 'r') as file:
        # Crear un lector CSV con el delimitador especificado
        reader = csv.reader(file, delimiter='\t')
        
        # Leer cada fila del archivo CSV
        for row in reader:
            # Verificar si la fila tiene elementos
            if row:
                # Obtener la letra de la columna 1
                letra = row[0]
                # Separar los elementos de la columna 4
                elementos = row[3].split(',')
                # Separar el diccionario de la columna 5 en claves y valores
                claves_valores = row[4].split(',')
                # Obtener la cantidad de elementos de las columnas 4 y 5
                cantidad_col_4 = len(elementos)
                cantidad_col_5 = len(claves_valores)
                # Agregar la tupla a la lista de resultados
                resultados_10.append((letra, cantidad_col_4, cantidad_col_5))

    return resultados_10


def pregunta_11():
    """
    Retorne un diccionario que contengan la suma de la columna 2 para cada letra de la
    columna 4, ordenadas alfabeticamente.

    Rta/
    {
        "a": 122,
        "b": 49,
        "c": 91,
        "d": 73,
        "e": 86,
        "f": 134,
        "g": 35,
    }


    """
    # Diccionario para almacenar la suma de la columna 2 para cada letra de la columna 4
    resultados_11 = {}

    # Abrir el archivo CSV en modo lectura
    with open(file_csv, 'r') as file:
        # Crear un lector CSV con el delimitador especificado
        reader = csv.reader(file, delimiter='\t')
        
        # Leer cada fila del archivo CSV
        for row in reader:
            # Verificar si la fila tiene elementos
            if row:
                # Separar los elementos de la columna 4
                elementos = row[3].split(',')
                # Obtener la letra de la columna 1
                letra = row[0]
                # Obtener el valor de la columna 2
                valor_col_2 = int(row[1])
                # Iterar sobre los elementos de la columna 4
                for elemento in elementos:
                    # Convertir la letra a minúsculas
                    elemento = elemento.lower()
                    # Incrementar la suma para la letra correspondiente
                    resultados_11[elemento] = resultados_11.get(elemento, 0) + valor_col_2

    resultados_11 = dict(sorted(resultados_11.items()))

    return resultados_11


def pregunta_12():
    """
    Genere un diccionario que contengan como clave la columna 1 y como valor la suma de
    los valores de la columna 5 sobre todo el archivo.

    Rta/
    {
        'A': 177,
        'B': 187,
        'C': 114,
        'D': 136,
        'E': 324
    }

    """
    # Diccionario para almacenar la suma de los valores de la columna 5 para cada letra de la columna 1
    resultados_12 = {}

    # Abrir el archivo CSV en modo lectura
    with open(file_csv, 'r') as file:
        # Crear un lector CSV con el delimitador especificado
        reader = csv.reader(file, delimiter='\t')
        
        # Leer cada fila del archivo CSV
        for row in reader:
            # Verificar si la fila tiene elementos
            if row:
                # Obtener la letra de la columna 1
                letra = row[0]
                # Separar el diccionario de la columna 5 en claves y valores
                claves_valores = row[4].split(',')
                # Iterar sobre las claves y valores
                for clave_valor in claves_valores:
                    # Separar la clave y el valor
                    _, valor = clave_valor.split(':')
                    # Convertir el valor a entero
                    valor = int(valor)
                    # Incrementar la suma para la letra correspondiente
                    resultados_12[letra] = resultados_12.get(letra, 0) + valor

    resultados_12 = dict(sorted(resultados_12.items()))

    return resultados_12
