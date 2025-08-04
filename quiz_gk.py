def run_quiz():
    print("Welcome to the Indian General Knowledge Quiz!")
    print("You'll be asked 5 questions. Each has 4 options (A, B, C, D).")
    print("Answer carefully. You’ll get feedback after each question.\n")

    questions = [
        {
            "question": "What is the national bird of India?",
            "options": {
                "A": "Chicken",
                "B": "Peacock",
                "C": "Ostrich",
                "D": "Sparrow"
            },
            "answer": "B",
            "explanation": "Peacock is the national bird of India."
        },
        {
            "question": "What is the national animal of India?",
            "options": {
                "A": "Tiger",
                "B": "Lion",
                "C": "Zebra",
                "D": "Hippo"
            },
            "answer": "A",
            "explanation": "Tiger is the national animal of India."
        },
        {
            "question": "What is the national flower of India?",
            "options": {
                "A": "Rose",
                "B": "Lotus",
                "C": "Sunflower",
                "D": "Lily"
            },
            "answer": "B",
            "explanation": "Lotus is the national flower of India, symbolizing purity."
        },
        {
            "question": "What is the national currency of India?",
            "options": {
                "A": "Rupee",
                "B": "Yen",
                "C": "Dollar",
                "D": "Peso"
            },
            "answer": "A",
            "explanation": "The Indian Rupee (INR) is the official currency of India."
        },
        {
            "question": "Which is the national tree of India?",
            "options": {
                "A": "Neem",
                "B": "Banyan",
                "C": "Peepal",
                "D": "Mango"
            },
            "answer": "B",
            "explanation": "The Banyan tree is the national tree of India, known for its longevity and large canopy."
        }
    ]

    score = 0

    for idx, q in enumerate(questions, start=1):
        print(f"\nQuestion {idx}: {q['question']}")
        for option, value in q["options"].items():
            print(f"  {option}: {value}")
        
        user_answer = input("Your answer (A/B/C/D): ").strip().upper()

        if user_answer == q["answer"]:
            print("✅ Correct!")
            score += 1
        else:
            print(f"❌ Wrong! {q['explanation']}")

    print("\n--- Quiz Complete ---")
    print(f"Your score: {score} out of {len(questions)}")

    if score == len(questions):
        print("🎉 Excellent! You got all the answers right. ALL THE BEST!")
    elif score >= len(questions) // 2:
        print("👍 Good effort! Keep learning and improving.")
    else:
        print("📘 You might want to try again and learn from your mistakes.")

    print("Thanks for taking the quiz!")

# Run the quiz
if __name__ == "__main__":
    run_quiz()
