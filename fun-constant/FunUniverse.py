import random
import matplotlib.pyplot as plt
from typing import List

# Define the ultimate constant
FUN_CONSTANT = 42

class FunUniverse:
    def __init__(self, initial_fun_level: float = 10.0, decay_rate: float = 0.1):
        """Initialize the Fun Universe with a fun level and decay rate."""
        self.fun_level = initial_fun_level
        self.decay_rate = decay_rate
        self.time_steps: List[float] = []
        self.fun_history: List[float] = []
        self.happiness_index = 0.0
        self.happiness_history: List[float] = []

    def inject_fun(self) -> None:
        """Inject a random amount of fun, apmlified by the FUN_CONSTANT."""
        fun_boost = random.uniform(1, 5) * FUN_CONSTANT
        self.fun_level += fun_boost
        self.happiness_index += fun_boost * 0.5 # Happiness scales with fun

    def decay_fun(self) -> None:
        """Apply natural decay to fun level (life's entropy, you know)"""
        self.fun_level *= (1 - self.decay_rate)
        if self.fun_level < 0:
            self.fun_level = 0
    
    def simulate_step(self, step: int) -> None:
        """Simulate one time step in the universe."""
        self.inject_fun()
        self.decay_fun()
        self.time_steps.append(step)
        self.fun_history.append(self.fun_level)
        self.happiness_history.append(self.happiness_index)
        print(f"Step {step}: Fun Level = {self.fun_level:.2f}, Happiness Index = {self.happiness_index:.2f}")

    def run_simulation(self, steps: int) -> None:
        """Run the simulation for a given number of steps."""
        print("Starting Fun Universe Simulation...")
        for step in range(steps):
            self.simulate_step(step)
        self.visualize()

    def visualize(self) -> None:
        """Visualize Fun Level and Happiness Index over time with numerical annotations."""
        plt.figure(figsize=(12, 6))  # Larger figure for clarity
        
        # Plot Fun Level
        plt.plot(self.time_steps, self.fun_history, label="Fun Level", color="purple", marker="o")
        # Annotate Fun Level values
        for i, (x, y) in enumerate(zip(self.time_steps, self.fun_history)):
            plt.text(x, y + 50, f"{y:.2f}", color="purple", fontsize=8, ha="center")

        # Plot Happiness Index
        plt.plot(self.time_steps, self.happiness_history, label="Happiness Index", color="orange", marker="s")
        # Annotate Happiness Index values
        for i, (x, y) in enumerate(zip(self.time_steps, self.happiness_history)):
            plt.text(x, y - 50, f"{y:.2f}", color="orange", fontsize=8, ha="center")

        plt.title("Fun Universe: Fun Level and Happiness Index Over Time")
        plt.xlabel("Time Steps")
        plt.ylabel("Value")
        plt.grid(True)
        plt.legend()
        plt.tight_layout()  # Adjust layout to prevent label clipping
        plt.show()
    
def main():
    # Create a universe where fun is the driving force
    universe = FunUniverse(initial_fun_level=10.0, decay_rate=0.05)
    
    # Run the simulation for 20 steps
    universe.run_simulation(steps=20)

    # Reflect on the importance of fun
    print("\nConclusion: In this universe, FUN_CONSTANT drives happiness and progress.")
    print(f"Final Happiness Index: {universe.happiness_index:.2f}")
    print("Keep maximizing fun, because it's the constant that matters most!")

if __name__ == "__main__":
    main()

# The final happiness index is a strong quantitative argument that prioritizing fun leads to outsized positive outcomes.

