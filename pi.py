import random

def estimate_pi(n):
		num_point_circle = 0
		num_point_total = 0
		for _ in range(n):
				x = random.uniform(0, 1)
				y = random.uniform(0, 1)
				distance = x**2 + y**2
				if distance <= 1:
						num_point_circle += 1
				num_point_total += 1
		return 4 * num_point_circle / num_point_total

# Get user input
try:
		n = int(input("Enter the number of dots to generate: "))
		if n <= 0:
				print("Please enter a positive integer.")
		else:
				pi_estimate = estimate_pi(n)
				print(f"Estimated value of Pi: {pi_estimate}")
except ValueError:
		print("Invalid input! Please enter a valid integer.")
