#Magic 8 Ball
import random

user_input = input(str("what is your question?: "))
responses = ["Ask Again Later", "Better Not Tell You Now","No","Outlook Good", "Outlook not so good", "Yes", "Signs point to Yes!", "Yes definitely", "You may rely on it."]

number = random.randint(0,9)

print(responses[number])
