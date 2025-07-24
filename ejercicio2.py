
import numpy as np
import matplotlib.pyplot as plt

beta = 0.3     
gamma = 0.1    
dt = 0.5       
dias = 180
N = int(dias / dt)

def simular_SIR_vacunacion(v, S0=0.99, I0=0.01, R0=0.0):
    S = np.zeros(N)
    I = np.zeros(N)
    R = np.zeros(N)
    tiempo = np.linspace(0, dias, N)

    S[0] = S0
    I[0] = I0
    R[0] = R0

    for t in range(N - 1):
        dS = -beta * S[t] * I[t] - v * S[t]
        dI = beta * S[t] * I[t] - gamma * I[t]
        dR = gamma * I[t] + v * S[t]

        S[t+1] = S[t] + dS * dt
        I[t+1] = I[t] + dI * dt
        R[t+1] = R[t] + dR * dt

    return tiempo, S, I, R

# Gráfica con v = 0.05
tiempo, S, I, R = simular_SIR_vacunacion(v=0.05)

plt.figure(figsize=(10, 6))
plt.plot(tiempo, S, label='Susceptibles')
plt.plot(tiempo, I, label='Infectados')
plt.plot(tiempo, R, label='Recuperados')
plt.title("Modelo SIR con vacunación (v = 0.05)")
plt.xlabel("Días")
plt.ylabel("Proporción de la población")
plt.legend()
plt.grid(True)
plt.show()
