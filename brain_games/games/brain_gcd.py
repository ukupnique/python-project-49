import random
from brain_games.engine import run_game

RULES = 'Find the greatest common divisor of given numbers.'


def generate_question():
    num1 = random.randint(1, 100)
    num2 = random.randint(1, 100)
    question = f'{num1} {num2}'
    correct_answer = gsd(num1, num2)
    return question, correct_answer


def gsd(num1, num2):
    mi = min(num1, num2)
    ma = max(num1, num2)
    while ma % mi != 0:
        mi, ma = ma % mi, mi
    return mi


def brain_gsd():
    run_game(generate_question, RULES)


def main():
    brain_gsd()


if __name__ == "__main__":
    main()
