# this opens a new img each time for each iteration

import numpy as np
from matplotlib import pyplot as plt
from PIL import Image

env_img = Image.open("rock.jpg").convert("RGB")
env = np.array(env_img) / 255.0  # normalize 0-1

N, M, _ = env.shape

# Chromatophores have various pigments in their skin.
# this is mimicked using RGB 'layers,' 3 chromatophore types (R, G, B)
skin = np.zeros((N, M, 3))

# Parameters
Env_sensitivity = 0.2
smoothing = 0.1   # neighbor smoothing
pulsing = 0.02 # random pulsing

def update_cell(i, j, c):
    local_env = env[i, j, c]
    neighbors = skin[max(i-1,0):i+2, max(j-1,0):j+2, c]
    neighbor_avg = (np.sum(neighbors) - skin[i,j,c]) / (neighbors.size - 1)
    delta = Env_sensitivity * (local_env - skin[i,j,c]) + smoothing * (neighbor_avg - skin[i,j,c])
    return skin[i,j,c] + np.tanh(delta) * 0.5

# Main simulation loop
plt.figure(figsize=(8,8))
for t in range(200):
    skin_new = np.copy(skin)
    for i in range(N):
        for j in range(M):
            for c in range(3):
                skin_new[i,j,c] = update_cell(i,j,c)
                # Add pulsing/noise
                skin_new[i,j,c] += pulsing * (np.random.rand() - 0.5)
    # Keep values in [0,1]
    skin = np.clip(skin_new, 0, 1)

    plt.imshow(skin)
    plt.axis('off')
    plt.title("Chromatophore Camouflage Simulation")
    plt.pause(0.01)
