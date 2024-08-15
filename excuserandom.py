import random

# List of excuses
excuses = [
    "My cat ate my homework.",
    "I was abducted by aliens.",
    "I had to save a family of ducks from a storm drain.",
    "I was in a time loop, reliving the same day for weeks.",
    "A wizard cursed me, and I turned into a newt. But I got better.",
    "I was on a secret mission for the government. Can't say more.",
    "My internet was kidnapped by ninjas.",
    "I accidentally joined a circus parade.",
    "I was busy inventing a new flavor of toothpaste.",
    "I got lost in a hedge maze. For three days."
]

def generate_excuse(task):
    """Generate and print a random excuse for not doing a specific task."""
    print(f"Here's your excuse for not doing {task}: {random.choice(excuses)}")

# Get user input for the task
task = input("What task are you trying to get out of? ")

# Generate the excuse
generate_excuse(task)