# Python Quiz App
from random import sample
from typing import TypedDict

# Explicit type hinting for the Data Structure Quiz_Bank using TypedDict
class QuizQuestion(TypedDict):
    Question: str
    Options: list[str]
    Answer: str

type quiz_bank = list[QuizQuestion]

TOTAL_QUESTIONS: int = 10

# Function that stores question set
def quiz_set() -> quiz_bank:

    quiz_question_bank: quiz_bank = [
        {
            "Question": "Which symbol is used to write a comment in Python ?",
            "Options": ["A. //", "B. #", "C. /* */", "D. --"],
            "Answer": "B",
        },
        {
            "Question": "Which of the following is a valid Python variable name?",
            "Options": ["A. 2name", "B. first-name", "C. first_name", "D. class"],
            "Answer": "C",
        },
        {
            "Question": "Which data type is used to store a sequence of items in order ?",
            "Options": ["A. Dictionary", "B. Set", "C. List", "D. Boolean"],
            "Answer": "C",
        },
        {
            "Question": "Which operator performs floor division in Python?",
            "Options": ["A. /", "B. %", "C. //", "D. **"],
            "Answer": "C",
        },
        {
            "Question": "Which keyword is used to define a function in Python ?",
            "Options": ["A. function", "B. func", "C. define", "D. def"],
            "Answer": "D",
        },
        {
            "Question": "Which function is used to determine the number of items in a list ?",
            "Options": ["A. count()", "B. size()", "C. length()", "D. len()"],
            "Answer": "D",
        },
        {
            "Question": "Which operator is used for exponentiation (raising to a power) in Python ?",
            "Options": ["A. ^", "B. **", "C. //", "D. %"],
            "Answer": "B",
        },
        {
            "Question": "Which of the following data types is immutable ?",
            "Options": ["A. List", "B. Dictionary", "C. Set", "D. Tuple"],
            "Answer": "D",
        },
        {
            "Question": "Which statement is used to make a decision in Python ?",
            "Options": ["A. for", "B. while", "C. if", "D. import"],
            "Answer": "C",
        },
        {
            "Question": "Which list method adds an item to the end of a list ?",
            "Options": ["A. insert()", "B. append()", "C. extend()", "D. add()"],
            "Answer": "B",
        },
    ]
    return quiz_question_bank

# Function that evaluates score metrics
def summarize_metrics(overall_score: int) -> None:
    print("\n=======Final Results=======")
    print(f"\nFinal score = {overall_score}/{TOTAL_QUESTIONS}")
    print(f"Percentage = {(overall_score/TOTAL_QUESTIONS*100):.0f}%\n")

# Function that chooses final Remark
def quiz_remark(overall_score: int) -> None:
    if overall_score == TOTAL_QUESTIONS:
        print("Outstanding !!!")
    elif overall_score == 0:
        print("Extremely Poor")
    elif overall_score < 4:
        print("Needs Improvement")
    elif overall_score < 7:
        print("Good Attempt !")
    elif overall_score < TOTAL_QUESTIONS:
        print("Excellent !!")

# Function that presents shuffled questions and tracks score.
def question_presenter() -> int:

    # To shuffle question order
    assorted_quiz: quiz_bank = sample(quiz_set(), k=TOTAL_QUESTIONS)
    overall_score: int = 0
    counter: int = 1 # For question number 

    for question in assorted_quiz:
        print(f"\nQuestion {counter}:\n{question['Question']}")

        option: str
        for option in question["Options"]:
            print(option)

        user_answer: str = (input("\nEnter your Option Letter: ")).lower()
        while not user_answer.startswith(("a","b","c","d")):
            print("Invalid format: Answer must contain Option Letter (e.g. , A, B, C or D)")
            user_answer: str = (input("\nEnter your Option with Answer: ")).lower()
        counter += 1

        if user_answer == ((question["Answer"]).lower()):
            print("Correct !")
            overall_score += 1
        else:
            print("Incorrect")
            print(f"Correct Answer was : {(question['Answer'])}")

    return overall_score

# Start of main program
def main() -> None:
    print("====== Quiz App ======\n")
    print("Start - s     Quit - q\n")
    choice: str = input("Enter choice: ")
    while choice.lower() == "s":
        overall_score: int = question_presenter()
        summarize_metrics(overall_score) # Invokes score metrics function
        quiz_remark(overall_score) # Invokes Remark function
        choice = (input("\nDo you want to Continue(s/q): ")).lower()
        while choice not in ["s", "q"]:  # Handles Invalid choice input
            print("Invalid choice entry")
            choice = input("\nDo you want to Continue(s/q): ")


main()
