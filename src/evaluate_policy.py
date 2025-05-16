import numpy as np
import matplotlib.pyplot as plt
from navigation.environment.container_environment import ContainerShipEnv

# Q-Tabelle laden
Q = np.load("q_table.npy")
env = ContainerShipEnv()

episodes = 100
success_count = 0
total_reward = 0
total_steps = 0
success_per_episode = []

def encode_state(x, y, has_container):
    return (x * env.grid_size + y) + (env.grid_size * env.grid_size) * has_container

for ep in range(episodes):
    obs, _ = env.reset()
    done = False
    episode_reward = 0
    steps = 0
    success = 0

    while not done:
        x, y, has_container = obs
        state = encode_state(x, y, has_container)
        action = np.argmax(Q[state])

        obs, reward, done, _, _ = env.step(action)
        episode_reward += reward
        steps += 1

        if done and reward == 20:
            success = 1
            success_count += 1

    total_reward += episode_reward
    total_steps += steps
    success_per_episode.append(success)

# Ergebnisse ausgeben
print(f"\n📊 Auswertung über {episodes} Policy-Durchläufe:")
print(f"✅ Erfolgreiche Drop-Offs: {success_count}/{episodes} "
      f"({(success_count / episodes) * 100:.1f}%)")
print(f"🏁 Durchschnittlicher Reward pro Episode: {total_reward / episodes:.2f}")
print(f"🕒 Durchschnittliche Schrittanzahl pro Episode: {total_steps / episodes:.1f}")

# Visualisierung der Zielerreichung
plt.figure(figsize=(10, 3))
plt.plot(success_per_episode, label="Ziel erreicht (0/1)", color='green', alpha=0.6)
plt.xlabel("Episode")
plt.ylabel("Erfolg")
plt.title("Zielerreichung pro Episode (Evaluation)")
plt.grid(True)
plt.tight_layout()
plt.show()
