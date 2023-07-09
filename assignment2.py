import numpy as np

class StateSimulator:
    def __init__(self, states, transition_probabilities, holding_times):
        self.states = states
        self.transition_probabilities = transition_probabilities
        self.holding_times = holding_times
        self.current_state = np.random.choice(list(states))  # Initialize current state
        self.remaining_hours = holding_times[self.current_state]

    def get_states(self):
        return self.states

    def get_current_state(self):
        return self.current_state

    def next_state(self):
        probabilities = list(self.transition_probabilities[self.current_state].values())
        next_state = np.random.choice(self.states, p=probabilities)
        self.current_state = next_state
        self.remaining_hours = self.holding_times[next_state]

    def set_state(self, new_state):
        if new_state not in self.states:
            raise ValueError("Invalid state '{}'.".format(new_state))
        self.current_state = new_state
        self.remaining_hours = self.holding_times[new_state]

    def current_state_remaining_hours(self):
        return self.remaining_hours

    def iterable(self):
        while True:
            yield self.current_state
            self.next_state()

    def simulate(self, hours):
        state_counts = {state: 0 for state in self.states}
        for _ in range(hours):
            self.next_state()
            state_counts[self.current_state] += 1
        state_percentages = [state_counts[state] / hours for state in self.states]
        return state_percentages
