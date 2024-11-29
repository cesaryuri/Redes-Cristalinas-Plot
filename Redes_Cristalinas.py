import numpy as np
import matplotlib.pyplot as plt

# Função para gerar os vetores da rede
def gerar_vetores(a, b, c, alpha, beta, gamma):
    alpha, beta, gamma = np.radians([alpha, beta, gamma])  
    v1 = np.array([a, 0, 0])
    v2 = np.array([b * np.cos(gamma), b * np.sin(gamma), 0])
    v3 = np.array([
        c * np.cos(beta),
        c * (np.cos(alpha) - np.cos(beta) * np.cos(gamma)) / np.sin(gamma),
        np.sqrt(c**2 - (c * np.cos(beta))**2 - (c * (np.cos(alpha) - np.cos(beta) * np.cos(gamma)) / np.sin(gamma))**2),
    ])
    return v1, v2, v3

# Função para gerar os pontos da rede, gera N células na direção v1 v2 e v3
def gerar_rede(v1, v2, v3, N):
    pontos = []
    for i in range(N):  
        for j in range(N):  
            for k in range(N):  
                # Adiciona os vértices de uma célula unitária
                pontos.append(i * v1 + j * v2 + k * v3)
    return np.unique(np.array(pontos), axis=0)  

# Função para ajustar a escala do gráfico
def ajustar_escala(ax, pontos):
    
    x_min, x_max = np.min(pontos[:, 0]), np.max(pontos[:, 0])
    y_min, y_max = np.min(pontos[:, 1]), np.max(pontos[:, 1])
    z_min, z_max = np.min(pontos[:, 2]), np.max(pontos[:, 2])
    
    # Determinar o intervalo máximo
    max_range = max(x_max - x_min, y_max - y_min, z_max - z_min)

    # Centralizar os limites em cada eixo
    ax.set_xlim((x_min, x_min + max_range))
    ax.set_ylim((y_min, y_min + max_range))
    ax.set_zlim((z_min, z_min + max_range))

# Parâmetros da célula unitária 
a, b, c = 1, 1, 1  # Comprimentos das arestas 
alpha, beta, gamma = 80, 80, 80  # Ângulos em graus
N = 2  # Número de células em cada direção


# Gerar vetores e pontos
v1, v2, v3 = gerar_vetores(a, b, c, alpha, beta, gamma)
pontos = gerar_rede(v1, v2, v3, N)

# Plotar os pontos e as arestas
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

# Adicionar pontos
for ponto in pontos:
    ax.scatter(ponto[0], ponto[1], ponto[2], color='blue')

# Conectar os pontos com as arestas
for ponto in pontos:
    for vizinho in [ponto + v1, ponto + v2, ponto + v3]:  
        if any(np.allclose(vizinho, p) for p in pontos): 
            ax.plot([ponto[0], vizinho[0]], [ponto[1], vizinho[1]], [ponto[2], vizinho[2]], color='black')

# Ajustar escala do gráfico
ajustar_escala(ax, pontos)

# Configuração do gráfico
ax.set_xlabel('X')
ax.set_ylabel('Y')
ax.set_zlabel('Z')
plt.title(f"Trigonal R")
plt.show()