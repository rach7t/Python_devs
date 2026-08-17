
quiz = [
    {"question": "What is the capital of France?", "answer": "Paris"},
    {"question": "What is 5 + 7?", "answer": "12"},
    {"question": "Which planet is known as the Red Planet?", "answer": "Mars"},
    {"question": "How many states are in the United States?", "answer": "50"},
    {"question": "What is the largest ocean on Earth?", "answer": "Pacific"},
    {"question": "What is the square root of 64?", "answer": "8"},
    {"question": "Which gas do plants absorb during photosynthesis?", "answer": "Carbon Dioxide"},
    {"question": "What is the boiling point of water in Celsius?", "answer": "100"},
    {"question": "Who painted the Mona Lisa?", "answer": "Leonardo da Vinci"},
    {"question": "What is the chemical symbol for Gold?", "answer": "Au"}
]

score = 0

print("--- Welcome to the 10-Question Quiz! ---\n")


for i, item in enumerate(quiz, 1):
    user_answer = input(f"Q{i}: {item['question']}\nYour Answer: ").strip()
    
    if user_answer.lower() == item['answer'].lower():
        print("Correct! 🎉\n")
        score += 1
    else:
        print(f"Wrong! The correct answer is: {item['answer']}\n")

print("--- Quiz Finished ---")
print(f"Your final score: {score} out of 10")