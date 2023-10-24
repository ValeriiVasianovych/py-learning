# Python Programming Course

## Level 1: Introduction to Python

### Module 0: Introduction
- What is Python (Что такое Python)
- Python history and popularity (История и популярность)
- Installing Python (multiple platforms) (Установка Python)
- Using Python interpreters (IDLE, command line) (Использование интерпретаторов Python)
- Integrated Development Environments (IDEs) (Интегрированные среды разработки)

### Module 1: Python Basics
- Variables and assignment (Переменные и присваивание)
- Data types: int, float, str (Типы данных: int, float, str)
- Basic operations and expressions (Базовые операции и выражения)
- Input and output (Ввод и вывод)
- Comments and code style (Комментарии и стиль кода)

**Practical Assignments:**
1. Create a Python program that takes user input for their name and greets them using that input.
2. Calculate the area of a circle with a given radius and print the result.
3. Write a Python program that takes a sentence as input and counts the number of words in it.

### Module 2: Control Structures
- Conditional statements (if, elif, else) (Условные операторы)
- Loops (while, for) (Циклы)
- Iteration and looping techniques (Итерация и техники циклов)
- Break and continue statements (Операторы break и continue)
- Error handling (try, except) (Обработка ошибок)

**Practical Assignments:**
1. Write a Python program that checks whether a given number is even or odd and prints the result.
2. Create a program that prints the first 10 natural numbers using a while loop.
3. Use a for loop to iterate through a list of names and print a greeting for each name, but skip names that start with the letter 'A'.

### Module 3: Data Structures
- Lists, tuples, and dictionaries (Списки, кортежи и словари)
- List comprehensions (Списковые включения)
- Sets and frozensets (Множества)
- Working with sequences (range, enumerate, zip) (Работа с последовательностями)
- Built-in data structures (collections) (Встроенные структуры данных)

**Practical Assignments:**
1. Create a Python program that takes user input to build a list of numbers. Then, write a function to find and print the maximum and minimum values in the list. Additionally, calculate and print the average of all the numbers in the list.
2. Implement a Python dictionary to create a simple address book. Users can add, remove, or search for contact information using their names. Write functions for each of these operations.
3. Write a Python program that takes a list of words as input and generates a new list containing only the unique words (eliminating duplicates). Use sets to help you achieve this. Then, count and print the number of occurrences of each unique word in the original list.

## Level 2: Intermediate Python

### Module 4: Functions and Modules
- Defining functions (Объявление функций)
- Function parameters and arguments (Параметры и аргументы функций)
- Function return values (Возвращаемые значения функций)
- Scopes and namespaces (Области видимости и пространства имен)
- Importing modules and packages (Импорт модулей и пакетов)

**Practical Assignments:**
1. Define a Python function that calculates the factorial of a given number and call it with an example number.
2. Create a module with a function that calculates the square of a number. Import this module and use the function in a separate Python script.
3. Write a Python function that accepts a list of numbers and returns the sum of all the even numbers in the list.

### Module 5: File Handling
- File I/O best practices (Лучшие практики работы с файлами)
- Reading and writing text files (open, read, write) (Чтение и запись текстовых файлов)
- Working with binary files (Чтение и запись двоичных файлов)
- File and directory manipulation (os, sys, pathlib, shutil) (Работа с файлами и каталогами)
- Exception handling in file operations (Обработка исключений при работе с файлами)
- Working with CSV, JSON, XML, and YAML files + configparser (Работа с CSV, JSON, XML и YAML файлами)
- subprocess, sys.argv (Работа с внешними процессами и аргументами командной строки)
- requests (HTTP запросы)
- API basics (API основы и простые запросы и ответы)

**Practical Assignments:**
### Module 5: File Handling

1. Create a text file named "sample.txt" and write several lines of text in it. Then open the file and print its content to the console. (Import: `open`, `read`)
2. Create a new text file named "output.txt" and write some lines of text to it. Then add a few more lines to the same file without erasing the previous content. (Import: `open`, `write`)
3. Create a binary file and write binary data, such as bytes or numbers, to it. Then read the data from the file and print it. (Import: `open`)
4. Using the `os` module, create a new directory named "my_directory" in the current working directory. Then create a text file in this directory and write some data to it. (Import: `os`)
5. Attempt to read a file that doesn't exist and handle the exception that occurs. (Import: `try`, `except`)
6. Create a file "data.csv" and use the `csv` module to write and read data in CSV format. Create a dataset and save it to this file, then read and print the data to the screen. (Import: `csv`)
7. Create a JSON file with some data and use the `json` module to write and read JSON structures. (Import: `json`)
8. Create an XML file representing some data and use the `xml` module to read and process this XML file. (Import: `xml`)
9. Create a configuration file using the `configparser` module and use it to store and read settings for your program. (Import: `configparser`)
10. Write a program that takes a command-line argument (sys.argv) and prints its value. (Import: `sys`)
11. Use the `subprocess` module to execute an external command, such as "ls" on Linux or "dir" on Windows, and print the command's output to the console. (Import: `subprocess`)
12. Use the `requests` library to send an HTTP request to a web resource (e.g., a website) and print the received response. (Import: `requests`)
13. Learn the basics of working with APIs by sending a GET request to an open API (e.g., JSONPlaceholder) and processing the received data. (Import: `requests`)
14. Create a directory using the `pathlib` module and create a text file with some content in this directory. Then read the contents of this file. (Import: `pathlib`)
15. Try to delete a non-existent file using the `shutil` module and handle the exception. Then copy a file from one directory to another. (Import: `shutil`)
16. Create a YAML file representing some data and use the `PyYAML` module to write and read data from the file. (Import: `PyYAML`)
17. Create a function that takes a file name and checks if it exists. If the file exists, the function should return True; otherwise, it should return False.
18. Write a program that iterates through all files in the current working directory and prints their names and sizes.
19. Create a text file containing several URL addresses. Using the `requests` library, make HTTP requests to each of the URLs and print the HTTP response status.
20. Implement a simple web server using the `http.server` module. The server should listen on port 8080 and serve files from the current working directory. After starting the server, open a web browser and try to access files in the current directory through the browser.



