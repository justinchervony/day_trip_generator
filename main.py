import random
import sys


destination_list = ["Ireland", "New York", "Miami", "Aspen"]
restaurant_list = [["tavern", "steakhouse", "cafe"], ["seafood restaurant", "pizza shop", "diner"], ["steakhouse", "cuban restaurant", "hibachi restaurant"], ["soup and sandwich shop", "vegan restaurant", "bar and grill"]]
transportation_list = ["rental car", "train", "bike"]
entertainment_list = [["tour of the Guinness Factory", "drink an Irishman under the table", "explore an old castle"], ["visit Time Square", "go to the museums", "walk through Central Park"], ["go to the beach", "walk on miracle mile", "hit the clubs"], ["go hiking", "go skiing", "go fishing"]]
destination_list_length = len(destination_list) - 1

destination_selected = random.randint(0, destination_list_length)
restaurant_selected = random.randint(0, len(restaurant_list[destination_selected])-1)
transportation_selected = random.randint(0, 2)
entertainment_list = random.randint(0, len(entertainment_list[destination_selected])-1)

user_trip_confirmation = False

print("Welcome to the Day Trip Generator! Let's get started...")

while user_trip_confirmation == False :
    user_valid_response = False
    while user_valid_response == False:
        destination_confirmation_str = input(f"For a destination, how about {destination_list[destination_selected]}? y/n ")
        current_destination = destination_list[destination_selected]
        if  destination_confirmation_str == "y":
            user_valid_response = True
            break
        elif destination_confirmation_str == "n" and len(destination_list) == 1:
            print("I have no more options to give you. Please restart and try again.")
            sys.exit()
        elif destination_confirmation_str == "n":
            destination_list.remove(current_destination)
            destination_selected = random.randint(0, len(destination_list) - 1)
            print("Sorry that doesn't work for you. Let me try again...")
        else:
            print("Hmm...that didn't seem like a valid response. Please type 'y' or 'n'.")


    if destination_list[destination_selected] == "Ireland":
        destination_selected = 0
    elif destination_list[destination_selected] == "New York":
        destination_selected = 1
    elif destination_list[destination_selected] == "Miami":
        destination_selected = 2
    else:
        destination_selected = 3
    print("Great! Let's continue...")

    user_valid_response = False
    while user_valid_response == False:
        transportation_confirmation_str = input(f"For transportation, how about a {transportation_list[transportation_selected]}? y/n ")
        current_transportation = transportation_list[transportation_selected]
        if  transportation_confirmation_str == "y":
            user_valid_response = True
            break
        elif transportation_confirmation_str == "n" and len(transportation_list) == 1:
            print("I have no more options to give you. Please restart and try again.")
            sys.exit()
        elif transportation_confirmation_str == "n":
            transportation_list.remove(current_restaurant)
            transportation_selected = random.randint(0, len(transportation_list) - 1)
            print("Sorry that doesn't work for you. Let me try again...")
        else:
            print("Hmm...that didn't seem like a valid response. Please type 'y' or 'n'.")

    print("Gotta go fast! Let's continue...")

    user_valid_response = False
    while user_valid_response == False:
        restaurant_confirmation_str = input(f"For your dining, how about a {restaurant_list[restaurant_selected]}? y/n ")
        current_restaurant = restaurant_list[restaurant_selected]
        if  restaurant_confirmation_str == "y":
            user_valid_response = True
            break
        elif restaurant_confirmation_str == "n" and len(restaurant_list) == 1:
            print("I have no more options to give you. Please restart and try again.")
            sys.exit()
        elif restaurant_confirmation_str == "n":
            restaurant_list.remove(current_restaurant)
            restaurant_selected = random.randint(0, len(restaurant_list) - 1)
            print("Sorry that doesn't work for you. Let me try again...")
        else:
            print("Hmm...that didn't seem like a valid response. Please type 'y' or 'n'.")


    #offer entertainment option loop
    #if user confirms rng entertainment, proceed, else remove option from list and randomly generate another
    #if list length < 1, break the program

    #display trip selected options. If confirmed, proceed to next. Else go back to the beginning.

#display full trip. End.