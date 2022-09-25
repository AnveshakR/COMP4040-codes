# Write a Python program to simulate poker card shuffling to generate a random permutation of all 52 cards (excluding jokers).
# Then simulate four players to draw 11 cards for each player, where each plays takes turn to draw one card at each round
# following a fixed order of drawing (actually, this is equivalent to randomly selecting 9 cards for each player at a time provided
# that shuffling is truely random). The rest of the cards are discarded. These are the cards for playing one game. 
# Run your program until one player receives all 4 A's in his/her hand. How many games will have to be played for this to happen? 
# When this happens, it is considered as one success, Keep playing the games for 100 successes. 
# What is the average number of games to play to get all A's in one hand? 
# Repeat this experiment for 100 times. What can you conclude about the expected number of games to play for a success?

from random import choice
import itertools
import time

cards = [str(x) for x in range(2,11)]+['King', 'Queen', 'Jack', 'Ace']
types = ['Spades', 'Clubs', 'Hearts', 'Diamonds']

deck_test = list(itertools.product(cards,types)) # creating a deck of cards excluding joker

def middleSquare(max_num): # this function implements the middle square method of PRNG. It returns all the numbers 
                           # from 0 to max_num in a random order

    number = int(time.time() - time.time()%1) * time.time_ns() # the seed is chosen based on the system time
    range_num = []

    k = len(str(number))
    already_seen = set()

    while number not in already_seen:

        already_seen.add(number)
        l = k - k//2 
        r = k + k//2 + 1
        number = int(str(number * number).zfill(2*k)[l:r])  # zfill adds padding of zeroes in front
        if (number % pow(10, len(str(max_num))) < max_num):
            if number % pow(10, len(str(max_num))) not in range_num:
                range_num.append(number % pow(10, len(str(max_num)))) # adds number to final array if it is less than max_num
        
        if (len(range_num) == max_num):
            return range_num # if the array has the correct number of elements then it is returned


# the function below is to be uncommented if you want to use the middle square method of RNG in place of python's random.choice function
# WARNING: this method is extremely resource consuming and is VERY slow. I'd suggest running it only a few iterations.

# def swap_shuffler(deck):
#     rand_index = middleSquare(len(deck))
#     for i in range(len(deck)):
#         deck[i], deck[rand_index[i]] = deck[rand_index[i]], deck[i]
#     return deck


# comment out this function if you want to use the middle square method

def swap_shuffler(deck): # function to shuffle the deck of cards 
    for i in range(len(deck)):
        j = choice(range(len(deck)))
        deck[i], deck[j] = deck[j], deck[i]
    return deck


def remake(): # function to reset the cards of the 4 players

    deck = list(itertools.product(cards,types))
    deck = swap_shuffler(deck)
    players =  [[0 for j in range(11)] for i in range(4)]

    for i in range(11):
        for j in range(4):
            players[j][i] = (deck[j])
            deck.remove(deck[j])

    return players

avg_counter = 0
avg_games = []

while(avg_counter <= 100): # runs loop for avg_counter number of successes
    games_counter = 0
    break_counter = 0
    successes = 100
    while(break_counter < successes): # runs loop until 'successes' number of 4-ace hands are acheived
        player_cards = remake()
        games_counter+=1
        for player in player_cards:
            ace_counter = 0
            for card in [x[0] for x in player]: # checks the hand of every player, if any player has a 4-ace then it breaks the loop, 
                if card == 'Ace':               # else it resets the cards of the players
                    ace_counter+=1
            if(ace_counter == 4):
                # [print(x[0]+" of "+x[1]) for x in player] # prints the hand of the winning player
                break_counter+=1
                break
    print("Average number of games for 100 4-aces number {} =".format(avg_counter), games_counter/100)
    avg_games.append(games_counter/100)
    avg_counter +=1

print("Maximum average", max(avg_games))
print("Minimum average", min(avg_games))