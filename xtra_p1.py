"""
Optional bonus. See course site for details.

"""

import random

# Change the name below to a name of your choice

name = "Mr. Extra Creddy"

# Fix the code below to print the name using an f-string

print()
print(f"Hello, I'm {name}, your gamebot.")
print("Let's play an animal guessing game!")
print("There are 3 animals: wolf, eagle, snake (a Python of course).")
print("The wolf scares the eagle.")
print("The eagle grabs the snake.")
print("The snake bites the wolf.")
print("I'll pick one and you pick one and we'll see who wins.")
print()

# Right now, the user choses wolf everytime.
# Modify the code so the user is asked to
# enter wolf, eagle, or snake.
# Hint: use the input() function

user_choice = input("Choose 'wolf', 'eagle', or 'snake': ")

# Now the bot will pick one
buddy_choice = random.choice(["wolf", "eagle", "snake"])

# Report the choices
print()
print(f"You said {user_choice}.")
print(f"I said {buddy_choice}.")
print()

# Now we need to compare the choices and determine the winner
# Complete the logic to
# compare the choices and print who won
# In Python, indentation is important!
if user_choice == buddy_choice:
    print("We tied!")
elif user_choice == 'wolf' and buddy_choice == 'eagle':
    print("You win! Nice job.")
elif user_choice == 'wolf' and buddy_choice == 'snake':
    print("I win! Nice try.")
elif user_choice == 'eagle' and buddy_choice == 'wolf':
    print("I win! Nice try.")
elif user_choice == 'eagle' and buddy_choice == 'snake':
    print("You win! Nice job.")
elif user_choice == 'snake' and buddy_choice == 'wolf':
    print("You win! Nice job.")
elif user_choice == 'snake' and buddy_choice == 'eagle':
    print("I win! Nice try.")

# When you finish,
# right-click on the code and select "Format Document"

# Run the code, and play the game a few times.
# Copy the output from the terminal and paste it into the
# docstring comment below.
# --------------------------------------------------------------------

"""

Hello, I'm Mr. Extra Creddy, your gamebot.
Let's play an animal guessing game!
There are 3 animals: wolf, eagle, snake (a Python of course).
The wolf scares the eagle.
The eagle grabs the snake.
The snake bites the wolf.
I'll pick one and you pick one and we'll see who wins.

Choose 'wolf', 'eagle', or 'snake': wolf

You said wolf.
I said eagle.

You win! Nice job.

"""
