import random

restaurants = ["just natural", "mcdoanlds", "wendys", "sweet spot"]
destinations = ["Sao Paulo, Brazil", "Accra, Ghana", "Negril, Jamaica", "San Juan, Costa Rica"]
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
            print(f'Ok, let\'s select a different {category}.\n')

def getOptions():
    final_selections["destination"] = select_option(destinations, 'destination')
    final_selections["restaurant"] = select_option(restaurants, 'restaurant')
    final_selections["transportation"] = select_option(transportation, 'transportation')
    final_selections["entertainment"] = select_option(entertainment, 'entertainment')

selecting_options = True
print('Let\'s plan your day.')
while selecting_options:
    getOptions()
    selected_option = input(f'You selected {final_selections["destination"]}, {final_selections["restaurant"]}, {final_selections["transportation"]}, and {final_selections["entertainment"]}.\nAre these options ok? y/n ')
    if selected_option == 'y':
        print('All done')
        selecting_options = False
    else:
        print('Let\'s try again.\n')
