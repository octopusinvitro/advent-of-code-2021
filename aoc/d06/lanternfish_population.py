from .state import State


class LanternfishPopulation:
    def simulate(self, initial_states, days):
        counts_per_state = self._load(initial_states)

        for day in range(days):
            counts = counts_per_state.pop(State.SPAWN.value)
            counts_per_state[State.RESET.value] += counts
            counts_per_state.append(counts)

        return counts_per_state

    def _load(self, initial_states):
        counts_per_state = [0] * (State.START.value + 1)

        for state in initial_states:
            counts_per_state[state] += 1

        return counts_per_state
