import numpy as np
import matplotlib.pyplot as plt

# Função para calcular a expressão
def expression(x):
    return 3**x + 3**(x+1) - 2 * 3**(x+2) + 3**(x+3)

# Gerando valores de x
x_values = np.linspace(-2, 2, 400)

# Calculando os valores da expressão para cada x
y_values = expression(x_values)

# Linha de referência y = 13
y_ref = np.full_like(x_values, 13)

# Criando o gráfico
plt.figure(figsize=(10, 6))
plt.plot(x_values, y_values, label=r'$3^x + 3^{x+1} - 2\cdot3^{x+2} + 3^{x+3}$', color='blue')
plt.plot(x_values, y_ref, label=r'$y = 13$', color='red', linestyle='--')

# Adicionando linha horizontal em y=0 para referência
plt.axhline(0, color='black',linewidth=0.5)

# Configurações do gráfico
plt.title(r'Gráfico da Equação $3^x + 3^{x+1} - 2\cdot3^{x+2} + 3^{x+3} < 13$')
plt.xlabel(r'$x$')
plt.ylabel(r'$y$')
plt.legend()
plt.grid(True)
plt.show()
