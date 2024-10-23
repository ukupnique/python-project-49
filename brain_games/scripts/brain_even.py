import prompt
import random


def welcome_message():
    print("Welcome to the Brain Games!")


def get_user_name():
    return prompt.string("May I have your name? ")


def ask_question():
    return random.randint(0, 1000)


def check_answer(answ, number):
    return (answ == 'yes' and number % 2 == 0) or (answ == 'no' and number % 2 != 0)


def brain_even():
    welcome_message()
    name = get_user_name()
    print(f"Hello, {name}!")
    true_answer = 0
    print('Answer "yes" if the number is even, otherwise answer "no".')

    while true_answer < 3:
        number = ask_question()
        print(f'Question: {number}')
        answ = prompt.string("Your answer: ")

        if check_answer(answ, number):
            print('Correct!')
            true_answer += 1
        else:
            correct_answ = 'yes' if number % 2 == 0 else 'no'
            print(f"'{answ}' is wrong answer ;(. Correct answer was '{correct_answ}'.")
            break

    if true_answer == 3:
        print(f'Congratulations, {name}!')
    else:
        print(f"Let's try again, {name}!")


def main():
    brain_even()


if __name__ == "__main__":
    main()
