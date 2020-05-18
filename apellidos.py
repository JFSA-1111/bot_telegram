# -*- coding: utf-8 -*-
import csv
import re
from unicodedata import normalize


def apellido(name):
    nombres_array = name.split()
    nombres_array = [x.lower() for x in nombres_array]

    for i in range(len(nombres_array)):
        nombres_array[i] = re.sub(
            r"([^n\u0300-\u036f]|n(?!\u0303(?![\u0300-\u036f])))[\u0300-\u036f]+",
            r"\1",
            normalize("NFD", nombres_array[i]), 0, re.I
        )

    with open('numbers3.csv', newline='') as File:
        reader = csv.reader(File)
        apellidos = []
        for row in reader:
            for apellido in row:
                if apellido in nombres_array:
                    apellidos.append(apellido.capitalize())
        if not apellidos:
            apellidos.append('No conozco ese apellido')
    return apellidos
