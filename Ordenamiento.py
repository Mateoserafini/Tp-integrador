import time
import random
import sys

sys.setrecursionlimit(1000000)

# ---------- GENERADOR DE LISTA DESORDENADA ----------
def crear_lista_aleatoria(n):
    """Genera una lista de n números aleatorios únicos."""
    return random.sample(range(1, n * 10), n)


# ---------- MÉTODOS DE ORDENAMIENTO ----------

def bubble_sort(arr):
    a = arr.copy()
    n = len(a)
    for i in range(n):
        for j in range(0, n - i - 1):
            if a[j] > a[j + 1]:
                a[j], a[j + 1] = a[j + 1], a[j]
    return a

def quick_sort(arr):
    a = arr.copy()
    if len(a) <= 1:
        return a
    pivot = a[0]
    menores = [x for x in a[1:] if x < pivot]
    mayores = [x for x in a[1:] if x >= pivot]
    return quick_sort(menores) + [pivot] + quick_sort(mayores)

def selection_sort(arr):
    a = arr.copy()
    n = len(a)
    for i in range(n):
        min_idx = i
        for j in range(i + 1, n):
            if a[j] < a[min_idx]:
                min_idx = j
        a[i], a[min_idx] = a[min_idx], a[i]
    return a

def insertion_sort(arr):
    a = arr.copy()
    for i in range(1, len(a)):
        clave = a[i]
        j = i - 1
        while j >= 0 and clave < a[j]:
            a[j + 1] = a[j]
            j -= 1
        a[j + 1] = clave
    return a


# ---------- FUNCIÓN PRINCIPAL ----------
def main():
    n = int(input("¿Cuántos números aleatorios quieres generar?: "))
    lista = crear_lista_aleatoria(n)

    print("\n--- ORDENAMIENTOS ---")

    # Bubble Sort
    inicio = time.time()
    bubble_sort(lista)
    fin = time.time()
    print(f"Bubble Sort:          {fin - inicio:.6f} segundos")

    # Quick Sort
    inicio = time.time()
    quick_sort(lista)
    fin = time.time()
    print(f"Quick Sort:           {fin - inicio:.6f} segundos")

    # Selection Sort
    inicio = time.time()
    selection_sort(lista)
    fin = time.time()
    print(f"Selection Sort:       {fin - inicio:.6f} segundos")

    # Insertion Sort
    inicio = time.time()
    insertion_sort(lista)
    fin = time.time()
    print(f"Insertion Sort:       {fin - inicio:.6f} segundos")


if __name__ == "__main__":
    main()
