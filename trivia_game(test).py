import json
import requests
 #Import the time library
import time

# Calculate the start time
start = time.time()

# Code here

# Calculate the end time and time taken
end = time.time()
length = end - start

# Show the results : this can be altered however you like
print("It took", length, "seconds!")
API_URL = "https://opentdb.com/api.php?amount=10&category=11&difficulty=medium&type=boolean"

response = requests.get(API_URL)
data = json.loads(response.text)    

questions = data["resultats"]

correct_answers = 0
for question in questions:
    print(question["question"])
    print("Options:")
    for i in range(len(question["reponse_incorrect"])):
        print(f"{i+1}. {question['reponse_incorrect'][i]}")
    print(f"{len(question['reponse_incorrect'])+1}. {question['correct_answer']}")
    user_answer = int(input("Enter the number of your answer: "))
    if user_answer == len(question["reponse_incorrect"]) + 1:
        print("Correct!")
        correct_answers += 1
    else:
        print("Incorrect.")

print(f"Vous avez {correct_answers} out of {len(questions)} questions correct.")

