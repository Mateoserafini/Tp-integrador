import time
import random
import sys

sys.setrecursionlimit(1000000)
# ---------- GENERADORES DE LISTAS ----------

def crear_lista_secuencial(n):
    """Lista ordenada del 1 a n."""
    return list(range(1, n + 1))

def crear_lista_aleatoria(n):
    """Lista ordenada de n números aleatorios únicos."""
    return sorted(random.sample(range(1, n * 10), n))


# ---------- MÉTODOS DE BÚSQUEDA ----------

def busqueda_lineal_iterativa(lista, objetivo):
    for i in range(len(lista)):
        if lista[i] == objetivo:
            return i
    return -1

def busqueda_lineal_recursiva(lista, objetivo, indice=0):
    if indice >= len(lista):
        return -1
    if lista[indice] == objetivo:
        return indice
    return busqueda_lineal_recursiva(lista, objetivo, indice + 1)

def busqueda_binaria_iterativa(lista, objetivo):
    izquierda = 0
    derecha = len(lista) - 1
    while izquierda <= derecha:
        medio = (izquierda + derecha) // 2
        if lista[medio] == objetivo:
            return medio
        elif lista[medio] < objetivo:
            izquierda = medio + 1
        else:
            derecha = medio - 1
    return -1

def busqueda_binaria_recursiva(lista, objetivo, izquierda=0, derecha=None):
    if derecha is None:
        derecha = len(lista) - 1
    if izquierda > derecha:
        return -1
    medio = (izquierda + derecha) // 2
    if lista[medio] == objetivo:
        return medio
    elif lista[medio] < objetivo:
        return busqueda_binaria_recursiva(lista, objetivo, medio + 1, derecha)
    else:
        return busqueda_binaria_recursiva(lista, objetivo, izquierda, medio - 1)


# ---------- FUNCION PRINCIPAL ----------

def main():
    n = int(input("¿Cuántos elementos quieres en la lista?: "))
    objetivo = int(input("¿Qué número deseas buscar?: "))
    tipo_lista = input("¿Qué tipo de lista quieres? (secuencial / aleatoria): ").strip().lower()

    # Crear lista
    if tipo_lista == "aleatoria":
        lista = crear_lista_aleatoria(n)
    else:
        lista = crear_lista_secuencial(n)

    print("\n--- RESULTADOS ---")

    # Búsqueda lineal iterativa
    inicio = time.time()
    resultado = busqueda_lineal_iterativa(lista, objetivo)
    fin = time.time()
    print(f"Lineal Iterativa:     {'Encontrado en índice ' + str(resultado) if resultado != -1 else 'No encontrado'}")
    print(f"Tiempo: {fin - inicio:.6f} segundos")

    # Búsqueda lineal recursiva
    inicio = time.time()
    resultado = busqueda_lineal_recursiva(lista, objetivo)
    fin = time.time()
    print(f"Lineal Recursiva:     {'Encontrado en índice ' + str(resultado) if resultado != -1 else 'No encontrado'}")
    print(f"Tiempo: {fin - inicio:.6f} segundos")

    # Búsqueda binaria iterativa
    inicio = time.time()
    resultado = busqueda_binaria_iterativa(lista, objetivo)
    fin = time.time()
    print(f"Binaria Iterativa:    {'Encontrado en índice ' + str(resultado) if resultado != -1 else 'No encontrado'}")
    print(f"Tiempo: {fin - inicio:.6f} segundos")

    # Búsqueda binaria recursiva
    inicio = time.time()
    resultado = busqueda_binaria_recursiva(lista, objetivo)
    fin = time.time()
    print(f"Binaria Recursiva:    {'Encontrado en índice ' + str(resultado) if resultado != -1 else 'No encontrado'}")
    print(f"Tiempo: {fin - inicio:.6f} segundos")


if __name__ == "__main__":
    main()
