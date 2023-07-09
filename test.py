from assignment2 import StateSimulator

my_transitions = {
    'sunny': {'sunny': 0.7, 'cloudy': 0.3, 'rainy': 0, 'snowy': 0},
    'cloudy': {'sunny': 0.5, 'cloudy': 0.3, 'rainy': 0.15, 'snowy': 0.05},
    'rainy': {'sunny': 0.7, 'cloudy': 0.2, 'rainy': 0.05, 'snowy': 0.05},
    'snowy': {'sunny': 0.7, 'cloudy': 0.1, 'rainy': 0.05, 'snowy': 0.15}
}

my_holding_times = {'sunny': 1, 'cloudy': 2, 'rainy': 2, 'snowy': 1}

# Create an instance of StateSimulator
state_sim = StateSimulator(list(my_transitions.keys()), my_transitions, my_holding_times)

hours = 10000
state_percentages = state_sim.simulate(hours)
print("State percentages after simulating {} hours:".format(hours))
print(state_percentages)
