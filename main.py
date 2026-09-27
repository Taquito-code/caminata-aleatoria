import matplotlib.pyplot as plt
import numpy as np

# Fijar la semilla para reproducibilidad
np.random.seed(123)

# 1. Simular la caminata aleatoria 500 veces
all_walks = []
for i in range(500):
    random_walk = [0]
    for x in range(100):
        step = random_walk[-1]
        dice = np.random.randint(1, 7)

        if dice <= 2:
            step = max(0, step - 1)
        elif dice <= 5:
            step = step + 1
        else:
            step = step + np.random.randint(1, 7)

        # 0.1% de probabilidad de tropezar y caer al inicio
        if np.random.rand() <= 0.001:
            step = 0

        random_walk.append(step)
    all_walks.append(random_walk)

# 2. Trasponer la matriz para organizar los datos
np_aw_t = np.transpose(np.array(all_walks))

# 3. Seleccionar la última fila (escalón final tras 100 pasos)
ends = np_aw_t[-1, :]

# 4. Calcular estadísticas
exitos = np.sum(ends >= 60)
porcentaje = (exitos / 500) * 100

print(f"Caminatas que alcanzaron el escalón 60 o más: {exitos} de 500")
print(f"Probabilidad estimada: {porcentaje:.1f}%")

# 5. Graficar el histograma de resultados finales
plt.hist(ends, bins=15, edgecolor="black")
plt.axvline(
    x=60,
    color="red",
    linestyle="--",
    linewidth=2,
    label="Meta (Escalón 60)",
)
plt.title("Distribución de posiciones finales tras 100 pasos")
plt.xlabel("Escalón alcanzado")
plt.ylabel("Frecuencia (N° de caminatas)")
plt.legend()

# Guardar la imagen del gráfico
plt.savefig("histograma_caminata.png")
print("Gráfico guardado como 'histograma_caminata.png'")

plt.show()