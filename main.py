import random
import sys


destination_list = ["Ireland", "New York", "Miami", "Aspen"]
restaurant_list = [["tavern", "steakhouse", "cafe"], ["seafood restaurant", "pizza shop", "diner"], ["steakhouse", "cuban restaurant", "hibachi restaurant"], ["soup and sandwich shop", "vegan restaurant", "bar and grill"]]
transportation_list = ["rental car", "train", "bike"]
entertainment_list = [["tour the Guinness Factory", "drink an Irishman under the table", "explore an old castle"], ["visit Time Square", "go to the museums", "walk through Central Park"], ["go to the beach", "walk on miracle mile", "hit the clubs"], ["go hiking", "go skiing", "go fishing"]]
destination_list_length = len(destination_list) - 1 #Number of destinations, adjusting for list number system

#initiating all "selected" parameters
destination_selected = random.randint(0, destination_list_length)
restaurant_selected = random.randint(0, len(restaurant_list[destination_selected])-1)
transportation_selected = random.randint(0, 2)
entertainment_selected = random.randint(0, len(entertainment_list[destination_selected])-1)

#setting user confirmation to False so the generator will reset on user rejection of trip.
user_trip_confirmation = False

print("Welcome to the Day Trip Generator! Let's get started...")

while user_trip_confirmation == False :
    user_valid_response = False
    while user_valid_response == False:
        destination_confirmation_str = input(f"For a destination, how about {destination_list[destination_selected]}? y/n ")
        current_destination = destination_list[destination_selected]
        if  destination_confirmation_str == "y":
            user_destination_final = current_destination
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

    #Resets destination_selected to the original list value so other comparisons still work.
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
            user_transportation_final = current_transportation
            user_valid_response = True
            break
        elif transportation_confirmation_str == "n" and len(transportation_list) == 1:
            print("I have no more options to give you. Please restart and try again.")
            sys.exit()
        elif transportation_confirmation_str == "n":
            transportation_list.remove(current_transportation)
            transportation_selected = random.randint(0, len(transportation_list) - 1)
            print("Sorry that doesn't work for you. Let me try again...")
        else:
            print("Hmm...that didn't seem like a valid response. Please type 'y' or 'n'.")

    print("Gotta go fast! Let's continue...")

    user_valid_response = False
    restaurant_selected = random.randint(0, len(restaurant_list[destination_selected]) -1)
    restaurant_list_selected = restaurant_list[destination_selected]
    while user_valid_response == False:
        restaurant_confirmation_str = input(f"For your dining, how about a {restaurant_list_selected[restaurant_selected]}? y/n ")
        current_restaurant = restaurant_list_selected[restaurant_selected]
        if  restaurant_confirmation_str == "y":
            user_restaurant_final = current_restaurant
            user_valid_response = True
            break
        elif restaurant_confirmation_str == "n" and len(restaurant_list_selected) == 1:
            print("I have no more options to give you. Please restart and try again.")
            sys.exit()
        elif restaurant_confirmation_str == "n":
            restaurant_list_selected.remove(current_restaurant)
            restaurant_selected = random.randint(0, len(restaurant_list_selected) - 1)
            print("Sorry that doesn't work for you. Let me try again...")
        else:
            print("Hmm...that didn't seem like a valid response. Please type 'y' or 'n'.")

    print("Delicious! Let's continue...")

    user_valid_response = False
    entertainment_selected = random.randint(0, len(entertainment_list[destination_selected]) -1)
    entertainment_list_selected = entertainment_list[destination_selected]    
    while user_valid_response == False:
        entertainment_confirmation_str = input(f"For fun, how would you like to {entertainment_list_selected[entertainment_selected]}? y/n ")
        current_entertainment = entertainment_list_selected[entertainment_selected]
        if  entertainment_confirmation_str == "y":
            user_entertainment_final = current_entertainment
            user_valid_response = True
            break
        elif entertainment_confirmation_str == "n" and len(entertainment_list_selected) == 1:
            print("I have no more options to give you. Please restart and try again.")
            sys.exit()
        elif entertainment_confirmation_str == "n":
            entertainment_list_selected.remove(current_entertainment)
            entertainment_selected = random.randint(0, len(entertainment_list_selected) - 1)
            print("Sorry that doesn't work for you. Let me try again...")
        else:
            print("Hmm...that didn't seem like a valid response. Please type 'y' or 'n'.")

    print("That sounds like a great way to spend your time!")
    print("")
    print(f"So your destination is {user_destination_final}, your transportation is a {user_transportation_final}, you picked to eat at a {user_restaurant_final}, and you chose to {user_entertainment_final}.")
    user_valid_response = False
   
    while user_valid_response == False:
        user_finalize_trip = input("Do you want to finalize this trip? y/n ")
        if user_finalize_trip == "y":
            user_valid_response = True
            user_trip_confirmation = True
        elif user_finalize_trip =="n":
            print("Let's go back and remake this trip then!")
            destination_list = ["Ireland", "New York", "Miami", "Aspen"]
            restaurant_list = [["tavern", "steakhouse", "cafe"], ["seafood restaurant", "pizza shop", "diner"], ["steakhouse", "cuban restaurant", "hibachi restaurant"], ["soup and sandwich shop", "vegan restaurant", "bar and grill"]]
            transportation_list = ["rental car", "train", "bike"]
            entertainment_list = [["tour the Guinness Factory", "drink an Irishman under the table", "explore an old castle"], ["visit Time Square", "go to the museums", "walk through Central Park"], ["go to the beach", "walk on miracle mile", "hit the clubs"], ["go hiking", "go skiing", "go fishing"]]
            destination_list_length = len(destination_list) - 1
            break
        else:
            print("Hmm...that didn't seem like a valid response. Please type 'y' or 'n'.")


print(f"For your trip, you will take a {user_transportation_final} and go to {user_destination_final}. You'll spend your time eating at {user_restaurant_final} and you will {user_entertainment_final}. Hope you enjoy!")