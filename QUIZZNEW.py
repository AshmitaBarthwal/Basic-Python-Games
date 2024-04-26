# ANSI escape codes for colors
GREEN = '\033[92m'
RED = '\033[91m'
ENDC = '\033[0m'  # Reset color

def print_separator():
    print("^*^*^*^*^*^*^*^*^*^*^*")

def check_answer(user_guess, correct_answer):
    return user_guess == correct_answer

score = 0

questions = [
    {"text": "Which country is known as the 'Land of the Rising Sun'?", "Answer": "B"},
    {"text": "The Great Barrier Reef is located off the coast of which country?", "Answer": "B"},
    {"text": "In which mountain range is Mount Everest located?", "Answer": "A"},
    {"text": "Which river is the longest in the world?", "Answer": "C"},
    {"text": "Which ocean is the largest by area?", "Answer": "D"}
]

options = [
    ["A. China", "B. Japan", "C. South Korea", "D. Thailand"],
    ["A. Mexico", "B. Australia", "C. Brazil", "D. Thailand"],
    ["A. Himalayas", "B. Alps", "C. Rocky Mountains", "D. Andes"],
    ["A. Amazon River", "B. Mississippi River", "C. Nile River", "D. Yangtze River"],
    ["A. Atlantic Ocean", "B. Indian Ocean", "C. Southern Ocean", "D. Pacific Ocean"]
]

# Welcome message
print("WELCOME TO MY QUIZ GAME!")
print("LET'S TEST YOUR GENERAL KNOWLEDGE.GOOD LUCK !")

for ques_num in range(len(questions)):
    print("                      ")
    print_separator()
    print(questions[ques_num]["text"])
    for i in options[ques_num]:
        print(i)
    guess = input("Enter Your Answer (A/B/C/D): ").upper()

    is_correct = check_answer(guess, questions[ques_num]["Answer"])
    
    if is_correct:
        print(GREEN + "** CORRECT ANSWER **" + ENDC)
        score += 1
    else:
        print(RED + "** INCORRECT ANSWER **" + ENDC)
        print("!!!!!!!!!!!")
        print(f" CORRECT ANSWER IS {questions[ques_num]['Answer']} ")
    print(f"YOUR CURRENT SCORE ---> {score}/{ques_num + 1}")

percentage_score = score / len(questions) * 100
percentage_emoji = '🎉' if percentage_score >= 70 else '😕'  # Choose emojis based on the percentage

print("\n" + "=" * 30)
print(f"YOU HAVE GIVEN {score} CORRECT ANSWERS")
print(f"YOUR SCORE PERCENTAGE IS --> {percentage_score:.2f}% {percentage_emoji}")
print("=" * 30)
