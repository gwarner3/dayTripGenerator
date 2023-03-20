import random

DESTINATION_CATEGORY = 'destination'
RESTAURANT_CATEGORY = 'restaurant'
TRANSPORTATION_CATEGORY = 'transportation'
ENTERTAINMENT_CATEGORY = 'entertainment'

destinations = ["Sao Paulo, Brazil", "Accra, Ghana", "Negril, Jamaica", "San Juan, Costa Rica"]
restaurants = ["just natural", "mcdoanlds", "wendys", "sweet spot"]
transportation = ["Lyft", "Uber", "walking", "biking"]
entertainment = ["sightseeing", "kayaking", "sunbathing", "hiking"]

final_selections = {"restaurant": "", "destination": "", "transportation": "", "entertainment": ""}

def select_option(options, category):
    prompting_user = True
    while prompting_user:
        random_option = random.choice(options)
        selected_option = input(f'Is {category} {random_option} ok? y/n ').lower()
        if selected_option == 'y':
            prompting_user = False
            print(f'Great, {random_option} is a lovely {category}!\n')
            return random_option
        else:
            options.remove(random_option)
            if len(options) == 0:
                users_option = input(f'Uh-oh, we don\'t have another {category} for you to chose. Type your desired {category}: y')
                return users_option
            else:
                print(f'Ok, let\'s select a different {category}.\n')

def getOptions():
    final_selections["destination"] = select_option(destinations, DESTINATION_CATEGORY)
    final_selections["restaurant"] = select_option(restaurants, RESTAURANT_CATEGORY)
    final_selections["transportation"] = select_option(transportation, TRANSPORTATION_CATEGORY)
    final_selections["entertainment"] = select_option(entertainment, ENTERTAINMENT_CATEGORY)

# main program
print('Let\'s plan your day.')
selecting_options = True
while selecting_options:
    getOptions()
    selected_option = input(f'You selected {final_selections["destination"]}, {final_selections["restaurant"]}, {final_selections["transportation"]}, and {final_selections["entertainment"]}.\nAre these options ok? y/n ')
    if selected_option == 'y':
        print('Great, have fun!!!')
        selecting_options = False
    else:
        print('Let\'s try again.\n')