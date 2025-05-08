questions = [
    {
        'prompt': 'Who is Eva Smith most closely associated with in the play’s timeline before her death?',
        'options': ['A) Edna', 'B) Sheila', 'C) All of the Birlings and Gerald', 'D) Inspector Goole'],
        'answer': 'C) All of the Birlings and Gerald',
    },
    {
        'prompt': 'What theme does the Inspector’s final speech most strongly convey?',
        'options': ['A) Capitalism', 'B) Love and family', 'C) Social responsibility and collective guilt', 'D) Gender roles'],
        'answer': 'C) Social responsibility and collective guilt',
    },
    {
        'prompt': 'What does the Inspector’s name suggest about his character?',
        'options': ['A) He is a ghost', 'B) He is a policeman', 'C) He is a priest', 'D) He is a teacher'],
        'answer': 'A) He is a ghost',
    },
    {
        'prompt': 'What does the Inspector’s arrival signify in the play?',
        'options': ['A) A change in the weather', 'B) The end of the Birlings’ happiness', 'C) The beginning of a new era', 'D) The arrival of a new character'],
        'answer': 'B) The end of the Birlings’ happiness',
    },
    {
        'prompt': 'What does the Inspector’s final speech suggest about the future?',
        'options': ['A) It will be better', 'B) It will be worse', 'C) It will be the same', 'D) It is uncertain'],
        'answer': 'D) It is uncertain',
    }
]

def run_quiz(questions):
    score = 0
    for question in questions:
        print(question['prompt'])
        for option in question['options']:
            print(option)
        answer = input('Enter your answer (A, B, C or D): ')
        if answer == question['answer']:
            print('Correct, hooray!!\n')
            score += 1
        else:
            print('Wrong, the correct was', question['answer'], '\n')

    print(f'You got {score} out of {len(questions)} questions correct.')

run_quiz(questions)           