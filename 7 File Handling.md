# Chapter 7: File Handling

### Introduction to File Handling

File handling is a crucial part of any programming language, including Python. It allows you to create, read, update, and delete files. Python provides built-in functions and methods to handle files, making it easy to work with file operations.

### Opening a File

To work with a file, you first need to open it using the `open()` function. This function returns a file object and takes two parameters: the file name and the mode.

```python
# Opening a file in read mode
file = open('example.txt', 'r')
```

### Modes of Opening a File

- **'r'**: Read mode (default)
- **'w'**: Write mode (overwrites the file)
- **'a'**: Append mode (adds to the end of the file)
- **'x'**: Create mode (creates a new file)
- **'b'**: Binary mode
- **'t'**: Text mode (default)

### Reading from a File

Once a file is opened in read mode, you can read its contents using methods like `read()`, `readline()`, or `readlines()`.

```python
# Reading the entire content of the file
content = file.read()
print(content)

# Reading one line at a time
line = file.readline()
print(line)

# Reading all lines into a list
lines = file.readlines()
print(lines)
```

### Writing to a File

To write to a file, you need to open it in write or append mode. You can then use the `write()` method to write data to the file.

```python
# Opening a file in write mode
file = open('example.txt', 'w')

# Writing to the file
file.write('Hello, World!')

# Closing the file is important to save changes
file.close()
```

### Closing a File

It's important to close files after you're done with them using the `close()` method. This frees up system resources.

```python
# Closing the file
file.close()
```

### Using 'with' Statement

The `with` statement automatically takes care of closing the file once the block of code is executed.

```python
# Using 'with' statement for better resource management
with open('example.txt', 'r') as file:
    content = file.read()
    print(content)
```

### Practical Examples and Output

Let's see some practical examples of reading from and writing to files:

```python
# Writing multiple lines to a file
with open('example.txt', 'w') as file:
    lines = ['Line 1\n', 'Line 2\n', 'Line 3\n']
    for line in lines:
        file.write(line)

# Reading from the same file
with open('example.txt', 'r') as file:
    content = file.read()
    print(content)
```

**Output:**
```
Line 1
Line 2
Line 3
```

### Exercises

1. Write a Python program that reads a text file and prints its content.
2. Write a Python program that writes your name and age to a text file.
3. Modify the previous program to append your favorite color to the same text file.

---

This chapter should provide you with a comprehensive understanding of how to handle files in Python. It's important to practice by writing your own programs that involve reading from and writing to files. Happy coding! 😊

---

Working with different file types is an essential skill in Python, as it allows you to handle various data formats commonly used in data processing and storage. Here's a brief overview of how to work with text, CSV, and JSON files in Python:

### Text Files

Text files are the simplest file type to work with. You can read and write text files using the built-in `open()` function.

```python
# Writing to a text file
with open('example.txt', 'w') as file:
    file.write('Hello, World!')

# Reading from a text file
with open('example.txt', 'r') as file:
    content = file.read()
    print(content)
```

### CSV Files

CSV (Comma-Separated Values) files are used to store tabular data. Python's `csv` module provides functionality to read from and write to CSV files.

```python
import csv

# Writing to a CSV file
with open('example.csv', 'w', newline='') as file:
    writer = csv.writer(file)
    writer.writerow(['Name', 'Age'])
    writer.writerow(['Alice', 30])
    writer.writerow(['Bob', 25])

# Reading from a CSV file
with open('example.csv', 'r') as file:
    reader = csv.reader(file)
    for row in reader:
        print(row)
```

### JSON Files

JSON (JavaScript Object Notation) files are used for storing and exchanging data. Python's `json` module allows you to work with JSON data.

```python
import json

# Writing to a JSON file
data = {'name': 'Alice', 'age': 30}
with open('example.json', 'w') as file:
    json.dump(data, file)

# Reading from a JSON file
with open('example.json', 'r') as file:
    data = json.load(file)
    print(data)
```

### Exercises

1. Write a Python program that reads a CSV file and prints each row.
2. Write a Python program that writes a dictionary to a JSON file.
3. Modify the previous program to read the JSON file and print the dictionary.

---

This overview should help you get started with working different file types in Python. Remember to practice by creating your own programs that involve reading from and writing to these files. Happy coding! 😊

---

Using context managers in Python is a best practice for handling resources like files, network connections, or locks. Context managers ensure that resources are properly acquired and released, even if errors occur during the execution of the block of code.

The most common way to use a context manager is with the `with` statement. Here's an example of using a context manager to handle file operations:

```python
# Using a context manager to open and read a file
with open('example.txt', 'r') as file:
    content = file.read()
    print(content)
```

In this example, the `open()` function returns a file object that is a context manager. The `with` statement ensures that the file is automatically closed after the block of code is executed, even if an exception is raised.

### Advantages of Using Context Managers

- **Automatic Resource Management**: They automatically manage resources, ensuring they are properly released.
- **Exception Safety**: They provide a safe way to handle exceptions without leaving resources open.
- **Code Readability**: They make the code cleaner and more readable by abstracting away the resource management details.

### Exercises

1. Write a Python program that uses a context manager to write to a file.
2. Use a context manager to handle opening and closing multiple files in a single block of code.

---

This explanation should help you understand the importance and usage of context managers in Python. It's important to practice by writing your own programs that use context managers to handle various resources. Happy coding! 😊