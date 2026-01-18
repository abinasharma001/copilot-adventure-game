# Build a simple command-line "Choose Your Own Adventure" game.
# The player starts in a forest.
# Use input() for choices.
# Include at least 3 decision points and multiple endings.

def start_game():
    print("Welcome to the Choose Your Own Adventure game!")
    print("You find yourself in a dark forest. There are two paths ahead.")
    choice1 = input("Do you want to go left or right? (left/right): ").strip().lower()

    if choice1 == "left":
        print("You walk down the left path and encounter a wild river.")
        choice2 = input("Do you want to swim across or build a raft? (swim/raft): ").strip().lower()

        if choice2 == "swim":
            print("You bravely swim across the river but get swept away by the current.")
            print("Game Over: You were lost in the river.")
        elif choice2 == "raft":
            print("You build a sturdy raft and safely cross the river.")
            print("On the other side, you find a treasure chest!")
            print("Congratulations! You found the treasure and won the game!")
        else:
            print("Invalid choice. Game Over.")

    elif choice1 == "right":
        print("You walk down the right path and come across a sleeping dragon.")
        choice2 = input("Do you want to sneak past it or try to fight it? (sneak/fight): ").strip().lower()

        if choice2 == "sneak":
            print("You successfully sneak past the dragon and find a hidden cave filled with gold!")
            print("Congratulations! You found the treasure and won the game!")
        elif choice2 == "fight":
            print("You try to fight the dragon, but it wakes up and defeats you.")
            print("Game Over: The dragon was too strong.")
        else:
            print("Invalid choice. Game Over.")

    else:
        print("Invalid choice. Game Over.")


start_game()
