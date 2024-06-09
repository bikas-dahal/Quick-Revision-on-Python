# Python Quiz Project

Here's the Project for the "Interactive Quiz Game" project, along with explanations and expected output:

```python
# Interactive Quiz Game

# List of questions and answers
questions = [
    {"question": "What is the capital of France?", "answer": "Paris"},
    {"question": "What is 2 + 2?", "answer": "4"},
    {"question": "What is the largest mammal?", "answer": "Blue Whale"}
]

# Function to ask a question and check the answer
def ask_question(question):
    user_answer = input(question["question"] + " ")
    if user_answer.lower() == question["answer"].lower():
        print("Correct!")
        return True
    else:
        print("Incorrect!")
        return False

# Main game loop
score = 0
for question in questions:
    if ask_question(question):
        score += 1

# Display the final score
print(f"Your final score is: {score}/{len(questions)}")

# Output example:
# What is the capital of France? Paris
# Correct!
# What is 2 + 2? 4
# Correct!
# What is the largest mammal? Blue Whale
# Correct!
# Your final score is: 3/3
```

#### Explanation:

- We start by defining a list of dictionaries, `questions`, where each dictionary contains a question and its correct answer.
- The `ask_question` function takes a question dictionary as an argument, asks the user for their answer, and checks if it's correct. It returns `True` for a correct answer and `False` otherwise.
- In the main game loop, we iterate over each question in the `questions` list. For each question, we call `ask_question` and increment the `score` variable if the answer is correct.
- After all questions have been asked, we print out the final score.

#### Expected Output:

The output will vary depending on the user's answers. If all answers are correct, the output will be:

```
Your final score is: 3/3
```

If some answers are incorrect, the output will reflect the number of correct answers out of the total number of questions.

This project demonstrates how to use variables, functions, loops, and conditional statements in Python to create an interactive game. It's a fun way to practice coding skills and apply what you've learned! 😊