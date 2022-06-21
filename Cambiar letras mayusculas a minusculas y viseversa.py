def palabra(cadena):
    palabras = ""
    for cad in cadena:
        if cad == cad.upper():
            palabras += cad.lower()
        else:
            palabras += cad.upper()
    return palabras


cadenas = input("dijite la cadena de texto: ")
print(palabra(cadenas))