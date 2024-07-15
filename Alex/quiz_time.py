import random

score = 0

for _ in range(5):
    num1 = random.randint(1,999)
    num2 = random.randint(1,999)
    operations = random.choice(["+","-","*","/"])

if operations == "/":
    num1 = num1 * num2

q = f"what is {num1} {operations} {num2} ="
correct_an = eval(f"{num1} {operations} {num2}")
answer = float(input(q + ""))
if answer == correct_an:
    print("!!!CORRECT!!!")
    score += 10

else:
    print(f"Wrong..lol.. The correct answer is {correct_an}")

print(f"your final score is {score}/100")