import random
from brain_games.engine import run_game


RULES = 'What is the result of the expression?'
OPERATIONS = ['+', '-', '*']


def generate_question():
    num1 = random.randint(1, 100)
    num2 = random.randint(1, 100)
    operation = random.choice(OPERATIONS)
    question = f"{num1} {operation} {num2}"
    correct_answer = eval(f"{num1} {operation} {num2}")
    return question, correct_answer


def brain_calc():
    run_game(generate_question, RULES)


def main():
    brain_calc()


if __name__ == "__main__":
    main()
