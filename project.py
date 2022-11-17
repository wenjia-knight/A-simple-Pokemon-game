import random
import requests
import time

# Required 1: function to generate a random number between 1 and 151 to use as the Pokemon ID number
def random_pokemon():
    pokemon_number = random.randint(1, 151)
    url = 'https://pokeapi.co/api/v2/pokemon/{}/'.format(pokemon_number)
    response = requests.get(url)
# Required 2: Using the Pokemon API get a Pokemon based on its ID number
    pokemon = response.json()
# Extended: Use different stats (base experience and number of moves) for the Pokemon from the API
# Required 3: Create a dictionary that contains the returned Pokemon's name, id, height and weight
    return {
        'name': pokemon['name'],
        'id': pokemon['id'],
        'height': pokemon['height'],
        'weight': pokemon['weight'],
        'base_experience': pokemon['base_experience'],
        'moves': len(pokemon['moves'])
    }

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

def start_game():
    intro()
    start_play = input("Now would you like to play Pokemon game with me? y/n: ")
    if start_play == 'y':
        play()
    elif start_play == 'n':
        print("That's a shame, you don't want any fun :(")
    else:
        print("I don't understand what you want to do.")

def play():
    want_continue = 'y'
    player_total = 0
    computer_total = 0
    rounds = 1
    while want_continue == 'y':
# Required 4: Get a random Pokemon for the player and another for their opponent
        player_pokemon = random_pokemon()
        computer_pokemon = random_pokemon()
        print(f"^^^^^^^^^^^^^^^ROUND {rounds}^^^^^^^^^^^^^^^")
        print("----------Generating Your Pokemon...----------")
        time.sleep(2)
        print("Your Pokemon's ID is: " + str(player_pokemon['id']))
        print("Your Pokemon's name is: " + (player_pokemon['name']).capitalize())
        print("Your Pokemon's height is: " + str(player_pokemon['height']))
        print("Your Pokemon's weight is: " + str(player_pokemon['weight']))
        print("Your Pokemon's base experience is: " + str(player_pokemon['base_experience']))
        print("Your Pokemon can make " + str(player_pokemon['moves']) + ' moves.')
        print("----------------------------------------------")
# Required 5: Ask the user which stat they want to use (id, height or weight)
        which_stat = input(
            "Which stat would you like to use to compare with my Pokemon? \n Please type id/height/weight/base_experience/moves: ")
        player_stat = player_pokemon[which_stat]
        computer_stat = computer_pokemon[which_stat]
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
        print("My Pokemon's ID is: " + str(computer_pokemon['id']))
        print("My Pokemon's name is: " + (computer_pokemon['name']).capitalize())
        print("My Pokemon's height is: " + str(computer_pokemon['height']))
        print("My Pokemon's weight is: " + str(computer_pokemon['weight']))
        print("My Pokemon's base experience is: " + str(computer_pokemon['base_experience']))
        print("My Pokemon can make " + str(computer_pokemon['moves']) + ' moves.')
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
    print(f"We have played {rounds - 1} rounds in total")
    time.sleep(2)
    if player_total > computer_total:
        print(f"Well done! Your final score is {player_total}, my final score is {computer_total}, you beat me!")
    elif player_total > computer_total:
        print(f"Your final score is {player_total}, my final score is {computer_total}. I'm sorry but I'm clever than you.")
    elif player_total == computer_total:
        print(f"Your final score is {player_total}, my final score is {computer_total}. It's a draw! I think we should play again.")

start_game()