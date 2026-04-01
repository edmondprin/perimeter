# layer 1 (pure/testable functions)

import random 

def gen_question(sides):
    numbers = []
    for _ in range(sides):
        n = random.randint(1, 20)
        numbers.append(n)
    return numbers

def calculate_expected(my_list):
    # my_list = gen_question(sides)
    expected = sum(my_list)
    return expected

def check_result(answer_input, expected):
    return answer_input == expected


# layer 2 (workflow)

def run_quiz(iterations, sides, answer_func):
    points = 0
    detailed_question = []
    for i in range(iterations):
        n = gen_question(sides)
        expected = calculate_expected(n)
        answer_input = answer_func(n)
        result = check_result(answer_input, expected)
        if result is True:
            # print("Correct!")
            points += 1
        # else:
            # print(f"Incorrect! The result was {expected}")
        detailed_question.append((n, expected, answer_input, result))
    return points, detailed_question
    


# layer 3 (UI, I/O)

def main():
    min_sides = 3
    max_sides = 6
    iterations = 2
    while True:
        sides = input("Today we'll work on calculating perimeters. Enter the number of sides you want to work on. 3 is the minimum and 6 the maximum. Type 3 to work on triangles, 4 to work on rectangles, 5 to work on pentagons, and 6 to work on hexagons: ")
        try:
            sides = int(sides)
            if min_sides <= sides <= max_sides:
                break
        except ValueError:
            print(f"Enter number from {min_sides} to {max_sides}!")
    def answer_func(my_list):
        question_str = " + ".join(map(str, my_list))
        while True:
            answer_input = input(f"What is the perimeter of a form or shape with the following measurements: {question_str}? ")
            try: 
                answer_input = int(answer_input)
                return answer_input
            except ValueError:
                print("enter a number only!")
    points, detailed_questions = run_quiz(iterations, sides, answer_func)
    print(f"{points} points / {iterations}")
    for item in detailed_questions:
        n, expected, answer_input, result = item
        print(f"{' + '.join(map(str, n))} | Correct answer: {expected} | Your answer: {answer_input} | {'Good!' if result else 'Oops!'}")
    

if __name__ == "__main__":
    main()

