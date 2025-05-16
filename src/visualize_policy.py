import pygame
import numpy as np
import sys
import os
import time

# Pfad setzen, damit Import aus environment funktioniert
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '.')))
from navigation.environment.container_environment import ContainerShipEnv

# Q-Tabelle laden
Q = np.load("q_table.npy")

# Umgebung initialisieren
env = ContainerShipEnv()
CELL_SIZE = 80
GRID_SIZE = env.grid_size
WIDTH = HEIGHT = CELL_SIZE * GRID_SIZE

pygame.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Agentenpfad – Container Navigation")
font = pygame.font.SysFont("Segoe UI Emoji", 40)

actions_map = {0: '↑', 1: '→', 2: '↓', 3: '←'}
color_map = {
    'pickup': (255, 215, 0),
    'dropoff': (0, 200, 0),
    'hazard': (200, 0, 0),
    'agent': (30, 144, 255),
    'start': (255, 140, 0)
}

def encode_state(x, y, has_container):
    return (x * GRID_SIZE + y) + (GRID_SIZE * GRID_SIZE) * has_container

def draw_grid(agent_pos, has_container):
    screen.fill((224, 247, 255))  # maritimer Hintergrund
    for i in range(GRID_SIZE):
        for j in range(GRID_SIZE):
            rect = pygame.Rect(j * CELL_SIZE, i * CELL_SIZE, CELL_SIZE, CELL_SIZE)
            pygame.draw.rect(screen, (200, 200, 200), rect, 1)

            pos = (i, j)
            if pos == agent_pos:
                txt = font.render("🚢", True, color_map['agent'])
                screen.blit(txt, (j * CELL_SIZE + 25, i * CELL_SIZE + 20))
            elif pos == env.start_pos:
                txt = font.render("🧭", True, color_map['start'])
                screen.blit(txt, (j * CELL_SIZE + 25, i * CELL_SIZE + 20))
            elif pos == env.pickup_pos:
                txt = font.render("📦", True, color_map['pickup'])
                screen.blit(txt, (j * CELL_SIZE + 25, i * CELL_SIZE + 20))
            elif pos == env.dropoff_pos:
                txt = font.render("🏁", True, color_map['dropoff'])
                screen.blit(txt, (j * CELL_SIZE + 25, i * CELL_SIZE + 20))
            elif pos in env.hazards:
                txt = font.render("🪨", True, color_map['hazard'])
                screen.blit(txt, (j * CELL_SIZE + 25, i * CELL_SIZE + 20))
            else:
                c = 1 if has_container else 0
                s = encode_state(i, j, c)
                best_action = np.argmax(Q[s])
                txt = font.render(actions_map[best_action], True, (0, 0, 0))
                screen.blit(txt, (j * CELL_SIZE + 25, i * CELL_SIZE + 20))

    pygame.display.flip()

def run_agent():
    state, _ = env.reset()
    draw_grid((state[0], state[1]), state[2])
    time.sleep(0.5)

    done = False
    while not done:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                return

        x, y, c = state
        s = encode_state(x, y, c)
        action = np.argmax(Q[s])

        state, _, done, _, _ = env.step(action)
        draw_grid((state[0], state[1]), state[2])
        time.sleep(0.4)

    time.sleep(2)
    pygame.quit()

run_agent()