### Module 6: Pythonic Coding
- List comprehensions and generators (Списковые включения и генераторы)
- Decorators and closures (Декораторы и замыкания)
- Context managers and with statements (Контекстные менеджеры и операторы with)
- Lambda functions (Анонимные функции)
- Object-oriented programming basics (Основы объектно-ориентированного программирования)

**Practical Assignments:**
1. Implement a Python decorator that logs the execution time of a function and the arguments passed to it. Apply this decorator to a few functions and analyze the results.
2. Create a context manager that captures exceptions and logs them. Use this context manager to handle exceptions in a block of code and display custom error messages.
3. Write a Python program that uses lambda functions to filter a list of numbers, keeping only the even ones. Use the filter function and a lambda expression to achieve this.

### Module 7: Regular Expressions
- Introduction to regular expressions (Введение в регулярные выражения)
- Pattern matching and searching (Поиск и сопоставление шаблонов)
- Pattern substitution and manipulation (Замена и манипуляция шаблонов)
- Using the `re` module (Использование модуля `re`)
- Advanced regex techniques (lookahead, lookbehind) (Продвинутые техники регулярных выражений)

**Practical Assignments:**
1. Develop a Python script that validates email addresses. Use regular expressions to ensure that the provided email addresses follow a valid format (e.g., username@domain.com). Test your script with various email addresses to verify its accuracy.
2. Write a Python program that extracts all the phone numbers (including international formats) from a given text. Use regular expressions to identify and print these phone numbers.
3. Create a Python program that reads a text file and replaces all occurrences of a specific word with another word of your choice. Use regular expressions for this task, and make sure to preserve the case of the replaced word.

### Module 8: Functional Programming
- Functional programming concepts (Чистые функции, неизменяемость, отсутствие побочных эффектов)
- Map, filter, and reduce functions (Функции map, filter и reduce)
- Anonymous functions (lambda) (Анонимные функции)
- Functional programming libraries (functools) (Библиотеки функционального программирования)

**Practical Assignments:**
1. Implement a Python function that calculates the factorial of a number using recursion. Make sure your function follows the principles of functional programming, such as immutability and avoiding side effects.
2. Create a list of integers and use the map function to square each element in the list. Then, use the filter function to select only the squared values that are divisible by 5.
3. Write a Python program that calculates the sum of all prime numbers in a given range using the reduce function. You will need to define a helper function for prime number checking and then use reduce to accumulate the sum.

## Level 3: Advanced Python

### Module 9: Object-Oriented Programming
- Classes and objects
- Inheritance and polymorphism
- Encapsulation and data hiding
- Special methods (dunworder methods)
- Advanced OOP concepts

**Practical Assignments:**
1. Define a Python class for a basic shape (e.g., a circle or rectangle) with methods to calculate area and perimeter. Create instances and use these methods.
2. Create a subclass of the shape class that adds functionality specific to triangles. Demonstrate inheritance and polymorphism.
3. Implement a simple object that demonstrates encapsulation and data hiding principles.

### Module 10: Concurrency and Multithreading
- Understanding threads and processes
- Threading in Python
- Synchronization and thread safety
- Multiprocessing and parallelism
- Asynchronous programming with asyncio

**Practical Assignments:**
1. Write a Python program that uses multithreading to download multiple files concurrently.
2. Create a Python script that simulates a scenario where multiple threads need to access a shared resource and demonstrate thread synchronization.
3. Implement a simple asynchronous Python program that performs multiple tasks concurrently using the asyncio library.

### Module 11: Data Manipulation and Analysis
- Working with data libraries (NumPy, Pandas)
- Data analysis and visualization
- Data cleaning and transformation
- Statistics and data exploration
- Real-world data projects

**Practical Assignments:**
1. Use NumPy to create a NumPy array and perform basic operations like mean, median, and standard deviation on it.
2. Read a CSV file using Pandas and perform data cleaning operations such as removing missing values and duplicates.
3. Visualize a dataset using Matplotlib or another Python data visualization library.

### Module 12: Web Development with Python
- Introduction to web development frameworks (Django, Flask)
- Creating web applications
- Routing and views
- Templates and front-end integration
- Building RESTful APIs

**Practical Assignments:**
1. Create a basic web application using a Python web framework of your choice (Django or Flask). Implement a simple "Hello, World!" view.
2. Add a new route to your web application that takes user input through a form and displays it on a separate page.
3. Extend your web application to serve static files (e.g., CSS, JavaScript) and demonstrate how to integrate them into your templates.

### Module 13: Databases and Data Persistence
- Relational databases (SQLite, MySQL, PostgreSQL)
- Database design and modeling
- SQL and database operations
- NoSQL databases (MongoDB)
- ORM (Object-Relational Mapping)

**Practical Assignments:**
1. Create a SQLite database with a table for storing user information (e.g., name, email). Write SQL queries to insert and retrieve data.
2. Use an ORM (e.g., SQLAlchemy) to define a Python class representing a table in a database and perform database operations (insert, update, query) using this class.
3. Set up a connection to a NoSQL database (e.g., MongoDB) and perform basic CRUD operations using a Python library or driver.
