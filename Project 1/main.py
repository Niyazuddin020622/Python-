import random

# Computer randomly selects -1 (Water), 0 (Gun), or 1 (Snake)
computer = random.choice([-1, 0, 1])

# Player input
youstr = input("Enter your choice (s for Snake, w for Water, g for Gun): ").lower()

# Dictionaries for mapping choices
youDict = {"s": 1, "w": -1, "g": 0}
reverseDict = {1: "Snake", -1: "Water", 0: "Gun"}

# Check if the input is valid
if youstr not in youDict:
    print("Invalid choice! Please select s, w, or g.")
else:
    # Map the player's input to the corresponding value
    you = youDict[youstr]

    # Display choices
    print(f"You chose {reverseDict[you]}\nComputer chose {reverseDict[computer]}")

    # Determine the result
    if computer == you:
        print("It's a Draw!")
    elif (computer == -1 and you == 1) or (computer == 0 and you == -1) or (computer == 1 and you == 0):
        print("You Win!")
    else:
        print("You Lose!")
