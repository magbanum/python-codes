# Let's Create Snake and Ladder of 20 blocks

# Import random module for dice
import random
# Position of snakes and their value
snakes = {5 : 2, 7 : 1, 11 : 5, 15: 3, 18: 9}
# Position after getting snake [3, 6, 6, 12, 9]
# Position of Ladders and their values
ladder = {4: 5, 8:4, 13: 3}
# Position after getting ladder [9, 12, 16]

# Enter names of Players
Player1 = input("Player 1: Enter your name -> ")
Player2 = input("Player 2: Enter your name -> ")
print()
# Players start at Zero
Player1_pos = 0
Player2_pos = 0

# Lambda function to get random dice value
dice = lambda : random.choice(range(1,7))

# Function for Snake/Ladder operation
def snakeorladder(Player, Player_name):
    # Keyboard interactive to make it manual dice rolling
    input("{} it's your turn to roll the dice.".format(Player_name))
    # Rolled the dice
    dice_rolled = dice()
    

    # If position of player is less than 20 after dice rolled then add dice value to previous position.
    if (Player + dice_rolled < 20):
        Player += dice_rolled
        if dice_rolled == 6:
            print("🎲 You hit the {} on dice roll.🔥".format(dice_rolled))
        else:
            print("🎲 You got {} on dice roll.".format(dice_rolled))
    # If Position of player is 20 after dice rolled then return "Winner" to print results.
    elif (Player + dice_rolled == 20):
        print("🎲 You got {} on dice roll. And you've reached the destination.".format(dice_rolled))
        return "Winner"
    # Position of Player can not be greater than 20. Hence do not add dice value to player position.
    else:
        print("🎲 You got {} but can't go beyond 20. You are still at {}".format(dice_rolled, Player))
        print()
        return Player

    # If there is snake on the player position then decrease the position by snake value.
    if Player in snakes.keys():
        Player -= snakes[Player]
        print("⬇ Oops! there was a 🐍. You are down to {}".format(Player))
        print()
    # If there is ladder on the player position then increase the position by ladder value.
    elif Player in ladder.keys():
        Player += ladder[Player]
        print("⬆ Hurray! it's a Ladder and you just jumped to {}".format(Player))
        print()
    # If there is no ladder or snake then just return the current player position.
    else:
        print("⬆ You just moved to {}".format(Player))
        print()
    # return final player position after dice roll.
    return Player

# while loop to repeat turn until any player reaches the final destination
while(1):
    # Player 1's turn
    Player1_pos = snakeorladder(Player1_pos, Player1)
    # If function returns "Winner" that means Player1 reached the destination
    if Player1_pos == "Winner":
        print()
        print("✨✨✨ Congratulations! {} is the Winner.✨✨✨ ".format(Player1))
        break
    # Player 2's turn
    Player2_pos = snakeorladder(Player2_pos, Player2)
    # If function returns "Winner" that means Player2 reached the destination
    if Player2_pos == "Winner":
        print()
        print("✨✨✨ Congratulations! {} is the Winner. ✨✨✨".format(Player2))
        break
# Play one more game