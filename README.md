## Min Cars Needed Function

A Python function to determine the **minimum number of cars** required to transport a group of people, where each car has a certain number of passengers and available seats. The goal is to take as few cars as possible on the trip. 


## Problem Statement

A group of friends is going on a trip. They arrive at a meeting point using `N` cars. Each car is represented by:

- `P[K]`: number of people who travelled to the meeting point in the car
- `S[K]`: number of seats available in the car

They want to **combine cars** so that everyone fits, and use as **few cars as possible**, leaving the rest parked.

## Examples:

1. `P = [1, 4, 1]`, `S = [1, 5, 1]` → **2 cars used**  
2. `P = [4, 4, 2, 4]`, `S = [5, 5, 2, 5]` → **3 cars used**  
3. `P = [2, 3, 4, 2]`, `S = [2, 5, 7, 2]` → **2 cars used**

## Solution Overview

- Calculate the total number of people to transport
- Sort the cars by seat count in descending order
- Add one car at a time until the total seat count is enough
- Return the number of cars used
- Includes input validation for types and values

## How to Run

### Requirements
- Python 3.7+
- `pytest` for running tests

### Install Dependencies
```bash
pip install -r requirements.txt
```

### Run the Function
```bash
python app.py
```

### Run the Tests
```bash
pytest
```

## Test Coverage

- Valid input cases and edge cases
- Empty lists, zero passengers
- Input validation (negative numbers, non-integers)
- Scenarios with too few seats
- Large-scale inputs

## Assumptions
- Everyone must be seated
- If not enough seats are available, across all cars, a ValueError is raised
