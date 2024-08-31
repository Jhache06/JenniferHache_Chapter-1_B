# Import the random to generate random numbers and select random items.
import random

# Ask user to ask a yes or no question and give user option to quit game.
# Create a loop that will continue.
# If the answer to question is empty or says 'quit', loop will stop.
while True:
    question = input("Ask yes or no question. If you want to quit game, type 'quit': ")

# Use if statement to verify if user typed an answer of 'quit' or left empty.
    if question == "quit":

# Use print to let user know that they chose to quit the game.
        print("Game over!")

# Break will exit/terminate the loop.
        break

# Create loop that will generate a random number between 1 and 12.
    for i in range(random.randrange(0, 13)):

# break out of the loop after one iteration
        break

# Use print to generate answer from the txt file.
# Open file and have it read its contents from list.
    response = random.choice(open("8ball_responses.txt", "r").read().splitlines())
    print("8-Ball Answer is: "+ response)




