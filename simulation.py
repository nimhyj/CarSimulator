"""
Auto Driving Car Simulation

This program simulates a field where autonomous cars can move around based on user-defined commands. It uses a command-line interface
for input and output, allowing users to interact with the simulation in a step-by-step manner. The program incorporates several features
including the ability to:

1. Define the dimensions of the simulation field.
2. Add cars with unique names, initial positions, and directions within the field.
3. Define movement commands for each car using a simple instruction set (L, R, F).
4. Simulate the movement of all cars step-by-step, handling direction changes and forward movements.
5. Detect and report collisions between cars.

The program uses procedural programming but can be refactored into an Object-Oriented Programming (OOP) design for better scalability
and maintainability. This can involve introducing classes like `SimulationField`, `Car`, and `SimulationController`.

Key Functionalities:

1. Initialize Field: Users specify the width and height of the simulation field.
2. Add Cars: Users can add cars with attributes like name, initial position, and commands.
3. Simulate Movements: The program processes commands for all cars and updates their positions.
4. Handle Collisions: Detects and reports collisions, removing collided cars from the simulation.
5. Restart or Exit: Users can choose to restart the simulation or exit after running a simulation.

Usage:
1. Run the program and follow the instructions to define the field and cars.
2. Input valid commands and observe the simulation results.
3. Handle collisions and restart or exit as required.

Command Syntax:
- Directions: `N` (North), `S` (South), `E` (East), `W` (West)
- Commands: `L` (Turn Left), `R` (Turn Right), `F` (Move Forward)

Dependencies:
- Python 3.11

Example:
```bash
Welcome to Auto Driving Car Simulation!
Please enter the width and height of the simulation field in x y format: 5 5
You have created a field of 5 x 5.

Please choose from the following options:
[1] Add a car to field
[2] Run simulation

# Add a car and simulate its movement
```"""

import sys

def main():
    """
    The main function serves as the entry point for the Auto Driving Car Simulation program.
    It handles user interactions for setting up the simulation field, adding cars with initial positions
    and commands, and running the simulation to track the movements and detect collisions.

    Workflow:
    1. Prompt user to define the simulation field dimensions.
    2. Allow users to add cars with unique names, initial positions, directions, and movement commands.
    3. Simulate car movements based on commands while checking for collisions.
    4. Provide options to restart or exit the simulation after each run.
    """

    while True:
        print("Welcome to Auto Driving Car Simulation!\n")
        try:
            width, height = map(int, input("Please enter the width and height of the simulation field in x y format: ").split())
            if width <= 0 or height <= 0:
                raise ValueError("Field dimensions must be positive integers.")
            break
        except ValueError as e:
            print(f"Invalid input: {e}")

    print(f"You have created a field of {width} x {height}.\n")

    cars = []

    while True:
        print("Please choose from the following options:")
        print("[1] Add a car to field")
        print("[2] Run simulation")

        try:
            choice = int(input())
            if choice not in [1, 2]:
                raise ValueError("Please choose a valid option (1 or 2).")
        except ValueError as e:
            print(f"Invalid input: {e}")
            continue

        if choice == 1:
            while True:
                name = input("Please enter the name of the car: ").strip()
                if not name:
                    print("Car name cannot be empty.")
                    continue
                if any(car['name'] == name for car in cars):
                    print("Car name must be unique.")
                    continue
                break

            while True:
                try:
                    x, y, direction = input(f"Please enter initial position of car {name} in x y Direction format: ").split()
                    x, y = int(x), int(y)
                    direction = direction.upper()
                    if direction not in ['N', 'S', 'E', 'W']:
                        raise ValueError("Direction must be one of N, S, E, W.")
                    if not (0 <= x < width and 0 <= y < height):
                        raise ValueError("Position must be within field boundaries.")
                    if any(car['x'] == x and car['y'] == y for car in cars):
                        raise ValueError("Position is already occupied by another car.")
                    break
                except ValueError as e:
                    print(f"Invalid input: {e}")

            while True:
                commands = input(f"Please enter the commands for car {name}: ").strip().upper()
                if not all(c in 'LRF' for c in commands):
                    print("Commands can only contain L, R, and F.")
                    continue
                break

            cars.append({
                'name': name,
                'x': x,
                'y': y,
                'direction': direction,
                'commands': commands
            })

            print("\nYour current list of cars are:")
            for car in cars:
                print(f"- {car['name']}, ({car['x']},{car['y']}) {car['direction']}, {car['commands']}")
            print()

        elif choice == 2:
            if not cars:
                print("No cars to simulate. Please add cars first.\n")
                continue

            print("\nRunning simulation...")

            positions = {(car['x'], car['y']): car['name'] for car in cars}
            collision_logs = []

            for step in range(max(len(car['commands']) for car in cars)):
                """
                Simulation Loop Logic:
                - Iterate through each simulation step, processing one command per car.
                - Commands:
                  * 'L': Rotate the car 90 degrees counter-clockwise.
                  * 'R': Rotate the car 90 degrees clockwise.
                  * 'F': Move the car one unit forward in its current direction.
                - Detect collisions if two cars occupy the same position after a move.
                - Remove both cars involved in a collision from the simulation.
                """
                
                for car in cars:
                    if step >= len(car['commands']):
                        continue

                    command = car['commands'][step]

                    if command == 'L':
                        car['direction'] = {'N': 'W', 'W': 'S', 'S': 'E', 'E': 'N'}[car['direction']]
                    elif command == 'R':
                        car['direction'] = {'N': 'E', 'E': 'S', 'S': 'W', 'W': 'N'}[car['direction']]
                    elif command == 'F':
                        new_x, new_y = car['x'], car['y']
                        if car['direction'] == 'N':
                            new_y += 1
                        elif car['direction'] == 'S':
                            new_y -= 1
                        elif car['direction'] == 'E':
                            new_x += 1
                        elif car['direction'] == 'W':
                            new_x -= 1

                        if 0 <= new_x < width and 0 <= new_y < height:
                            if (new_x, new_y) in positions:
                                other_car = positions[(new_x, new_y)]
                                collision_logs.append((car['name'], other_car, new_x, new_y, step + 1))
                                print(f"\nCollision detected at step {step + 1} between {car['name']} and {other_car} at ({new_x}, {new_y}).")
                                cars = [c for c in cars if c['name'] not in {car['name'], other_car}]
                                break
                            else:
                                del positions[(car['x'], car['y'])]
                                car['x'], car['y'] = new_x, new_y
                                positions[(new_x, new_y)] = car['name']

                if collision_logs:
                    break

            print("\nAfter simulation, the result is:")
            for car in cars:
                print(f"- {car['name']}, ({car['x']},{car['y']}) {car['direction']}")
            for log in collision_logs:
                print(f"- {log[0]}, collides with {log[1]} at ({log[2]},{log[3]}) at step {log[4]}")

            print("\nPlease choose from the following options:")
            print("[1] Start over")
            print("[2] Exit")

            while True:
                try:
                    choice = int(input())
                    if choice not in [1, 2]:
                        raise ValueError("Please choose a valid option (1 or 2).")
                except ValueError as e:
                    print(f"Invalid input: {e}")
                    continue

                if choice == 1:
                    main()
                elif choice == 2:
                    print("Thank you for running the simulation. Goodbye!")
                    sys.exit()

if __name__ == "__main__":
    main()
