#!/usr/bin/env python3
import random, yaml

with open("quizzes/questions.yaml") as f:
    questions = yaml.safe_load(f)

random.shuffle(questions)

for q in questions:
    print("\nQ:", q["q"])
    if q["type"] == "mc":
        for i, choice in enumerate(q["choices"]):
            print(f"  {i}) {choice}")
        ans = input("Your answer: ")
        print("✔ Correct!" if int(ans) == q["answer"] else f"✘ Wrong. Correct: {q['choices'][q['answer']]}")
    else:  # short answer
        ans = input("Your answer: ")
        if ans.lower() in [a.lower() for a in q["answer"]]:
            print("✔ Correct!")
        else:
            print(f"✘ Wrong. Example answers: {q['answer']}")
    print("Why:", q["why"])
