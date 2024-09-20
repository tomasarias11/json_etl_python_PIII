import json

def serializar():
    print("Función que genera un archivo JSON")
    
    # JSON Serialize
    # Armar un JSON que represente los datos personales
    # nombre, apellido, DNI
    # Además, debe tener una lista de prendas con al menos 2 prendas

    mipersona = {
        "nombre": "Tomas",
        "apellido": "Arias",
        "DNI": "43440783",
        "elementos_vestir": [
            {"prenda": "chaleco", "cantidad": 2},
            {"prenda": "zapato", "cantidad": 5}
        ]
    }

    # Serializamos el diccionario en un archivo JSON
    with open('mi_persona_json.json', 'w') as jsonfile:
        json.dump(mipersona, jsonfile, indent=4)

    print("Archivo 'mi_persona_json.json' creado correctamente.")


def deserializar():
    print("Función que lee un archivo JSON")
    
    # JSON Deserialize
    # Leemos el archivo JSON y lo convertimos a un objeto Python
    try:
        with open('mi_persona_json.json', 'r') as jsonfile:
            json_data = json.load(jsonfile)

        # Convertimos el objeto Python a un string JSON formateado
        json_string = json.dumps(json_data, indent=4)

        # Mostramos el contenido del archivo JSON
        print("Contenido del archivo 'mi_persona_json.json':")
        print(json_string)

    except FileNotFoundError:
        print("El archivo 'mi_persona_json.json' no se encuentra. Primero debes ejecutar la función serializar().")


if __name__ == '__main__':
    print("Bienvenidos a otra clase con Python")
    
    # Ejecutamos las funciones
    serializar()
    deserializar()

    print("Hemos terminado")

    input("Muchas gracias por revisarlo")