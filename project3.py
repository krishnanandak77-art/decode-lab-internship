# Initialize the score counter
score = 0

print("--- Welcome to the Quiz Game! ---")

# Question 1
answer1 = input("1. What is the capital of France? ").strip().lower()
if answer1 == "paris":
    print("Correct!")
    score += 1
else:
    print("Incorrect. The correct answer is Paris.")

# Question 2
answer2 = input("2. Which planet is known as the Red Planet? ").strip().lower()
if answer2 == "mars":
    print("Correct!")
    score += 1
else:
    print("Incorrect. The correct answer is Mars.")

# Question 3
answer3 = input("3. What is the largest ocean on Earth? ").strip().lower()
if answer3 == "pacific":
    print("Correct!")
    score += 1
else:
    print("Incorrect. The correct answer is Pacific.")

# Display final score
print("---------------------------------")
print(f"Game Over! Your final score is: {score}/3")
