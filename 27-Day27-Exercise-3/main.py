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
        "options": ["Python", "Photoshop", "Microsoft Word", "Adobe Illustrator"],
        "correct_answer": "Python"
    },
    {
        "question": "What is the chemical symbol for carbon?",
        "options": ["C", "Ca", "Co", "Cu"],
        "correct_answer": "C"
    },
    {
        "question": "Who painted 'The Starry Night'?",
        "options": ["Vincent van Gogh", "Pablo Picasso", "Leonardo da Vinci", "Claude Monet"],
        "correct_answer": "Vincent van Gogh"
    },
    {
        "question": "What is the capital city of Brazil?",
        "options": ["Brasilia", "Rio de Janeiro", "São Paulo", "Salvador"],
        "correct_answer": "Brasilia"
    }
]

user_score = 0
user_corret_answers = 0
user_wrong_answers = 0
user_skip_questions = 0
print('You will earn ₹1000 on each correct answer and You will lose ₹100 on each wrong answer and if you skip the question neither You\'ll earn nor you lose.\n')
print('Type (quit) to exit the game or You can skip the question just by Pressing Enter.\n')
for question in questions:
    print(question['question'])
    print(question['options'][0])
    print(question['options'][1])
    print(question['options'][2])
    print(question['options'][3])
    user_answer = str(input('Enter Your Answer: ')).lower()
    if user_answer=='quit':break
    if not user_answer.strip():
        print('You Skipped the Question.\n')
        user_skip_questions = user_skip_questions+1
        continue
    if user_answer==str(question['correct_answer']).lower():
        print('You are Correct.\n')
        user_score = user_score+1000
        user_corret_answers = user_corret_answers+1
    else:
        print('You are Wrong.\n')
        user_score = user_score-100
        user_wrong_answers = user_wrong_answers+1
if user_score<=0:user_score=0
print(f'Your correct answers were {user_corret_answers}, wrong answers were {user_wrong_answers} and You skipped {user_skip_questions} Questions. So as per the Calculations. Your Total Earning is ₹{user_score}')