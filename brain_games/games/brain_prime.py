import random
from brain_games.engine import run_game


RULES = 'Answer "yes" if given number is prime. Otherwise answer "no".'


def is_prime(num):
    if num <= 1:
        return False
    for i in range(2, int(num * 0.5) + 1):
        if num % i == 0:
            return False
    return True


def generate_question():
    num = random.randint(3, 50)
    question = num
    if is_prime(num):
        correct_answer = 'yes'
    else:
        correct_answer = 'no'
    return question, correct_answer


def brain_prime():
    run_game(generate_question, RULES)


def main():
    brain_prime()
