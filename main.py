import random


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
            user_trip_confirmation = True
            break
        elif destination_confirmation_str == "n":
            destination_list.remove(current_destination)
            destination_selected = random.randint(0, len(destination_list) - 1)
            print("Sorry that doesn't work for you. Let me try again...")
        else:
            print("Hmm...that didn't seem like a valid response. Please type 'y' or 'n'.")
    #offer restaurant option loop
    #if user confirms rng restaurant, proceed, else remove option from list and randomly generate another
    #if list length < 1, break the program

    #offer transportation option loop
    #if user confirms rng transportation, proceed, else remove option from list and randomly generate another
    #if list length < 1, break the program

    #offer entertainment option loop
    #if user confirms rng entertainment, proceed, else remove option from list and randomly generate another
    #if list length < 1, break the program

    #display trip selected options. If confirmed, proceed to next. Else go back to the beginning.

#display full trip. End.