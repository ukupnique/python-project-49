import random
from brain_games.engine import run_game

RULES = 'What number is missing in the progression?'


def generate_question():
    row = gen_row()
    pos = random.randint(0, 4)
    correct_answer = row[pos]
    row[pos] = '..'
    question = ' '.join(map(str, row))
    return question, correct_answer


def gen_row():
    num_start = random.randint(1, 100)
    num = random.randint(1, 5)
    nums = []
    for i in range(10):
        num_start += num
        nums.append(num_start)
    return nums


def brain_progression():
    run_game(generate_question, RULES)


def main():
    brain_progression()
