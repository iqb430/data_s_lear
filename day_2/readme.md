# 100 Days of Data Science - Day 2

**Python Fundamentals Continued** 🐍🚀

## Today's Progress
- Built upon Day 1's Python basics
- Explored core programming concepts:
  - Data types and variables
  - Control structures (loops and conditionals)
  - Basic error handling
  - Functions and modular programming
- Created a simple number guessing game
- Practiced GitHub workflow with daily commits

## Key Concepts Covered
### 📊 Data Types
- Integers, floats, strings, booleans
- Type conversion (`int()`, `str()`, `float()`)
- Basic string operations

### 🔄 Control Structures
- `if-elif-else` statements
- `for` and `while` loops
- Loop control (`break`, `continue`)

### 📦 Functions
- Function definition and invocation
- Parameters and return statements
- Scope of variables

### 🛟 Error Handling
- Basic `try-except` blocks
- Handling common exceptions

## What I Learned/Accomplished
1. Consolidated Python basics through practical exercises
2. Created my first interactive game using fundamental concepts
3. Understood the importance of clean code and documentation
4. Practiced daily GitHub commits for version control

```python
# Sample code from number guessing game
import random

def guess_game():
    target = random.randint(1, 100)
    attempts = 0
    
    while True:
        try:
            guess = int(input("Guess a number between 1-100: "))
            attempts += 1
            
            if guess < target:
                print("Higher!")
            elif guess > target:
                print("Lower!")
            else:
                print(f"🎉 Correct! Guessed in {attempts} attempts")
                break
                
        except ValueError:
            print("Please enter a valid number!")

guess_game()
