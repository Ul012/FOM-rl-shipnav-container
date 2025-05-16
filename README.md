# Container-basierte Schiffsnavigation mit Q-Learning

Dieses Projekt erweitert eine klassische Q-Learning-Umgebung um ein logistikähnliches Szenario: Ein Schiff muss Container an einem bestimmten Ort abholen und an einem anderen Ort abliefern. Die Umgebung enthält zudem Hindernisse, denen ausgewichen werden muss.

---

## Ziel
Entwicklung eines Q-Learning-Agenten, der lernt:
- effizient Container zu Pick-Up- und Drop-Off-Punkten zu transportieren,
- dabei Hindernisse zu vermeiden,
- und eine optimale Strategie durch Exploration und Belohnung zu entwickeln.

---

## Q-Learning Setup
- **State-Space:** Position (x, y) + Containerstatus (geladen / nicht geladen)
- **Action-Space:** 4 Richtungen (N, E, S, W)
- **Reward-Strategie:**
  - `+5` für erfolgreiches Aufnehmen eines Containers
  - `+10` für korrektes Abliefern
  - `-1` pro Schritt (Zeitstrafe)
  - `-10` bei Kollision mit Hindernis

---

## Projektstruktur
```
FOM-rl-container-shipnav/
├── src/
│   ├── environment/
│   │   └── container_environment.py  ← Umgebungsklasse mit Pick-Up & Drop-Off
│   ├── train.py                     ← Trainingslogik für den Agenten
│   └── run_policy.py                ← Optional: Nachspielen der Policy
├── requirements.txt                ← Abhängigkeiten
├── README.md                       ← Dieses Dokument
└── venv/                           ← (existierende virtuelle Umgebung)
```

---

## Ausführen
### Training starten
```bash
python src/train.py
```

### Lernverlauf visualisieren
Der Trainingsprozess erzeugt eine Lernkurve mit dem Gesamtreward pro Episode.

---

## Abhängigkeiten
Installierbar per `pip install -r requirements.txt`:
```txt
numpy
matplotlib
gymnasium
```

---

## Hinweise
- Die Positionen von Pick-Up und Drop-Off sind im Code derzeit fix, können aber leicht randomisiert werden.
- Die Umgebung basiert auf `gymnasium` und ist kompatibel mit gängigen RL-Algorithmen.

---

## Weiterentwicklungsideen
- Mehrere Container und Ziele gleichzeitig verwalten
- Dynamische Hindernisse oder Wetterzonen
- Vergleich mit Policy Gradient Methoden oder Deep Q-Networks (DQN)
