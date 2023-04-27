# State the number of available of tickets
tickets = 199


# Loop through first 200 users
for user_num in range(1, 201):
    # Check if there are any tickets remaining
    if tickets > 0:
        # printing welcome message and available tickets
        print(f"Welcome to Movies4Us! You are the {user_num}th user. The number of remaining tickets is now {tickets}.")
        # Decrease number of tickets
        tickets -= 1

        if tickets == 0:
            print("Welcome to Movies4Us! You are the 200th User. The number of remaining tickets is now 0.")

    else:
        # if there are no more tickets, print a message and finish loop
        print("Sorry, there are no more tickets available.")
        break

# If we get to this point, it means the loop has completed without using break statement
# So we can print a message indicating all tickets have been sold

if tickets == 0:
    print("All tickets have been sold.")
