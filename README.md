# Package Sorting System

## Overview
This project provides a `sort` function that categorizes packages based on their dimensions and mass.

## Sorting Rules
- **Bulky**: Volume ≥ 1,000,000 cm³ or any dimension ≥ 150 cm.
- **Heavy**: Mass ≥ 20 kg.
- **Categories**:
  - `STANDARD`: Not bulky or heavy.
  - `SPECIAL`: Bulky or heavy.
  - `REJECTED`: Both bulky and heavy.

## Usage
```python
def sort(width, height, length, mass) -> str:
```
- Returns one of: `"STANDARD"`, `"SPECIAL"`, or `"REJECTED"`.

### Example
```python
print(sort(100, 100, 100, 19))  # "SPECIAL"
print(sort(50, 50, 50, 21))    # "SPECIAL"
print(sort(100, 100, 100, 21)) # "REJECTED"
print(sort(30, 40, 50, 10))    # "STANDARD"
```

## Running Tests
Run the test suite using:
```sh
python3 -m unittest tests.py
```
