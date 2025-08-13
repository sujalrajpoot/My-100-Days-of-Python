questions = [
    {
        "question": "Who is known as the 'Father of the Nation' in India?",
        "options": ["Mahatma Gandhi", "Jawaharlal Nehru", "Subhash Chandra Bose", "Sardar Vallabhbhai Patel"],
        "correct_answer": "Mahatma Gandhi"
    },
    {
        "question": "Which planet is known as the 'Red Planet'?",
        "options": ["Mars", "Venus", "Mercury", "Saturn"],
        "correct_answer": "Mars"
    },
    {
        "question": "Who painted the Mona Lisa?",
        "options": ["Leonardo da Vinci", "Pablo Picasso", "Vincent van Gogh", "Michelangelo"],
        "correct_answer": "Leonardo da Vinci"
    },
    {
        "question": "What is the capital city of Australia?",
        "options": ["Canberra", "Sydney", "Melbourne", "Perth"],
        "correct_answer": "Canberra"
    },
    {
        "question": "Which of the following is a mammal?",
        "options": ["Whale", "Shark", "Turtle", "Crocodile"],
        "correct_answer": "Whale"
    },
    {
        "question": "What is the currency of Japan?",
        "options": ["Yen", "Dollar", "Euro", "Pound"],
        "correct_answer": "Yen"
    },
    {
        "question": "Who wrote 'To Kill a Mockingbird'?",
        "options": ["Harper Lee", "J.K. Rowling", "Stephen King", "Charles Dickens"],
        "correct_answer": "Harper Lee"
    },
    {
        "question": "What is the chemical symbol for water?",
        "options": ["H2O", "CO2", "NaCl", "O2"],
        "correct_answer": "H2O"
    },
    {
        "question": "Which country is famous for the Taj Mahal?",
        "options": ["India", "China", "Egypt", "Italy"],
        "correct_answer": "India"
    },
    {
        "question": "Who discovered penicillin?",
        "options": ["Alexander Fleming", "Marie Curie", "Isaac Newton", "Albert Einstein"],
        "correct_answer": "Alexander Fleming"
    },
    {
        "question": "What is the largest mammal in the world?",
        "options": ["Blue Whale", "African Elephant", "Giraffe", "Hippopotamus"],
        "correct_answer": "Blue Whale"
    },
    {
        "question": "What is the capital city of France?",
        "options": ["Paris", "London", "Berlin", "Rome"],
        "correct_answer": "Paris"
    },
    {
        "question": "Who is the author of 'Harry Potter' series?",
        "options": ["J.K. Rowling", "J.R.R. Tolkien", "C.S. Lewis", "George R.R. Martin"],
        "correct_answer": "J.K. Rowling"
    },
    {
        "question": "What is the chemical symbol for gold?",
        "options": ["Au", "Ag", "Fe", "Pb"],
        "correct_answer": "Au"
    },
    {
        "question": "Which is the longest river in the world?",
        "options": ["Nile", "Amazon", "Yangtze", "Mississippi"],
        "correct_answer": "Nile"
    },
    {
        "question": "Who composed the 'Symphony No. 9'?",
        "options": ["Ludwig van Beethoven", "Wolfgang Amadeus Mozart", "Johann Sebastian Bach", "Franz Schubert"],
        "correct_answer": "Ludwig van Beethoven"
    },
    {
        "question": "Which of the following is a programming language?",
        "options": ["Microsoft Word", "Adobe Illustrator", "Python", "Photoshop"],
        "correct_answer": "Python"
    }
]

level_money = [1000, 2000, 3000, 5000, 10000, 20000, 40000, 80000, 160000, 320000, 640000, 1250000, 2500000, 5000000, 7500000, 10000000, 75000000]
user_level = 1
money = 0
question_number = 1
user_skip_questions = 0
user_corret_answers = 0
user_wrong_answers = 0
user_name = str(input('Please Enter Your Name: ')).capitalize()
if not user_name.strip():print('You cannot Enter in the Game Without Giving Your Name');quit()
print(f'Welcome {user_name}! in KBC of Sujal Rajpoot.\n')
for question in questions:
    print(f">> {user_name}, your {question_number} question for ₹{level_money[user_level-1]}, your current earning is ₹{money}, and your question is:\n{question['question']}")
    option_a = question['options'][0]
    option_b = question['options'][1]
    option_c = question['options'][2]
    option_d = question['options'][3]
    print(f"A. {option_a}          B. {option_b}")
    print(f"C. {option_c}          D. {option_d}\n")
    
    dict_of_options = {'a': option_a, 'b': option_b, 'c': option_c, 'd': option_d}

    while True:
        user_answer = str(input('Enter any option from (A), (B), (C), (D) or type "quit" to exit: ')).lower()
        if user_answer == 'quit':
            break
        if not user_answer.strip():
            print('You skipped the question.\n')
            user_skip_questions = user_skip_questions+1
            user_level = user_level+1
            break
        if user_answer in dict_of_options:
            if dict_of_options[user_answer] == question['correct_answer']:
                print('You are correct.\n')
                money = money+level_money[user_level-1]
                user_corret_answers = user_corret_answers+1
            else:
                print('You are wrong.\n')
                money = money-level_money[user_level-1]
                user_wrong_answers = user_wrong_answers+1
            user_level = user_level+1
            break
        else:
            print('Invalid option. Please enter A, B, C, or D.\n')

    question_number = question_number+1
    if money<=0:money=0
    if user_answer == 'quit':
        break

print(f'Your correct answers were {user_corret_answers}, wrong answers were {user_wrong_answers} and You skipped {user_skip_questions} Questions. So as per the Calculations. Your Total Earning is ₹{money}')