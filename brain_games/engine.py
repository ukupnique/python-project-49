
def run_game(generate_question, rules):
    print("Welcome to the Brain Games!")
    name = input("May I have your name? ")
    print(f"Hello, {name}!")
    print(rules)

    true_answer_count = 0
    max_rounds = 3
    for _ in range(max_rounds):
        question, correct_answer = generate_question()
        print(f"Question: {question}")
        user_answer = input("Your answer: ")

        is_number = user_answer.strip('-').isdigit()
        is_correct = (is_number and int(user_answer) == correct_answer) or \
                     (user_answer.isalpha() and user_answer == correct_answer)

        if is_correct:
            print("Correct!")
            true_answer_count += 1
        else:
            print(f"'{user_answer}' is wrong answer ;(. ", end='')
            print(f"Correct answer was '{correct_answer}'.")
            print(f"Let's try again, {name}!")
            return

    print(f"Congratulations, {name}!")
