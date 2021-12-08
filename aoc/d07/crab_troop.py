from statistics import median, mean


class CrabTroop:
    def __init__(self, positions):
        self._positions = positions

    def linear_optimal_fuel_costs(self):
        optimal_position = int(median(self._positions))

        return self._differences(self._linear_fuel_cost, optimal_position)

    def quadratic_optimal_fuel_costs(self):
        optimal_position = int(mean(self._positions))

        return self._differences(self._quadratic_fuel_cost, optimal_position)

    def quadratic_optimal_fuel_cost(self):
        minimum_cost = float('inf')

        for potential_optimal in range(min(self._positions), max(self._positions) + 1):
            total_cost = sum(self._differences(self._quadratic_fuel_cost, potential_optimal))
            minimum_cost = min(minimum_cost, total_cost)

        return minimum_cost

    def _differences(self, cost_function, optimal_position):
        return [cost_function(abs(position - optimal_position)) for position in self._positions]

    def _linear_fuel_cost(self, steps):
        return steps

    def _quadratic_fuel_cost(self, steps):
        return (steps + 1) * steps / 2
