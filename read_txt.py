import pandas as pd
import os
import re


def read_txt(path, pattern):

    # list comprehension to read all files in a path
    files = [file for file in os.listdir(path)]

    # creating empty list
    importe = []
    nombre = []
    archivo = []

    # the first loop is created to read files in a path
    for file in files:
        f = open(path+file, "r", encoding="utf8")

        # the second one is created to read line in the file
        for line in f:
          resultado = re.match(pattern, line)
          if resultado:
            importe.append(resultado.group(1))
            nombre.append(resultado.group(2))
            archivo.append(file)
        f.close()

    return (nombre, importe, archivo)


if __name__ == '__main__':
    # It is needed a path and a pattern (RegEx)
    ruta = '2022_09_15/PEM/'
    pattern = re.compile(r'^[\d]{9}[\s]{16}[\d]{12}[\s]{10}([\d]{15})([A-Za-z\s]*).*$')
    listas = read_txt(path=ruta, pattern=pattern)

    # Lists are used to create a new DataFrame
    df_pem = pd.DataFrame(
            {
            'Nombre':listas[0],
            'Importe':listas[1],
            'Archivo':listas[2]
            }
            )
    df_pem['Importe'] = df_pem['Importe'].astype('int')
    df_pem['Importe'] = df_pem['Importe'].apply(lambda x: x/100)
    df_pem.head(10)
