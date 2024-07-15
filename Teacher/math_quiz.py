import random

score = 0

for _ in range(5):
    num1 = random.randint(1,10)
    num2 = random.randint(1,10)
    operations = random.choice(["+","-","*","/"])


if operations == "/":
    num1 = num1 * num2


question = f"what is {num1} {operations} {num2}?"
correct_answer = eval(f"{num1} {operations} {num2}")
answer = float(input(question +" "))
if answer == correct_answer:
    print("Correct!")
    score += 1
else:
    print(f"Wrong! The correct answer was {correct_answer}")

print(f"Your final score is  {score}/5")