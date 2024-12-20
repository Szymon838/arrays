test_results = [
    False, True, False, True, True,
    True, True, False, True, True,
    False, True, True, True, False
]

number_of_questions = len(test_results)

correct_answers = 0
for answer in test_results:
    if answer:
        correct_answers += 1

incorrect_answers = number_of_questions - correct_answers

percentage_correct = (correct_answers / number_of_questions) * 100

print('TEST STATISTICS')
print('===============')
print('Number of questions:', number_of_questions)
print('Number of correct answers:', correct_answers)
print('Number of incorrect answers:', incorrect_answers)
print(f'Percentage of correct answers: {percentage_correct:.2f}%')