# Programas modulación AM, FM y PM
import numpy as np
import matplotlib.pyplot as plt
from scipy.signal import hilbert

def generar_señal_senoidal(amplitud, frecuencia, tiempos):
  return amplitud * np.sin(2 * np.pi * frecuencia * tiempos)

def main():
  # Solicitar al usuario que especifique las entradas
  n = int(input("(Recomendado: 3-5) ¿Cuántas señales desea generar? "))
  a_min = float(input("(Recomendado: 1) Amplitud mínima: "))
  a_max = float(input("(Recomendado: 5) Amplitud máxima: "))
  f_min = float(input("(Recomendado: 1) Frecuencia mínima: "))
  f_max = float(input("(Recomendado: 5) Frecuencia máxima: "))

  # Generar los tiempos
  tiempos = np.linspace(0, 1, 1000)

  # Generar las señales sinusoidales
  señales = []
  frecuencias = []
  for i in range(n):
    amplitud = np.random.uniform(low=a_min, high=a_max)
    frecuencia = np.random.uniform(low=f_min, high=f_max)
    señales.append(generar_señal_senoidal(amplitud, frecuencia, tiempos))
    frecuencias.append(frecuencia)

  # Sumar las señales
  señal_compuesta = np.sum(señales, axis=0)

  # Encontrar la frecuencia máxima
  frec_max = max(frecuencias)

  # Graficar las señales individuales
  fig, axs = plt.subplots(n // 3 + 1, 3, figsize=(19, 13))
  axs = np.array(axs) # Asegurarse de que axs siempre sea un array
  for i in range(n):
    ax = axs.flatten()[i] # Usar flatten() para convertir axs en un array unidimensional
    ax.plot(tiempos, señales[i], label="Señal %d" % (i + 1), color=plt.cm.Spectral(np.random.rand()))
    ax.set_title("Señal %d" % (i + 1))
    ax.set_xlabel("Tiempo (s)")
    ax.set_ylabel("Amplitud")
    ax.legend()

  # Graficar la señal compuesta
  fig, ax = plt.subplots(1, 1, figsize=(9,9))
  ax.plot(tiempos, señal_compuesta)
  ax.set_title("Señal compuesta")
  ax.set_xlabel("Tiempo (s)")
  ax.set_ylabel("Amplitud")

  # Generar la señal portadora
  amplitud_portadora = a_max
  frecuencia_portadora = f_max * n * n # Hz
  portadora = amplitud_portadora * np.sin(2 * np.pi * frecuencia_portadora * tiempos)

  # Generar la señal moduladora
  señal_moduladora = generar_señal_senoidal(a_min, f_max, tiempos)

  # Modular la señal AM, con un valor k que puede ir de 0 a 1
  k = float(input("Ingrese el índice de Modulación AM entre 0 y 1: ")) # Un valor cercano a cero indica modulación AM de baja profundidad y uno de alta profundidad.
  am = portadora * (1 + k * señal_moduladora)

  # Calcular la envolvente usando la transformada de Hilbert
  envolvente = np.abs(hilbert(am))

  # Graficar las señales en un subplot para AM
  fig, axs = plt.subplots(4, figsize=(19,13))

  # Ajustar el espacio entre las gráficas
  plt.subplots_adjust(hspace = 0.5)

  # Graficar la señal portadora
  axs[0].plot(tiempos, portadora)
  axs[0].set_title('Señal Portadora')
  axs[0].set_xlabel("Tiempo (s)")
  axs[0].set_ylabel("Amplitud")

  # Graficar la señal moduladora
  axs[1].plot(tiempos, señal_moduladora)
  axs[1].set_title('Señal Moduladora')
  axs[1].set_xlabel("Tiempo (s)")
  axs[1].set_ylabel("Amplitud")

  # Graficar la señal compuesta y la señal moduladaora en el mismo gráfico
  axs[2].plot(tiempos, señal_compuesta, label="Señal Compuesta", color="red")
  axs[2].plot(tiempos, señal_moduladora, label="Señal Moduladora", color="blue")
  axs[2].plot(tiempos, am, label='Señal Modulada AM', color="green")

  axs[2].set_title('Señales Moduladora y Compuesta')
  axs[2].set_xlabel("Tiempo (s)")
  axs[2].set_ylabel("Amplitud")
  axs[2].legend()

  # Graficar la señal modulada en AM con su envolvente
  axs[3].plot(tiempos, am, label='Señal Modulada AM')
  axs[3].plot(tiempos, envolvente, label='Envolvente', color='red')
  axs[3].set_title('Señal Modulada AM con Envolvente')
  axs[3].set_xlabel("Tiempo (s)")
  axs[3].set_ylabel("Amplitud")
  axs[3].legend()

  # Generar la señal FM
  k_fm = float(input("Ingrese el índice de Modulación para FM: ")) # Un valor cercano a 0 indica modulación FM de baja profundidad y 1 de alta profundidad.
  fm = amplitud_portadora * np.sin(2 * np.pi * frecuencia_portadora * tiempos + k_fm * np.sin(2 * np.pi * f_max * tiempos)) # A diferencia AM, FM puede usar valores < 1 (modulación FM de banda ancha)

  # Graficar las señales en un subplot para FM
  fig, axs = plt.subplots(3, figsize=(19,13))

  # Ajustar el espacio entre las gráficas
  plt.subplots_adjust(hspace = 0.5)

  # Graficar la señal portadora
  axs[0].plot(tiempos, portadora)
  axs[0].set_title('Señal Portadora')
  axs[0].set_xlabel("Tiempo (s)")
  axs[0].set_ylabel("Amplitud")

  # Graficar la señal moduladora
  axs[1].plot(tiempos, señal_moduladora)
  axs[1].set_title('Señal Moduladora')
  axs[1].set_xlabel("Tiempo (s)")
  axs[1].set_ylabel("Amplitud")

  # Graficar la señal modulada en FM
  axs[2].plot(tiempos, fm)
  axs[2].set_title('Señal Modulada FM')
  axs[2].set_xlabel("Tiempo (s)")
  axs[2].set_ylabel("Amplitud")

  # Generar la señal PM
  pm = amplitud_portadora * np.sin(2 * np.pi * frecuencia_portadora * tiempos + k * señal_compuesta)

  # Graficar las señales en un subplot para PM
  fig, axs = plt.subplots(3, figsize=(19,13))

  # Ajustar el espacio entre las gráficas
  plt.subplots_adjust(hspace = 0.5)

  # Graficar la señal portadora
  axs[0].plot(tiempos, portadora)
  axs[0].set_title('Señal Portadora')
  axs[0].set_xlabel("Tiempo (s)")
  axs[0].set_ylabel("Amplitud")

  # Graficar la señal moduladora
  axs[1].plot(tiempos, señal_moduladora)
  axs[1].set_title('Señal Moduladora')
  axs[1].set_xlabel("Tiempo (s)")
  axs[1].set_ylabel("Amplitud")

  # Graficar la señal modulada en PM
  axs[2].plot(tiempos, pm)
  axs[2].set_title('Señal Modulada PM')
  axs[2].set_xlabel("Tiempo (s)")
  axs[2].set_ylabel("Amplitud")

  plt.show()

if __name__ == "__main__":
    main()
"""
Para notar la diferencia entre la FM Y la PM
(Recomendado: 3-5) ¿Cuántas señales desea generar? 1
(Recomendado: 1) Amplitud mínima: 1
(Recomendado: 5) Amplitud máxima: 1
(Recomendado: 1) Frecuencia mínima: 5
(Recomendado: 5) Frecuencia máxima: 5
Ingrese el índice de Modulación AM entre 0 y 1: 0.5
Ingrese el índice de Modulación para FM: 0.1
"""
