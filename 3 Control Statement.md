
### Conditional Statements

Conditional statements allow your program to make decisions and execute code accordingly. The most common conditional statements in Python are `if`, `elif` (short for else if), and `else`.

#### Syntax

```python
if condition:
    # code to execute if condition is True
elif another_condition:
    # code to execute if another_condition is True
else:
    # code to execute if all conditions are False
```

#### Example: Guess the Number Game

Let's create a simple "Guess the Number" game as an example. The game will generate a random number between 1 and 10, and the player will have three attempts to guess it.

```python
import random

# Generate a random number between 1 and 10
secret_number = random.randint(1, 10)

# Give the player three attempts to guess the number
for attempt in range(1, 4):
    guess = int(input(f"Attempt {attempt}: Guess a number between 1 and 10: "))

    # Check if the guess is correct
    if guess == secret_number:
        print("Congratulations! You guessed the number.")
        break
    elif guess < secret_number:
        print("Too low! Try again.")
    else:
        print("Too high! Try again.")

# If the player didn't guess the number in three attempts, reveal it
else:
    print(f"Sorry, you didn't guess the number. It was {secret_number}.")
```

In this game:
- The `if` statement checks if the player's guess is correct.
- The `elif` statement checks if the guess is too low.
- The `else` statement inside the loop provides feedback for incorrect guesses.
- The final `else` statement outside the loop reveals the secret number if the player fails to guess it after three attempts.

This example demonstrates how conditional statements can control the flow of a program based on user input and other conditions. Practice writing your own conditional statements to become more familiar with them. Happy coding! 😊


### For Loop

The `for` loop is used to iterate over a sequence (such as a list, tuple, dictionary, set, or string) or other iterable objects. Here's the syntax:

```python
for element in sequence:
    # code to execute for each element
```

#### Example: Sum of Numbers

```python
# Calculate the sum of numbers from 1 to 10
total = 0
for number in range(1, 11):
    total += number

print(f"The sum of numbers from 1 to 10 is: {total}")
```

This will output: "The sum of numbers from 1 to 10 is: 55"

### While Loop

The `while` loop continues to execute a block of code as long as a given condition is true. Here's the syntax:

```python
while condition:
    # code to execute while condition is True
```

#### Example: Countdown Timer

```python
# A simple countdown timer
count = 10
while count > 0:
    print(f"Countdown: {count}")
    count -= 1

print("Blast off!")
```

This will output a countdown from 10 to 1, followed by "Blast off!"

### Best Practices

- Use `for` loops when you know the number of iterations in advance.
- Use `while` loops when the number of iterations is not known beforehand.
- Always ensure that the loop has a condition that will eventually become false to avoid infinite loops.

Loops are powerful tools that can simplify your code and make it more efficient. Practice using them in different scenarios to master their use. Happy coding! 😊


### Break Statement

The `break` statement is used to exit a loop prematurely when a certain condition is met. Here's an example:

```python
# Using break to exit a loop
for number in range(1, 11):
    if number == 5:
        break  # Exit the loop when number is 5
    print(number)
```

This will output numbers from 1 to 4, and then exit the loop.

### Continue Statement

The `continue` statement skips the current iteration of a loop and proceeds with the next one. Here's an example:

```python
# Using continue to skip even numbers
for number in range(1, 11):
    if number % 2 == 0:
        continue  # Skip even numbers
    print(number)
```

This will output only odd numbers from 1 to 9.

### Pass Statement

The `pass` statement is a placeholder and does nothing. It's used when you need a statement syntactically but don't want any command or code to execute. Here's an example:

```python
# Using pass as a placeholder
for number in range(1, 11):
    if number == 5:
        pass  # Do nothing when number is 5
    else:
        print(number)
```

This will output numbers from 1 to 10, but when the number is 5, it will do nothing and continue with the next iteration.

These statements are useful for controlling the execution of loops based on specific conditions. Practice using them to gain a better understanding of their functionality. Happy coding! 😊