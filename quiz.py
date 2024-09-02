# data
questions = [
    {
        "question": "What is the capital of France?",
        "options": ["A. Berlin", "B. Paris", "C. Rome", "D. Madrid"],
        "answer": "B"
    },
    {
        "question": "Which planet is known as the Red Planet?",
        "options": ["A. Earth", "B. Venus", "C. Mars", "D. Jupiter"],
        "answer": "C"
    },
    {
        "question": "Who wrote 'Hamlet'?",
        "options": ["A. Charles Dickens", "B. William Shakespeare", "C. Mark Twain", "D. Leo Tolstoy"],
        "answer": "B"
    }
]

# handling logic

def play_quiz():
    score = 0
    print("Welcome to the Quiz Game!\n")

    for i, q in enumerate(questions):
        print(f"Q{i + 1}: {q['question']}")
        for option in q['options']:
            print(option)
        
        answer = input("Your answer (A, B, C, D): ").upper()
        
        if answer == q['answer']:
            print("Correct!\n")
            score += 1
        else:
            print(f"Wrong! The correct answer was {q['answer']}.\n")
    
    print(f"Quiz finished! Your score is {score}/{len(questions)}.")

if __name__ == "__main__":
    play_quiz()

