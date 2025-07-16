import numpy as np
import matplotlib.pyplot as plt

class PoblacionModel:
    def __init__(self, S0, alpha, dt, t_end):
        self.S0 = S0
        self.alpha = alpha
        self.dt = dt
        self.t_end = t_end
        self.time = np.arange(0, t_end + dt, dt)
        self.stock_euler = np.zeros(len(self.time))
        self.stock_analitica = np.zeros(len(self.time))

    def simular_euler(self):
        self.stock_euler[0] = self.S0
        for i in range(1, len(self.time)):
            dS = -self.alpha * self.stock_euler[i - 1]
            self.stock_euler[i] = self.stock_euler[i - 1] + dS * self.dt

    def calcular_analitica(self):
        self.stock_analitica = self.S0 * np.exp(-self.alpha * self.time)

    def graficar(self):
        plt.figure(figsize=(10, 6))
        plt.plot(self.time, self.stock_euler, '--', label=f'Método de Euler (Δt = {self.dt})')
        plt.plot(self.time, self.stock_analitica, label='Solución Analítica')
        plt.title('Disminución de población con tasa de mortalidad constante')
        plt.xlabel('Tiempo (meses)')
        plt.ylabel('Población')
        plt.grid(True)
        plt.legend()
        plt.tight_layout()
        plt.show()


modelo = PoblacionModel(S0=1000, alpha=0.1, dt=0.1, t_end=24)

modelo.simular_euler()
modelo.calcular_analitica()
modelo.graficar()
