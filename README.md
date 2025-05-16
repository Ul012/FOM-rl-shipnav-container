# Container-basierte Schiffsnavigation mit Q-Learning

Dieses Projekt erweitert eine klassische Q-Learning-Umgebung um ein logistikähnliches Szenario:  
Ein Schiff muss Container an variablen Pick-Up-Punkten aufnehmen und an unterschiedlichen Drop-Off-Punkten abliefern.  
Feste Hindernisse erschweren die Navigation.

---

## Ziel  
Entwicklung eines Q-Learning-Agenten, der lernt:  
- effiziente Routen zu variablen Pick-Up- und Drop-Off-Punkten  
- sichere Umfahrung von festen Hindernissen  
- optimale Strategie durch Exploration und Belohnung  

---

## Q-Learning Setup  
- **State-Space:** Position (x, y) + Containerstatus (geladen / nicht geladen)  
- **Action-Space:** 4 Richtungen (N, E, S, W)  
- **Reward-Strategie:**  
  - +8 für erfolgreiches Aufnehmen eines Containers  
  - +20 für korrektes Abliefern  
  - -2 pro Schritt (Zeitstrafe)  
  - -10 bei Kollision mit Hindernis  
  - Schleifen- und Timeout-Strafen zur Vermeidung ineffizienter Pfade  

---

## Projektstruktur

ship-navigation-container-rl/
├── src/
│ ├── navigation/
│ │ ├── environment/
│ │ │ └── container_environment.py ← Umgebung mit variablen Pick-Up/Drop-Off und festen Hindernissen
│ │ ├── train.py ← Trainingsskript mit Q-Learning und Epsilon-Decay
│ │ ├── run_policy.py ← Policy-Ausführung mit Visualisierung
│ │ └── visualize_policy.py ← Policy-Visualisierung über ganze Karten
├── docs/
│ └── index.md ← Projektdokumentation (MkDocs)
├── requirements.txt ← Python-Abhängigkeiten
├── README.md ← Dieses Dokument
└── .gitignore