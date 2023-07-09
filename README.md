## Assignment2.py

### Description
The `StateSimulator` class simulates state transitions and holding times of a system. It allows you to initialize the simulator with a set of states, transition probabilities, and holding times. You can then perform various operations such as getting the current state, transitioning to the next state, setting a new state, and simulating state percentages over a given number of hours.

### Class: StateSimulator

#### Methods:

1. `__init__(self, states, transition_probabilities, holding_times)`
   - Initializes the StateSimulator object with the provided states, transition probabilities, and holding times.
   - Parameters:
     - `states` (list): A list of all the possible states in the system.
     - `transition_probabilities` (dict): A dictionary representing the transition probabilities between states. The keys are the current states, and the values are dictionaries where the keys are the next states and the values are the probabilities of transitioning to those states.
     - `holding_times` (dict): A dictionary mapping each state to its holding time (number of hours to stay in that state).

2. `get_states(self) -> list`
   - Returns the list of states in the system.
   - Returns:
     - `list`: A list of all the possible states in the system.

3. `get_current_state(self) -> str`
   - Returns the current state of the simulator.
   - Returns:
     - `str`: The current state of the simulator.

4. `next_state(self) -> None`
   - Transitions to the next state based on the transition probabilities.
   - Does not return any value.

5. `set_state(self, new_state) -> None`
   - Sets the current state of the simulator to the specified new state.
   - Parameters:
     - `new_state` (str): The new state to set.
   - Raises:
     - `ValueError`: If the new state is not a valid state in the system.

6. `current_state_remaining_hours(self) -> int`
   - Returns the remaining hours in the current state.
   - Returns:
     - `int`: The remaining hours in the current state.

7. `iterable(self) -> iterator`
   - Returns an iterator that yields the current state at each iteration and transitions to the next state.
   - Yields:
     - `str`: The current state at each iteration.

8. `simulate(self, hours) -> list`
   - Simulates the state transitions for the specified number of hours and returns the state percentages.
   - Parameters:
     - `hours` (int): The number of hours to simulate.
   - Returns:
     - `list`: A list of state percentages representing the proportion of time spent in each state during the simulation.

## Test.py

### Description:
This code file demonstrates the usage of the `StateSimulator` class from `Assignment2.py` and sets up transition probabilities and holding times for different states, simulates state percentages over a specified number of hours, and prints out the results.

### Code:

```python
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
```

## Outcome
```
State percentages after simulating 10000 hours:
[0.4309, 0.2947, 0.1784, 0.096]
```

The code sets up a `StateSimulator` with transition probabilities and holding times for different weather states: sunny, cloudy, rainy, and snowy. It then simulates the state transitions for 10000 hours and calculates the percentages of time spent in each state during the simulation. The outcome shows the state percentages as a list, where each value represents the proportion of time spent in the corresponding state. In this example, the state percentages are approximately 43.09% for sunny, 29.47% for cloudy, 17.84% for rainy, and 9.6% for snowy.
