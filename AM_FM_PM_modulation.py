# AM, FM, PM, ASK, FSK and PSK modulation programs: AM, FM and PM modulation
import numpy as np
import matplotlib.pyplot as plt
from scipy.signal import hilbert

def generate_sinusoidal_signal(amplitude, frequency, times):
  return amplitude * np.sin(2 * np.pi * frequency * times)

def main():
  # Ask the user to specify the inputs
  n = int(input("(Recommended: 3-5) How many signals do you want to generate? "))
  a_min = float(input("(Recommended: 1) Minimum amplitude: "))
  a_max = float(input("(Recommended: 5) Maximum amplitude: "))
  f_min = float(input("(Recommended: 1) Minimum frequency: "))
  f_max = float(input("(Recommended: 5) Maximum frequency: "))

  # Generate the times
  times = np.linspace(0, 1, 1000)

  # Generate the sinusoidal signals
  signals = []
  frequencies = []
  for i in range(n):
    amplitude = np.random.uniform(low=a_min, high=a_max)
    frequency = np.random.uniform(low=f_min, high=f_max)
    signals.append(generate_sinusoidal_signal(amplitude, frequency, times))
    frequencies.append(frequency)

  # Sum the signals
  composite_signal = np.sum(signals, axis=0)

  # Find the maximum frequency
  freq_max = max(frequencies)

  # Plot the individual signals
  fig, axs = plt.subplots(n // 3 + 1, 3, figsize=(19, 13))
  axs = np.array(axs) # Make sure axs is always an array
  for i in range(n):
    ax = axs.flatten()[i] # Use flatten() to convert axs into a one-dimensional array
    ax.plot(times, signals[i], label="Signal %d" % (i + 1), color=plt.cm.Spectral(np.random.rand()))
    ax.set_title("Signal %d" % (i + 1))
    ax.set_xlabel("Time (s)")
    ax.set_ylabel("Amplitude")
    ax.legend()

  # Plot the composite signal
  fig, ax = plt.subplots(1, 1, figsize=(9,9))
  ax.plot(times, composite_signal)
  ax.set_title("Composite signal")
  ax.set_xlabel("Time (s)")
  ax.set_ylabel("Amplitude")

  # Generate the carrier signal
  carrier_amplitude = a_max
  carrier_frequency = f_max * n * n # Hz
  carrier = carrier_amplitude * np.sin(2 * np.pi * carrier_frequency * times)

  # Generate the modulating signal
  modulating_signal = generate_sinusoidal_signal(a_min, f_max, times)

  # Modulate the signal AM, with a value k that can go from 0 to 1
  k = float(input("Enter the AM Modulation index between 0 and 1: ")) # A value close to zero indicates low depth AM modulation and one high depth.
  am = carrier * (1 + k * modulating_signal)

  # Calculate the envelope using the Hilbert transform
  envelope = np.abs(hilbert(am))

  # Plot the signals in a subplot for AM
  fig, axs = plt.subplots(4, figsize=(19,13))

  # Adjust the space between the graphs
  plt.subplots_adjust(hspace = 0.5)

  # Plot the carrier signal
  axs[0].plot(times, carrier)
  axs[0].set_title('Carrier Signal')
  axs[0].set_xlabel("Time (s)")
  axs[0].set_ylabel("Amplitude")

  # Plot the modulating signal
  axs[1].plot(times, modulating_signal)
  axs[1].set_title('Modulating Signal')
  axs[1].set_xlabel("Time (s)")
  axs[1].set_ylabel("Amplitude")

  # Plot the composite signal and the modulating signal on the same graph
  axs[2].plot(times, composite_signal, label="Composite Signal", color="red")
  axs[2].plot(times, modulating_signal, label="Modulating Signal", color="blue")
  axs[2].plot(times, am, label='AM Modulated Signal', color="green")

  axs[2].set_title('Modulating and Composite Signals')
  axs[2].set_xlabel("Time (s)")
  axs[2].set_ylabel("Amplitude")
  axs[2].legend()

  # Plot the AM modulated signal with its envelope
  axs[3].plot(times, am, label='AM Modulated Signal')
  axs[3].plot(times, envelope, label='Envelope', color='red')
  axs[3].set_title('AM Modulated Signal with Envelope')
  axs[3].set_xlabel("Time (s)")
  axs[3].set_ylabel("Amplitude")
  axs[3].legend()

  # Generate the FM signal
  k_fm = float(input("Enter the FM Modulation index: ")) # A value close to 0 indicates low depth FM modulation and 1 high depth.
  fm = carrier_amplitude * np.sin(2 * np.pi * carrier_frequency * times + k_fm * np.sin(2 * np.pi * f_max * times)) # Unlike AM, FM can use values < 1 (wideband FM modulation)

  # Plot the signals in a subplot for FM
  fig, axs = plt.subplots(3, figsize=(19,13))

  # Adjust the space between the graphs
  plt.subplots_adjust(hspace = 0.5)

  # Plot the carrier signal
  axs[0].plot(times, carrier)
  axs[0].set_title('Carrier Signal')
  axs[0].set_xlabel("Time (s)")
  axs[0].set_ylabel("Amplitude")

  # Plot the modulating signal
  axs[1].plot(times, modulating_signal)
  axs[1].set_title('Modulating Signal')
  axs[1].set_xlabel("Time (s)")
  axs[1].set_ylabel("Amplitude")

  # Plot the FM modulated signal
  axs[2].plot(times, fm)
  axs[2].set_title('FM Modulated Signal')
  axs[2].set_xlabel("Time (s)")
  axs[2].set_ylabel("Amplitude")

  # Generate the PM signal
  pm = carrier_amplitude * np.sin(2 * np.pi * carrier_frequency * times + k * composite_signal)

  # Plot the signals in a subplot for PM
  fig, axs = plt.subplots(3, figsize=(19,13))

  # Adjust the space between the graphs
  plt.subplots_adjust(hspace = 0.5)

  # Plot the carrier signal
  axs[0].plot(times, carrier)
  axs[0].set_title('Carrier Signal')
  axs[0].set_xlabel("Time (s)")
  axs[0].set_ylabel("Amplitude")

  # Plot the modulating signal
  axs[1].plot(times, modulating_signal)
  axs[1].set_title('Modulating Signal')
  axs[1].set_xlabel("Time (s)")
  axs[1].set_ylabel("Amplitude")

  # Plot the PM modulated signal
  axs[2].plot(times, pm)
  axs[2].set_title('PM Modulated Signal')
  axs[2].set_xlabel("Time (s)")
  axs[2].set_ylabel("Amplitud")

  plt.show()

if __name__ == "__main__":
    main()
"""
To notice the difference between FM and PM
(Recommended: 3-5) How many signals do you want to generate? 1
(Recommended: 1) Minimum amplitude: 1
(Recommended: 5) Maximum amplitude: 1
(Recommended: 1) Minimum frequency: 5
(Recommended: 5) Maximum frequency: 5
Enter the AM Modulation index between 0 and 1: 0.5
Enter the FM Modulation index: 0.1
"""
