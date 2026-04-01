## About
* Small Python program designed to test the user's skills with calculating the perimeter of a shape.<br />
* Test file including thorough testing with 1000 random iterations for a single test function.<br />

## Requirements
* Python installed on your machine: https://www.python.org/downloads/ <br />
* Pytest installed via pip: https://docs.pytest.org/en/7.1.x/getting-started.html <br />

## How to run
* python3 perimeter.py<br /> 

## How to run the tests
* pytest test_perimeter.py<br />

## What it demonstrates
* 3-layer architecture (separation of concerns), to make sure layer 1 and 2 functions are fully testable and do no contain side effects such as input or print statements.<br />
* Higher-order functions and dependency injection, allowing run_quiz() to be tested with a lambda function instead of real user input.<br />
* Test-driven development with pytest: Thepytest framework makes it easy to write small, readable tests, and can scale to support complex functional testing for applications and libraries.<br />
* Mass testing with random iterations, to make sure edge cases are covered.<br />
