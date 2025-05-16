# Container-basierte Schiffsnavigation mit Q-Learning

Dieses Projekt demonstriert die Entwicklung eines Q-Learning-Agenten, der in einer 5×5-Gitterwelt Container von variablen Pick-Up- zu Drop-Off-Punkten transportiert.  
Feste Hindernisse erschweren die Navigation und erhöhen die Realitätsnähe der Simulation.

## Inhalt

- **Umgebung:** Definition der Grid-World mit variablen Container-Positionen und fixen Hindernissen  
- **Training:** Q-Learning mit adaptivem Epsilon-Decay zur effizienten Exploration  
- **Evaluation:** Visualisierung und Analyse der gelernten Policy  
- **Ergebnisse:** Darstellung von Lernkurven und Erfolgsraten in variablen Szenarien  

## Ziel

Das Modell soll die Generalisierungsfähigkeit eines RL-Agenten unter dynamischen Umweltbedingungen untersuchen und eine Grundlage für komplexere maritime Logistik-Szenarien bieten.

## Projektstruktur

docs/
├── index.md

src/
├── navigation/
│ ├── environment/
│ │ ├── init.py
│ │ └── container_environment.py
│ ├── evaluate_policy.py
│ ├── q_table.npy
│ ├── run_policy.py
│ ├── train.py
│ └── visualize_policy.py

.gitignore
README.md
requirements.txt