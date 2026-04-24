import numpy as np

class GridWorldMDP:
    def __init__(self, size, goal, trap):
        self.size = size
        self.goal = goal
        self.trap = trap
        self.state_space = [(i, j) for i in range(size) for j in range(size)]
        self.action_space = ['UP', 'DOWN', 'LEFT', 'RIGHT']
        self.transitions = self.build_transitions()
        self.rewards = self.build_rewards()

    def build_transitions(self):
        transitions = {}
        for state in self.state_space:
            transitions[state] = {}
            for action in self.action_space:
                transitions[state][action] = self.calculate_transitions(state, action)
        return transitions

    def calculate_transitions(self, state, action):
        i, j = state
        if action == 'UP':
            return self.validate_state(i - 1, j)
        elif action == 'DOWN':
            return self.validate_state(i + 1, j)
        elif action == 'LEFT':
            return self.validate_state(i, j - 1)
        elif action == 'RIGHT':
            return self.validate_state(i, j + 1)

    def validate_state(self, i, j):
        i = max(0, min(i, self.size - 1))
        j = max(0, min(j, self.size - 1))
        return [(1.0, (i, j))]

    def build_rewards(self):
        rewards = {}
        for state in self.state_space:
            rewards[state] = -1.0
        rewards[self.goal] = 0.0
        rewards[self.trap] = -10.0
        return rewards


# VALUE ITERATION WITH STEP PRINTING
def value_iteration(mdp, gamma=0.9, epsilon=0.01):
    state_values = {state: 0.0 for state in mdp.state_space}
    iteration = 0

    while True:
        iteration += 1
        delta = 0

        print(f"\n--- Value Iteration Step {iteration} ---")

        for state in mdp.state_space:
            if state == mdp.goal or state == mdp.trap:
                continue

            v = state_values[state]

            new_value = max(
                sum(p * (mdp.rewards[next_state] + gamma * state_values[next_state])
                    for p, next_state in mdp.transitions[state][action])
                for action in mdp.action_space
            )

            state_values[state] = new_value
            delta = max(delta, abs(v - new_value))

            print(f"State: {state}, Value: {new_value:.4f}")

        if delta < epsilon:
            print("\nConverged!")
            break

    return state_values


# 🔹 POLICY ITERATION WITH STEP PRINTING
def policy_iteration(mdp, gamma=0.9):
    policy = {state: np.random.choice(mdp.action_space)
              for state in mdp.state_space
              if state != mdp.goal and state != mdp.trap}

    state_values = {state: 0.0 for state in mdp.state_space}
    iteration = 0

    while True:
        iteration += 1
        print(f"\n=== Policy Iteration Step {iteration} ===")

        # Policy Evaluation
        eval_step = 0
        while True:
            eval_step += 1
            delta = 0

            print(f"\nPolicy Evaluation Step {eval_step}")

            for state in mdp.state_space:
                if state == mdp.goal or state == mdp.trap:
                    continue

                v = state_values[state]
                action = policy[state]

                new_value = sum(
                    p * (mdp.rewards[next_state] + gamma * state_values[next_state])
                    for p, next_state in mdp.transitions[state][action]
                )

                state_values[state] = new_value
                delta = max(delta, abs(v - new_value))

                print(f"State: {state}, Value: {new_value:.4f}")

            if delta < 0.01:
                break

        # Policy Improvement
        policy_stable = True
        print("\nPolicy Improvement:")

        for state in mdp.state_space:
            if state == mdp.goal or state == mdp.trap:
                continue

            old_action = policy[state]

            best_action = max(
                mdp.action_space,
                key=lambda a: sum(
                    p * (mdp.rewards[next_state] + gamma * state_values[next_state])
                    for p, next_state in mdp.transitions[state][a]
                )
            )

            policy[state] = best_action

            print(f"State: {state}, Old: {old_action}, New: {best_action}")

            if old_action != best_action:
                policy_stable = False

        if policy_stable:
            print("\nPolicy Converged!")
            break

    return policy, state_values


# Example Usage
size = 3
goal = (2, 2)
trap = (1, 1)

mdp = GridWorldMDP(size, goal, trap)

# Run Value Iteration
value_iteration(mdp)

# Run Policy Iteration
policy_iteration(mdp)
