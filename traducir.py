"""
El programa debe tener la capacidad de:
1. Agregar nuevas traducciones
2. Traducir al idioma de la siguiente forma codigo origen, codigo destino y palabra
    EN-ES dog --> perro
    ES-EN perro --> dog
"""

diccionario_con_palabras_en_ingles = {
    "Rojo": "Red",
    "Lenguaje": "Language",
    "Escuela": "School",
    "Perro": "Dog",
    "Gato": "Cat"
}

opcion = 0
while opcion != 4:
    print("Elija una opcion")
    print("\n1. Traducir de ESP-ING \n2. Traducir de ING-ESP \n3. Agregar una Palabra\n4. Salir")
    opcion = int(input("Elija una opción a realizar: "))
    
    if (opcion == 1):
        palabra = input("Escriba la palabra a Traducir \n")
        if diccionario_con_palabras_en_ingles.get(palabra)!= None:
            print(palabra, "-›", diccionario_con_palabras_en_ingles.get(palabra))
        else:
            print("La palabra no existe")
    elif (opcion == 2):
        palabra = input("Escriba la palabra a Traducir \n")
        encontrado = False
        for key in diccionario_con_palabras_en_ingles.keys():
            if palabra == diccionario_con_palabras_en_ingles[key]:
                print(palabra, "-->", key)
                encontrado = True
                break
        if encontrado == False:
            print("La palabra no existe")
    elif (opcion == 3):
        palabra = input("Ingresa la palabra en Español \n")
        if diccionario_con_palabras_en_ingles.get(palabra) == None:
            traduccion = input("Escribe la traduccion en Ingles \n")
            diccionario_con_palabras_en_ingles.update({palabra:traduccion})
            print("La palabra fue agregada con exito")
        else:
            print("La palabra ya fue agregada en el diccionario")

#Video en el cual me inspire para lograr hacer mi traductor con python

#https://youtu.be/1nMwohcIZgo?si=mpvDC_6tMeVLvlgN