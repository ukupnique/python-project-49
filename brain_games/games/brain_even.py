import random
from brain_games.engine import run_game


RULES = 'Answer "yes" if the number is even, otherwise answer "no".'


def generate_question():
    num = random.randint(1, 100)
    question = num
    correct_answer = ''
    if num % 2 == 0:
        correct_answer = 'yes'
    elif num % 2 != 0:
        correct_answer = 'no'
    return question, correct_answer


def brain_even():
    run_game(generate_question, RULES)


def main():
    brain_even()


if __name__ == "__main__":
    main()
