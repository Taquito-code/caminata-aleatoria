# Simulación Monte Carlo: Caminata Aleatoria (Random Walk)

Proyecto práctico enfocado en el análisis probabilístico y simulación de eventos aleatorios utilizando **Python Intermedio**, **NumPy** y **Matplotlib**.

## Objetivo del Proyecto
Modelar y evaluar el comportamiento de 500 caminatas aleatorias independientes de 100 pasos cada una para calcular la probabilidad empírica de alcanzar un objetivo determinado (Escalón 60+), incorporando condiciones límite y variables de riesgo.

---

## Conceptos de Python & NumPy Aplicados
* **Indexación y Slicing Avanzado:** Extracción de filas/columnas específicas en matrices bidimensionales (`ends = np_aw_t[-1, :]`).
* **Álgebra Matricial:** Uso de transposición de matrices (`np.transpose()`) para reestructurar series temporales de datos.
* **Vectorización y Máscaras Booleanas:** Filtrado eficiente de datos sin bucles adicionales (`np.sum(ends >= 60)`).
* **Generación de Números Pseudoaleatorios:** Control de semillas (`np.random.seed()`) para reproducibilidad de experimentos.
* **Visualización de Datos:** Creación y customización de histogramas de frecuencias con **Matplotlib**.

---

## Reglas de la Simulación
Cada paso dentro de una caminata de 100 iteraciones sigue estas reglas probabilísticas:

| Evento (Dado 1-6) | Probabilidad | Acción en la Caminata |
| :--- | :--- | :--- |
| **1 o 2** | 33.3% | Retrocede 1 escalón (límite inferior en 0). |
| **3, 4 o 5** | 50.0% | Avanza 1 escalón. |
| **6** | 16.7% | Avanza $1 + \text{random}(1,6)$ escalones. |
| **Tropezón** | 0.1% | Caída inmediata al origen (Escalón 0). |

---

## Resultados y Visualización
Tras ejecutar 500 simulaciones:
* **Éxito (Escalón $\ge 60$):** ~78.4% de probabilidad.
* La distribución muestra un sesgo positivo hacia adelante debido a la regla del dado 6, a pesar del riesgo implícito de tropezar.

El script genera automáticamente el archivo `histograma_caminata.png` con la distribución de frecuencias.

---

## Cómo Ejecutar el Proyecto

1. **Clonar el repositorio:**
   ```bash
   git clone [https://github.com/taquito-code/caminata-aleatoria.git](https://github.com/taquito-code/caminata-aleatoria.git)
   cd caminata-aleatoria