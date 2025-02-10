import numpy as np
import matplotlib.pyplot as plt

def fermi_dirac(E, E_F, T):
    k_B = 8.617e-5
    return 1 / (np.exp((E - E_F) / (k_B * T)) + 1)

# Parâmetros
E_F = 1.0  # Nível de Fermi em eV
T_values = [5.5, 300]  # Temperaturas em Kelvin
E = np.linspace(0, 2, 1000)  # Intervalo de energia de 0 a 2 eV

# Plotando para diferentes temperaturas
plt.figure(figsize=(8, 5))
for T in T_values:
    plt.plot(E, fermi_dirac(E, E_F, T), label=f"T = {T} K")

plt.xlabel("Energia (eV)")
plt.ylabel("f(E)")
plt.title("Distribuição de Fermi-Dirac")
plt.legend()
plt.grid()
plt.show()
