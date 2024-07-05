import random
import time

class SimulationRobobo:
    def __init__(self):
        self.position = [5, 5]  # Starting position in the middle of a 10x10 grid
        self.grid_size = 10
        self.obstacles = {(2, 2), (2, 3), (3, 2), (7, 7), (8, 7), (7, 8)}  # Example obstacles
        self.simulation_running = False

    def read_irs(self):
        """Simulate reading infrared sensors. Return random values simulating sensor readings."""
        ir_values = [random.randint(0, 100) for _ in range(9)]
        # Simulate proximity to obstacles
        if tuple(self.position) in self.obstacles:
            ir_values[7] = 100  # Simulate high sensor value if at obstacle
        return ir_values

    def move_blocking(self, left_wheel_speed, right_wheel_speed, duration):
        """Simulate moving the robot. Update position based on wheel speeds."""
        if not self.simulation_running:
            return
        # Simplified movement logic: Update position based on speeds
        if left_wheel_speed > right_wheel_speed:
            self.position[0] = max(0, self.position[0] - 1)  # Move left
        elif right_wheel_speed > left_wheel_speed:
            self.position[0] = min(self.grid_size - 1, self.position[0] + 1)  # Move right
        else:
            self.position[1] = min(self.grid_size - 1, self.position[1] + 1)  # Move forward

        # Simulate duration of the movement
        time.sleep(duration / 1000.0)

    def sleep(self, duration):
        """Simulate sleeping."""
        time.sleep(duration)

    def play_simulation(self):
        """Start the simulation."""
        self.simulation_running = True
        print("Simulation started")

    def stop_simulation(self):
        """Stop the simulation."""
        self.simulation_running = False
        print("Simulation stopped")


