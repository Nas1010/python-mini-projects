import random

word_list = [
    {'portuguese': 'o', 'english': 'the'},
    {'portuguese': 'a', 'english': 'the'},
    {'portuguese': 'de', 'english': 'of/from'},
    {'portuguese': 'que', 'english': 'that/what'},
    {'portuguese': 'e', 'english': 'and'},
    {'portuguese': 'do', 'english': 'of the'},
    {'portuguese': 'da', 'english': 'of the (feminine)'},
    {'portuguese': 'em', 'english': 'in/on'},
    {'portuguese': 'um', 'english': 'a/an (masculine)'},
    {'portuguese': 'para', 'english': 'for/to'},
    {'portuguese': 'é', 'english': 'is'},
    {'portuguese': 'com', 'english': 'with'},
    {'portuguese': 'não', 'english': 'no/not'},
    {'portuguese': 'uma', 'english': 'a/an (feminine)'},
    {'portuguese': 'os', 'english': 'the (plural)'},
    {'portuguese': 'no', 'english': 'in the (masculine)'},
    {'portuguese': 'se', 'english': 'if'},
    {'portuguese': 'na', 'english': 'in the (feminine)'},
    {'portuguese': 'por', 'english': 'by/through'},
    {'portuguese': 'mais', 'english': 'more'},
    {'portuguese': 'as', 'english': 'the (feminine plural)'},
    {'portuguese': 'dos', 'english': 'of the (plural)'},
    {'portuguese': 'como', 'english': 'like/as'},
    {'portuguese': 'mas', 'english': 'but'},
    {'portuguese': 'foi', 'english': 'was'},
    {'portuguese': 'ao', 'english': 'to the (masculine)'},
    {'portuguese': 'ele', 'english': 'he'},
    {'portuguese': 'das', 'english': 'of the (feminine plural)'},
    {'portuguese': 'à', 'english': 'to the (feminine)'},
    {'portuguese': 'seu', 'english': 'his/your'},
    {'portuguese': 'sua', 'english': 'her/your'},
    {'portuguese': 'ou', 'english': 'or'},
    {'portuguese': 'ser', 'english': 'to be'},
    {'portuguese': 'tem', 'english': 'has'},
    {'portuguese': 'tudo', 'english': 'everything'},
    {'portuguese': 'essa', 'english': 'that (feminine)'},
    {'portuguese': 'num', 'english': 'in a'},
    {'portuguese': 'também', 'english': 'also'},
    {'portuguese': 'são', 'english': 'are'},
    {'portuguese': 'só', 'english': 'only/just'},
    {'portuguese': 'pelo', 'english': 'by the'},
    {'portuguese': 'pela', 'english': 'by the (feminine)'},
    {'portuguese': 'até', 'english': 'until'},
    {'portuguese': 'isso', 'english': 'that (thing)'},
    {'portuguese': 'ela', 'english': 'she'},
    {'portuguese': 'entre', 'english': 'between'},
    {'portuguese': 'era', 'english': 'was'},
    {'portuguese': 'depois', 'english': 'after'},
    {'portuguese': 'sem', 'english': 'without'},
    {'portuguese': 'mesmo', 'english': 'same'},
    {'portuguese': 'aos', 'english': 'to the (plural)'},
    {'portuguese': 'ter', 'english': 'to have'},
    {'portuguese': 'seus', 'english': 'his/your (plural)'},
    {'portuguese': 'quem', 'english': 'who'},
    {'portuguese': 'nas', 'english': 'in the (feminine plural)'},
    {'portuguese': 'me', 'english': 'me'},
    {'portuguese': 'meu', 'english': 'my'},
    {'portuguese': 'te', 'english': 'you (object)'},
    {'portuguese': 'porque', 'english': 'because'},
    {'portuguese': 'há', 'english': 'there is/there are'},
    {'portuguese': 'nós', 'english': 'we'},
    {'portuguese': 'nos', 'english': 'us'},
    {'portuguese': 'meus', 'english': 'my (plural)'},
    {'portuguese': 'minha', 'english': 'my (feminine)'},
    {'portuguese': 'minhas', 'english': 'my (feminine plural)'},
    {'portuguese': 'dele', 'english': 'his'},
    {'portuguese': 'dela', 'english': 'her'},
    {'portuguese': 'tu', 'english': 'you (informal singular)'},
    {'portuguese': 'fazer', 'english': 'to do/make'},
    {'portuguese': 'quando', 'english': 'when'},
    {'portuguese': 'bem', 'english': 'well'},
    {'portuguese': 'nunca', 'english': 'never'},
    {'portuguese': 'sempre', 'english': 'always'},
    {'portuguese': 'vou', 'english': 'I go/I’m going'},
    {'portuguese': 'está', 'english': 'is (temporary)'},
    {'portuguese': 'estou', 'english': 'I am (temporary)'},
    {'portuguese': 'era', 'english': 'was'},
    {'portuguese': 'vamos', 'english': 'let’s go'},
    {'portuguese': 'sei', 'english': 'I know'},
    {'portuguese': 'sabe', 'english': 'knows'},
    {'portuguese': 'deu', 'english': 'gave'},
    {'portuguese': 'disse', 'english': 'said'},
    {'portuguese': 'lá', 'english': 'there'},
    {'portuguese': 'aqui', 'english': 'here'},
    {'portuguese': 'coisa', 'english': 'thing'},
    {'portuguese': 'hoje', 'english': 'today'},
    {'portuguese': 'ontem', 'english': 'yesterday'},
    {'portuguese': 'agora', 'english': 'now'},
    {'portuguese': 'tempo', 'english': 'time'},
    {'portuguese': 'vida', 'english': 'life'},
    {'portuguese': 'ano', 'english': 'year'},
    {'portuguese': 'dia', 'english': 'day'},
    {'portuguese': 'homem', 'english': 'man'},
    {'portuguese': 'mulher', 'english': 'woman'},
    {'portuguese': 'muito', 'english': 'a lot/very'},
    {'portuguese': 'pouco', 'english': 'little/few'},
    {'portuguese': 'grande', 'english': 'big'},
    {'portuguese': 'novo', 'english': 'new'},
    {'portuguese': 'velho', 'english': 'old'},
    {'portuguese': 'bom', 'english': 'good'},
    {'portuguese': 'ruim', 'english': 'bad'},
]

def quiz_user(word_list):
    random.shuffle(word_list)
    score = 0
    
    for word in word_list:
        print(f'What is the Engish translation of "{word["portuguese"]}"?')
        user_answer = input('Your answer: ').strip().lower()
        correct_answer = word['english'].lower()

        if user_answer == correct_answer:
            print('Correct Answer ✅\n')
            score+= 1
            
        else:
            print(f'Wrong ❌ The correct answer is "{word["english"]}" \n')
    
    print(f'Quiz complete, you scored {score} out of {len(word_list)}!')
    

def main():
    print('Welcome to the Language Learning flashcards App!')
    input('Press enter to start the quiz...')
    quiz_user(word_list)

if __name__ == '__main__':
    main()