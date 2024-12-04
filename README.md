# Auto Driving Car Simulation

This repository contains the **Auto Driving Car Simulation** program and its accompanying test suite. The simulation mimics a field where autonomous cars operate based on user-defined commands, enabling users to test scenarios such as car movements, boundary constraints, and collision detection.

---

## Project Structure

- **`simulation.py`**: The main script for the Auto Driving Car Simulation program.
- **`test_simulation.py`**: A comprehensive test suite using `unittest` to validate the program's functionality.

---

## Features

### Simulation Features:
1. **Field Definition**:
   - Users can define the dimensions of the simulation field.

2. **Car Initialization**:
   - Add cars with unique names, initial positions, and directions within the field.

3. **Movement Commands**:
   - Use a simple command set (`L`, `R`, `F`) to control cars:
     - `L`: Turn Left
     - `R`: Turn Right
     - `F`: Move Forward

4. **Collision Detection**:
   - Handle scenarios where cars collide during simulation.

5. **Boundary Validation**:
   - Prevent cars from being initialized or moving outside the field boundaries.

6. **Simulation Results**:
   - Output the state of all cars after the simulation.

### Test Suite Highlights:
- Validates core functionalities:
  - Adding cars
  - Simulating movements
  - Detecting collisions
  - Enforcing boundary constraints
- Uses `unittest` and `unittest.mock` for automated testing.

---

## Installation

### Prerequisites
- Python 3.11.1 or higher

### Steps
1. Clone the repository:
   ```bash
   git clone https://github.com/nimhyj/CarSimulator.git
   cd auto-driving-car-simulation
   ```
2. Install dependencies (if required):
   ```bash
   pip install -r requirements.txt
   ```

---

## Usage

### Run the Simulation
To start the simulation, execute the `simulation.py` script:
```bash
python simulation.py
```

Follow the prompts to:
1. Define the field dimensions.
2. Add cars with their names, initial positions, and directions.
3. Input movement commands for each car.
4. View the simulation results.

### Run the Test Suite
To ensure all features work correctly, execute the test suite:
```bash
python -m unittest test_simulation.py
```

---

## Example

### Input:
```
Enter field dimensions (width height): 5 5
Enter the number of cars: 1
Enter car name: CarA
Enter initial position and direction (x y D): 2 2 N
Enter movement commands: FFRFF
Enter 1 to add another car or 2 to start the simulation: 2
```

### Output:
```
You have created a field of 5 x 5.
Your current list of cars are:
CarA, (2,2) N, FFRFF
After simulation, the result is:
CarA, (4,4) E
```

---

## Contribution

Contributions are welcome! To contribute:
1. Fork the repository.
2. Create a feature branch.
3. Commit your changes.
4. Open a pull request.

---

## License

This project is licensed under the MIT License. See the `LICENSE` file for details.

---

## Acknowledgements

- Built with Python's `unittest` framework.
- Inspired by autonomous driving simulation projects.

---

Feel free to reach out for any queries or suggestions!

