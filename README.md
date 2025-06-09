# 📁 Algoritmos de Búsqueda y Ordenamiento en Python

Este proyecto contiene dos scripts en Python que implementan y comparan distintos **algoritmos de búsqueda** y **ordenamiento** sobre listas de números enteros.

## 📄 Archivos

### `Busquedas.py`
Contiene funciones para realizar búsquedas en listas, así como la comparación de tiempos de ejecución.

#### Algoritmos implementados:
- **Búsqueda Lineal Iterativa**
- **Búsqueda Lineal Recursiva**
- **Búsqueda Binaria Iterativa**
- **Búsqueda Binaria Recursiva**

#### Cómo funciona:
1. El usuario elige el tamaño de la lista y el número a buscar.
2. Selecciona si desea una lista ordenada secuencialmente o una lista aleatoria ordenada.
3. Se aplican los 4 algoritmos de búsqueda sobre la lista.
4. Se imprime si el número fue encontrado y el tiempo de ejecución de cada algoritmo.

---

### `Ordenamiento.py`
Contiene funciones para ordenar listas de números utilizando distintos algoritmos y medir su rendimiento.

#### Algoritmos implementados:
- **Bubble Sort**
- **Quick Sort**
- **Selection Sort**
- **Insertion Sort**

#### Cómo funciona:
1. El usuario ingresa el número de elementos aleatorios a generar.
2. Se genera una lista desordenada con números únicos.
3. Cada algoritmo ordena la lista y se mide el tiempo de ejecución.

---

## ▶️ Ejecución

Puedes ejecutar cualquiera de los archivos desde la terminal:

```bash
python Busquedas.py
```

```bash
python Ordenamiento.py
```

---

## 📌 Requisitos

- Python 3.x
- No se requieren librerías externas

---

## 🧠 Notas

- Los algoritmos binarios requieren que la lista esté ordenada para funcionar correctamente.
- Se usa `time.time()` para medir el rendimiento de cada algoritmo.
- `sys.setrecursionlimit(1000000)` se establece para evitar errores de recursión profunda en listas grandes.
