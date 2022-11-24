import random       # import random module to generate random numbers
import requests     # import requests module to get data from API
import time         # import time module to add a few seconds delay to display output
from datetime import datetime   # import datetime module to generate timestamp

# Required 1: function to generate a random number between 1 and 151 to use as the Pokemon ID number
def random_pokemon():
    pokemon_number = random.randint(1, 151)
    url = 'https://pokeapi.co/api/v2/pokemon/{}/'.format(pokemon_number)
    response = requests.get(url)
# Required 2: Using the Pokemon API get a Pokemon based on its ID number
    pokemon = response.json()
# Required 3: Create a dictionary that contains the returned Pokemon's name, id, height and weight
# Extended: Use different stats (base experience and number of moves) for the Pokemon from the API
    return {
        'name': pokemon['name'],
        'id': pokemon['id'],
        'height': pokemon['height'],
        'weight': pokemon['weight'],
        'base_experience': pokemon['base_experience'],
        'moves': len(pokemon['moves'])
    }

# Welcome to the game and tell the player the rules
def intro():
    print("Welcome to the wonderful Pokemon game!")
    time.sleep(2)
    print("Here are the rules")
    time.sleep(2)
    print("1. You are given a random Pokemon card with different stats")
    time.sleep(2)
    print("2. You select one of the card's stats")
    time.sleep(2)
    print("3. Another random Pokemon card is selected for me")
    time.sleep(2)
    print("4. The stats of the two cards are compared")
    time.sleep(2)
    print("5. The player with the stat higher than their opponent wins")
    time.sleep(2)

# Ask if player wants to play the game
def start_game():
    intro()
    start_play = input("Now would you like to play Pokemon game with me? y/n: ")
    if start_play.lower() == 'y' or start_play.lower() == 'yes':
        play()
    elif start_play.lower() == 'n' or start_play.lower() == 'no':
        print("That's a shame, you don't want any fun :(")
    else:
        print("I don't understand what you want to do.")

