"""
André is testing a new feature in Buscante's backend that processes data in a loop.
During testing, he noticed that the system stopped responding, and he suspects the issue lies in an infinite loop.

counter = 0

while counter < 10:
    print("Processing data...")

What is the issue with André's code, and how can it be resolved?
"""

counter = 0

while counter < 10:
    print(f"Processing data from file {counter+1}...")
    counter += 1 # Updates the counter to avoid the infinite loop
