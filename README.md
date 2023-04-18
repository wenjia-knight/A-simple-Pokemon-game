# A-simple-Pokemon-game
### In this project, I created a small Pokemon game where two players (the user and the computer) compare stats, similar to the Top Trumps card game. The basic flow of the games is:
1. You are given a random card with different stats
2. You select one of the card's stats
3. Another random card is selected for the computer
4. The stats of the two cards are compared
5. The player with the stat higher than their opponent wins

### This project used the Pokemon API to extract data on the randomly generated Pokemon. This project contained all the required tasks: 
1. Generate a random number between 1 and 151 to use as the Pokemon ID number
2. Using the Pokemon API get a Pokemon based on its ID number
3. Create a dictionary that contains the returned Pokemon's name, id, height and weight
4. Get a random Pokemon for the player and another for their opponent
5. Ask the user which stat they want to use (id, height or weight)
6. Compare the player's and opponent's Pokemon on the chosen stat to decide who wins

### It also contained all the extended ideas beyond the project. The additional features are:  
- Use different stats for the Pokemon from the API  
- Get multiple random Pokemon and let the player decide which one that they want to use
- Play multiple rounds and record the outcome of each round. The player with most number of rounds won, wins the game
- Allow the opponent (computer) to choose a stat that they would like to compare
- Record high scores for players and store them in a file
