import numpy as np

states = ["Low", "Medium", "High"]
actions = ["Increase", "Decrease", "Same"]

# Rewards
rewards = {
    "Low": 10,
    "Medium": 5,
    "High": -10
}

# Transition probabilities
transitions = {
    "Low": {
        "Increase": [("Low", 0.8), ("Medium", 0.2)],
        "Decrease": [("Medium", 0.6), ("High", 0.4)],
        "Same": [("Low", 0.7), ("Medium", 0.3)]
    },
    "Medium": {
        "Increase": [("Low", 0.6), ("Medium", 0.4)],
        "Decrease": [("Medium", 0.5), ("High", 0.5)],
        "Same": [("Medium", 0.6), ("High", 0.4)]
    },
    "High": {
        "Increase": [("Medium", 0.7), ("High", 0.3)],
        "Decrease": [("High", 0.8), ("Medium", 0.2)],
        "Same": [("High", 0.9), ("Medium", 0.1)]
    }
}

gamma = 0.9
epsilon = 0.01

# Initialize values
V = {s: 0 for s in states}

while True:
    delta = 0
    new_V = V.copy()

    for s in states:
        action_values = []

        for a in actions:
            value = sum(p * (rewards[s_next] + gamma * V[s_next])
                        for s_next, p in transitions[s][a])
            action_values.append(value)

        new_V[s] = max(action_values)
        delta = max(delta, abs(new_V[s] - V[s]))

    V = new_V

    if delta < epsilon:
        break

print("Optimal State Values:")
for s in V:
    print(s, ":", V[s])
