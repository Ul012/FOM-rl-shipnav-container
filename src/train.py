import sys
import os
import numpy as np
import matplotlib.pyplot as plt

# Pfad zum Environment-Modul
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '.')))
from navigation.environment.container_environment import ContainerShipEnv

# Q-Learning Parameter
alpha = 0.1
gamma = 0.9
episodes = 2000

grid_size = 5
n_states = grid_size * grid_size * 2  # Position + Containerstatus
n_actions = 4

# Steuerung: mit oder ohne epsilon decay?
use_decay = True  # << auf False setzen, um decay zu deaktivieren

if use_decay:
    epsilon = 1.0
    epsilon_min = 0.05
    epsilon_decay = 0.995
else:
    epsilon = 0.1  # fixer Wert ohne Decay

# Initialisierung
Q = np.zeros((n_states, n_actions))
rewards_per_episode = []
success_per_episode = []

def encode_state(x, y, has_container):
    return (x * grid_size + y) + (grid_size * grid_size) * has_container

# Umgebung einmal erzeugen
env = ContainerShipEnv()

for ep in range(episodes):
    (x, y, has_container), _ = env.reset()
    state = encode_state(x, y, has_container)
    total_reward = 0
    done = False
    success = 0

    while not done:
        # Aktion wählen (epsilon-greedy)
        if np.random.rand() < epsilon:
            action = np.random.choice(n_actions)
        else:
            action = np.argmax(Q[state])

        (x_next, y_next, has_container_next), reward, terminated, truncated, _ = env.step(action)
        next_state = encode_state(x_next, y_next, has_container_next)
        done = terminated or truncated

        # Q-Wert aktualisieren
        Q[state, action] += alpha * (reward + gamma * np.max(Q[next_state]) - Q[state, action])
        state = next_state
        total_reward += reward

        if terminated and reward == 20:  # Drop-Off erfolgreich
            success = 1
        else:
            success = 0

    rewards_per_episode.append(total_reward)
    success_per_episode.append(success)

    # Epsilon anpassen, falls decay aktiv
    if use_decay and epsilon > epsilon_min:
        epsilon *= epsilon_decay

# Q-Tabelle speichern
np.save("q_table.npy", Q)
print("Q-Tabelle gespeichert als q_table.npy")

# Lernkurve
window_size = 20
plt.figure(figsize=(10, 5))
plt.plot(rewards_per_episode, alpha=0.3, label="Raw Reward", color='blue')
if len(rewards_per_episode) >= window_size:
    moving_avg = np.convolve(rewards_per_episode, np.ones(window_size)/window_size, mode='valid')
    plt.plot(range(window_size - 1, episodes), moving_avg, label=f"Moving Average ({window_size})", color='red')
plt.xlabel("Episode")
plt.ylabel("Gesamtreward")
plt.title("Lernkurve (mit oder ohne Epsilon Decay)")
plt.legend()
plt.grid(True)
plt.tight_layout()
plt.show()

# Erfolgskurve
plt.figure(figsize=(10, 3))
plt.plot(success_per_episode, label="Ziel erreicht", color='green', alpha=0.5)
plt.xlabel("Episode")
plt.ylabel("Erfolg (0/1)")
plt.title("Zielerreichung pro Episode")
plt.grid(True)
plt.tight_layout()
plt.show()

# Erfolgsstatistik
total_successes = sum(success_per_episode)
print(f"Erfolgreiche Zielerreichung in {total_successes}/{episodes} Episoden ({(total_successes / episodes) * 100:.1f}%)")
