
# Hexl Library

## Overview

`Hexl` is a Python library designed to create and manipulate unique hexadecimal IDs. These IDs can be iterated, compared, and used in arithmetic operations. This library includes various methods to generate hexadecimal IDs, convert between decimal and hexadecimal, and perform mathematical operations on these values.

## Features

- **Hexadecimal ID Generation**: Generate random 8-digit hexadecimal IDs.
- **Decimal-to-Hexadecimal Conversion**: Convert decimal values to their hexadecimal equivalents and vice-versa.
- **Iterability**: The hexadecimal ID can be iterated over.
- **Mathematical Operations**: Support for addition, subtraction, multiplication, division, exponentiation, and more with hexadecimal values.
- **Comparison Operations**: Hexadecimal values can be compared using standard comparison operators.

## Class: `hexl`

### Attributes

- **hexl_ID**: A string representing an 8-digit hexadecimal value. It can be either provided by the user or randomly generated.

### Methods

- `__init__(self, hexl_ID: Union[str, int])`: Initializes the `hexl` instance with a hexadecimal ID. If no ID is provided, a random one will be generated.
- `generate_hex() -> hexl`: Generates a random 8-digit hexadecimal ID.
- `to_hex(values: Union[str, int]) -> str`: Converts a decimal or string value into a hexadecimal string.
- `__iter__()`: Makes the hexadecimal ID iterable.
- `__repr__()`: Returns a string representation of the `hexl` instance, showing both the hexadecimal and decimal values.
- `__str__()`: Returns the hexadecimal ID as a string.
- `__int__() -> int`: Converts the hexadecimal ID to its decimal equivalent.
- `__len__() -> int`: Returns the length of the hexadecimal ID.
- `__eq__(self, hex: str) -> bool`: Compares the hexadecimal ID with another string for equality.
- Mathematical operations: `__add__`, `__sub__`, `__mul__`, `__pow__`, `__floordiv__`, `__truediv__` for arithmetic operations with hexadecimal values.
- Comparison operators: `__le__`, `__lt__`, `__ge__`, `__gt__` for comparing hexadecimal values.
- Reflexive operations: `__radd__`, `__rsub__`, `__rmul__`, `__rpow__`, `__rfloordiv__`, `__rtruediv__` for operations where the left-hand side is not a `hexl` instance.
- `__hash__()`: Returns the hash value of the hexadecimal ID.

## Example Usage

```python
from hexl import hexl

# Creating a random hexadecimal ID
hex_instance = hexl()

# Creating a hexadecimal ID from a decimal or string
hex_from_str = hexl("A12FFBD0")
hex_from_int = hexl(12345)

# Performing mathematical operations
result = hex_from_str + 10
result_mul = hex_from_str * 2

# Converting to decimal
decimal_value = int(hex_from_str)

# Comparing hexadecimal IDs
is_equal = hex_instance == "A12FFBD0"
is_greater = hex_instance > hex_from_str
```

## Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/username/hexl-library.git
   ```

2. Install the required dependencies (if any):
   ```bash
   pip install -r requirements.txt
   ```

## License

This project is licensed under the MIT License.
