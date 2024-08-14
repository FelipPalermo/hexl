# Hexadecimal ID Library

Welcome to the Hexadecimal ID Library! This Python library provides utilities for working with hexadecimal numbers, including generating unique IDs. 
It offers a range of functions for hexadecimal operations and is designed to be both powerful and easy to use.

## Features

- **Generate Hexadecimal IDs:** Create unique 8-digit hexadecimal IDs.
- **Hexadecimal to Decimal Conversion:** Convert hexadecimal strings to their decimal equivalents.
- **Character Conversion:** Convert alphabetical characters (A-F) into hexadecimal values.
- **ID Operations:** Perform operations like addition and comparison on hexadecimal IDs.
- **Iterability:** The `ID` class supports iteration and comparison.

## Installation

To get started with the Hexadecimal ID Library, you can clone the repository and install any dependencies:

```bash
git clone https://github.com/FelipPalermo/hex_functions
cd hex_functions
pip install -r requirements.txt
```

## Usage 
```python
from hexadecimal_id_library import hex_functions, ID

# Generate a random hexadecimal ID
id_number = hex_functions.generate_hex_ID()
ID1 = ID(id_number)
print(f"ID1 in decimal: {int(ID1)}")

# Perform an esoteric sum of two hexadecimal IDs
z = ID1.esoteric_ID_sum(hex_functions.generate_hex_ID())
print(f"Esoteric sum result: {z}")
```

## TODO

Here are the upcoming tasks and improvements planned for the Hexadecimal ID Library:

Develop UML Diagrams: Create detailed UML diagrams for better understanding of the architecture.
Enhance Docstrings: Improve existing docstrings for better documentation and usability.
Implement Assignment and Search Functions: Add functionalities for assigning and searching IDs.
Set Up NoSQL Database: Design and implement a NoSQL database system.
Create 256-bit Hash Key: Develop a unitary key with a 256-bit hash for database access.
Build Simplified Database Library: Create a library for optimized and simplified database connections and queries.
Contributing

Contributions are welcome! Feel free to fork the repository, submit pull requests, and report any issues.

# License

This project is licensed under the [MIT License](https://opensource.org/licenses/MIT).

