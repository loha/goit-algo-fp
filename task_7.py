import random

def simulate_dice_rolls(num_rolls):
  """Simulates rolling two dice multiple times and calculates probabilities.

  Args:
    num_rolls: The number of times to roll the dice.

  Returns:
    A dictionary containing the sum as keys and the corresponding probability as values.
  """

  sum_counts = {}
  for _ in range(num_rolls):
    dice1 = random.randint(1, 6)
    dice2 = random.randint(1, 6)
    total = dice1 + dice2
    sum_counts[total] = sum_counts.get(total, 0) + 1

  total_rolls = sum(sum_counts.values())
  probabilities = {sum: count / total_rolls for sum, count in sum_counts.items()}
  return probabilities

# Number of simulations
num_simulations = 1000000

# Perform the simulation
simulated_probabilities = simulate_dice_rolls(num_simulations)

# Print the results
print("Simulated Probabilities:")
for sum, probability in simulated_probabilities.items():
  print(f"Sum {sum}: {probability:.4f}")

# Compare with analytical results
# ... (you can implement a comparison function here)