# play the game
def play():
    want_continue = 'y'
    player_total = 0
    computer_total = 0
    rounds = 0
    while want_continue.lower() == 'y' or want_continue.lower() == 'yes':
        # Required 4: Get a random Pokemon for the player and another for their opponent
        player_pokemon_1 = random_pokemon()
        player_pokemon_2 = random_pokemon()
        computer_pokemon = random_pokemon()
        print(f"^^^^^^^^^^^^^^^^^^^^ROUND {rounds + 1}^^^^^^^^^^^^^^^^^^^^")
        # Extended: Get multiple random Pokemon and let the player decide which one that they want to use
        print("----------Generating Your Pokemon 1...----------")
        time.sleep(2)
        print("Your Pokemon's ID is:                   " + str(player_pokemon_1['id']))
        print("Your Pokemon's name is:                 " + (player_pokemon_1['name']).capitalize())
        print("Your Pokemon's height is:               " + str(player_pokemon_1['height']))
        print("Your Pokemon's weight is:               " + str(player_pokemon_1['weight']))
        print("Your Pokemon's base experience is:      " + str(player_pokemon_1['base_experience']))
        print("Your Pokemon can make                   " + str(player_pokemon_1['moves']) + ' moves.')
        print("------------------------------------------------")
        print("----------Generating Your Pokemon 2...----------")
        time.sleep(2)
        print("Your Pokemon's ID is:                   " + str(player_pokemon_2['id']))
        print("Your Pokemon's name is:                 " + (player_pokemon_2['name']).capitalize())
        print("Your Pokemon's height is:               " + str(player_pokemon_2['height']))
        print("Your Pokemon's weight is:               " + str(player_pokemon_2['weight']))
        print("Your Pokemon's base experience is:      " + str(player_pokemon_2['base_experience']))
        print("Your Pokemon can make                   " + str(player_pokemon_2['moves']) + ' moves.')
        print("------------------------------------------------")
        which_pokemon = input("Which Pokemon whould you like to use? (type '1' for Pokemon 1, type '2' for Pokemon 2) ")
        if which_pokemon == '1':
            player_pokemon = player_pokemon_1
        elif which_pokemon == '2':
            player_pokemon = player_pokemon_2
        # Extended: Allow the opponent (computer) to choose a stat that they would like to compare.
        player_choose = input("Would you like to choose which stat to use? If 'y', you can choose. If 'n', I will choose. ")
        if player_choose.lower() == 'y' or player_choose.lower() == 'yes':
        # Required 5: Ask the user which stat they want to use (id, height or weight)
            which_stat = input(
                "Which stat would you like to use to compare with my Pokemon? \n Please type id/height/weight/base_experience/moves: ")
            player_stat = player_pokemon[which_stat]
            computer_stat = computer_pokemon[which_stat]
        elif player_choose.lower() == 'n' or player_choose == 'no':
            stat = {
                "id": computer_pokemon['id'],
                "height": computer_pokemon['height'],
                "weight": computer_pokemon['weight'],
                "base_experience": computer_pokemon['base_experience'],
                "moves": computer_pokemon['moves']
            }
            max_stat = [key for key in stat.keys() if stat[key] == max(stat.values())]
            which_stat = max_stat[0]
            player_stat = player_pokemon[which_stat]
            computer_stat = computer_pokemon[which_stat]
            print("I choose {} as the stat to compare with. ".format(which_stat))
        print("**********Generating My Pokemon...**********")
        time.sleep(2)
        print("*********************************************")
        # Required 6: Compare the player's and opponent's Pokemon on the chosen stat to decide who wins
        if player_stat > computer_stat:
            print("You won!")
            player_total += 1
        elif player_stat < computer_stat:
            print("Haha I won!")
            computer_total += 1
        else:
            print("It's a draw, no points to either")
        rounds += 1
        time.sleep(2)
        print("My Pokemon's ID is:                   " + str(computer_pokemon['id']))
        print("My Pokemon's name is:                 " + (computer_pokemon['name']).capitalize())
        print("My Pokemon's height is:               " + str(computer_pokemon['height']))
        print("My Pokemon's weight is:               " + str(computer_pokemon['weight']))
        print("My Pokemon's base experience is:      " + str(computer_pokemon['base_experience']))
        print("My Pokemon can make                   " + str(computer_pokemon['moves']) + ' moves.')
        print("*********************************************")
        print(f"Your Pokemon's {which_stat} is {player_pokemon[which_stat]}")
        print(f"My Pokemon's {which_stat} is {computer_pokemon[which_stat]}")
        print(f'Your score: {player_total} vs my score: {computer_total}')
        # Extended: Play multiple rounds and record the outcome of each round. The player with most number
        # of rounds won, wins the game
        want_continue = input("Would you like to continue playing? (y/n)")
    time.sleep(2)
    print("===============Final Result===============")
    time.sleep(2)
    print(f"We have played {rounds} rounds in total")
    time.sleep(2)
    if player_total > computer_total:
        print(f"Well done! Your final score is {player_total}, my final score is {computer_total}, you beat me!")
        print("==========================================")
    elif player_total > computer_total:
        print(f"Your final score is {player_total}, my final score is {computer_total}. I'm sorry but I'm clever than you.")
        print("==========================================")
    elif player_total == computer_total:
        print(f"Your final score is {player_total}, my final score is {computer_total}. It's a draw! I think we should play again.")
        print("==========================================")
    # Extended: Record scores for players and store them in a file
    with open('result_sheet.txt', 'a+') as result_sheet:
        current = datetime.now()
        curr_time = current.strftime("%d/%m/%Y %H:%M:%S")
        result_sheet.write(f"Time: {curr_time}\n")
        result_sheet.write(f"Total {rounds} rounds played, your final score is {player_total}, computer's final score is {computer_total}. \n\n")

start_game()
