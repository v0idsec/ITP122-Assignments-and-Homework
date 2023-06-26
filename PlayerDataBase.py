# Creating an empty dictionary to store player names and scores
player_scores = {}

# Defining a function to validate player names
def validate_player(name):
    #Checking to see if name contains digits
    if any(char.isdigit() for char in name):
        return False
    return True

# Creating a function to validate the player score
def validate_score(score):
    # Check if the score is a number
    if not score.isdigit():
        return False
    # Check if the score is between 1-100
    if int(score) <0 or int(score) > 100:
        return False
    return True

# Creating the interface and actual program

# Placing the code block in a while loop allows us to detect any invalid inputs
while True:
    print("="*40)
    print("** Welcome to the Champions Soccer Club **")
    print("-"*40)
    print("Please choose an option from the following.")
    print("1) Add player name and score", "\n2) Display all the player information and scores","\n3) Quit")
    print("=" * 40)
    sel = input("Enter option: ")

    # Opt 1
    #Prompt user for player name and score
    if sel == "1":
        # Loop to allow user to add as many players as needed
        while True:
            name = input("Enter player name: ")
            # Validating player name
            if not validate_player(name):
                print("Invalid name, the name should only contain letters.")
                continue

            # Prompt user for score
            score = input("Enter player Score: ")
            # Validating score
            if not validate_score(score):
                print("Invalid score, score should only be a number between 1 and 100.")
                continue

            # Adding the player name and score to the dictionary
            player_scores[name] = int(score)
            print("Player added successfully.")

            # Asking user if another player needs to be added
            choice = input("Do you want to add another player? (Y/N): ")
            if choice.lower() == 'y':
                # Continue the loop if the user needs to add another player
                continue
            else:
                # Breaking out of loop if user is done adding players
                print("Exiting Player Addition")
                break

    # Option 2
    # Displaying all names and scores
    elif sel == '2':
        # If there are no players in dictionary, we need something to tell user that there are no players
        if len(player_scores) == 0:
            print("No players currently in database")
        else:
            print("="*20)
            print("Player Name\tScore")
            print("="*20)
            for name, score in player_scores.items():
                print(f"{name}\t\t{score}")

    # Option 3
    # Exiting the program
    elif sel == '3':
        print("*** Exiting Program... *** ")
        break

    #Catching invalid choices
    else:
        print("Invalid choice, please select option again.")
