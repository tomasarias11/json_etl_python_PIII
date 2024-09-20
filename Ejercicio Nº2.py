import json
import requests
import matplotlib.pyplot as plt

def bar_plot(lista_userId, lista_completed):
    # Función que genera el gráfico de barras
    fig = plt.figure()
    fig.suptitle('Títulos completados por usuario', fontsize=16)
    ax = fig.add_subplot()

    # Generar el gráfico de barras
    ax.bar(lista_userId, lista_completed, label='Cantidad de títulos')
    ax.set_facecolor('whitesmoke')
    ax.legend()

    # Mostrar el gráfico
    plt.xlabel("Usuarios")
    plt.ylabel("Títulos Completados")
    plt.show()

if __name__ == '__main__':
    print("Bienvenidos a otra clase con Python")
    
    # URL de la API para obtener los datos
    url = "https://jsonplaceholder.typicode.com/todos"

    # Hacer la solicitud GET a la API
    response = requests.get(url)

    # Convertir la respuesta a JSON
    data = json.loads(response.text)

    # Listas para almacenar los datos de userId y cantidad de títulos completados
    lista_userId = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    lista_completed = []

    # Recorrer los 10 usuarios y contar cuántos títulos completó cada uno
    for i in lista_userId:
        suma = 0
        for user in data:
            if user['userId'] == i and user['completed']:
                suma += 1
        lista_completed.append(suma)
    
    # Mostrar el gráfico de barras con los datos recolectados
    bar_plot(lista_userId, lista_completed)

    print("Actividad completada.")