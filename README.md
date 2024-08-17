# Hexadecimal ID Library

Welcome to the Hexadecimal ID Library! This Python library provides utilities for working with hexadecimal numbers, including generating unique IDs. 
It offers a range of functions for hexadecimal operations and is designed to be both powerful and easy to use.

## Features

- **Hexadecimal to Decimal Conversion:** Convert hexadecimal strings to their decimal equivalents.
- **Character Conversion:** Convert strings "A25F" into hexadecimal values.
- **Iterability:** The `hexl` class supports iteration and comparison.

## Installation

To get started with the Hexadecimal ID Library, you can clone the repository and install any dependencies:

```bash
git clone https://github.com/FelipPalermo/hexl
cd hexl
pip install -r requirements.txt
```

## Usage 
```python
import hexl 

# Generate a random hexadecimal 
hexadecimal_number = hexl.generate_hex() # 8 digit random 
# or 
hexadecimal_number = hexl() # 8 digit random  

# Start hexadecimal number 
hexadecimal = hexl(999) # start with Int or "string"

# Get int / decimal of the hexl instance 
hint = int(hexadecimal) 

# Convert to hex / hexl. Works with int and "string" 
decimal = 1250
hexadecimal = hexl.to_hex(decimal)



## TODO

Here are the upcoming tasks and improvements planned for the hexl ID Library:

-  Set Up NoSQL Database: Design and implement a NoSQL database system.
-  Build Simplified Database Library: Create a library for optimized and simplified database connections and queries.


# License
This project is licensed under the [MIT License](https://opensource.org/licenses/MIT).

