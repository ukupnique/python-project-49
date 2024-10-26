import random
from brain_games.engine import run_game

RULES = 'What number is missing in the progression?'


def gen_row():
    num_start = random.randint(1, 100)
    num = random.randint(1, 5)
    nums = []
    for i in range(10):
        num_start += num
        nums.append(num_start)
    return nums


def gen_row():
    num_start = random.randint(1, 100)
    num2 = random.randint(1, 5)
    mul = random.randint(1, 5)
    nums = []
    for i in range(10):
        num_start += num2 * (mul + i)
        nums.append(num_start)
    return nums


def brain_progression():
    run_game(generate_question, RULES)


def main():
    brain_progression()
