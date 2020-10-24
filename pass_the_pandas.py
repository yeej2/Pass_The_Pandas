import random as r
import time
import msvcrt as m
from art import *

dict={1:"Blank", 2:"Bamboo", 3:"Water", 4:"Blank", 5:"Panda", 6:"Blank"}

class Player :

    # The age and gender parameters has a default value.
    def __init__ (self, name, dice_count):

        self.name = name
        self.dice = dice_count

    def showInfo(self):
        print ("Name: ", self.name)
        print ("Dice: ", self.dice)

def wait():
    m.getch()

def rules():
    print("\nScroll down for the rules. Press any key to \n")
    print("""\
             ______________________________________________________________________________________________
            |Object of the Game:                                                                           |
            |Try to be the first player to get rid of all of your dice.                                    |
            |______________________________________________________________________________________________|
            |                                                                                              |
            |Set Up:                                                                                       |
            |Each player starts with four to six dice, depending on the number of players:                 |
            |         _______________                                                                      |
            |Players:| 2 | 3 | 4 | 5 |                                                                     |
            |         ----------------                                                                     |
            |Dice:   | 6 | 6 | 5 | 4 |                                                                     |
            |______________________________________________________________________________________________|
            |                                                                                              |
            |About the Dice:                                                                               |
            |Each of the dice in the game contains six sides. Of these six sides, three show images (one   |
            |Panda, one Bamboo, and one Water Drop), and the other three are blank. Each image on the      |
            |die corresponds to an action taken by the player who rolled it. See Game Play for details on  |
            |each of these actions.                                                                        |
            |                                                                                              |
            |______________________________________________________________________________________________|
            |                                                                                              |
            |Game Play:                                                                                    |
            |Players take turns rolling the dice. Each turn should follow the order of operations listed   |
            |below, in sequential order:                                                                   |
            |                                                                                              |
            |1. Roll all of your dice.                                                                     |
            |                                                                                              |
            |2. Remove any Water Drops you rolled from the game. Since water evaporates, all Water         |
            | Drops rolled are immediately removed from the game and placed off to the side or in the box. |
            |                                                                                              |
            |3. Pass any Pandas you rolled to other players. Players who roll a Panda give that die to     |
            | any other player of their choice. If multiple Pandas are rolled, those dice can all be given |
            | to the same player, or split amongst multiple players in any manner.                         |
            |                                                                                              |
            |4. Set aside Bamboo for the Bamboo Challenge. Compare the number of Bamboo you rolled         |
            | with the previous player. If they have more bamboo than you, they must pass you the          |
            | difference (see Bamboo Challenge, below).                                                    |
            |                                                                                              |
            |5. Keep all Blank dice. When a player rolls a blank, no action is taken for that die.         |
            |Note: Remember that on every turn, players re-roll all of their dice. Play continues until    |
            |one player no longer has dice at the end of their turn or the end of another player’s turn.   |
            |                                                                                              |
            |______________________________________________________________________________________________|
            |                                                                                              |
            |Ending the Game:                                                                              |
            |The game is over if any player has no dice left at either the end of their own turn, or at the|
            |end of another player’s turn (because they have given the last of their bamboo away on another|
            |player’s turn). Players may choose to play for second, third, and fourth places.              |
            |                                                                                              |
            |______________________________________________________________________________________________|
            |                                                                                              |
            |Bamboo Challenge:                                                                             |
            |Each player must roll at least the same number of Bamboo as the previous player. If a player  |
            |does not meet this challenge, then the previous player will give that player the difference.  |
            |A turn is not over until the Bamboo Challenge is settled.                                     |
            |                                                                                              |
            |______________________________________________________________________________________________|

    """)
    print("\nPress any key to continue ...\n")
    wait()


def game_setup():
    player_count = int(input("How many players do you have?\n"))

    if player_count == 5:
        dice_count = 4

        player1 = input("Please input player 1 name\n")
        player1 = Player(player1,dice_count)
        player2 = input("Please input player 2 name\n")
        player2 = Player(player2,dice_count)
        player3 = input("Please input player 3 name\n")
        player3 = Player(player3,dice_count)
        player4 = input("Please input player 4 name\n")
        player4 = Player(player4,dice_count)
        player5 = input("Please input player 5 name\n")
        player5 = Player(player5,dice_count)

    elif player_count == 4:
        dice_count = 5
        player1 = input("Please input player 1 name\n")
        player1 = Player(player1,dice_count)
        player2 = input("Please input player 2 name\n")
        player2 = Player(player2,dice_count)
        player3 = input("Please input player 3 name\n")
        player3 = Player(player3,dice_count)
        player4 = input("Please input player 4 name\n")
        player4 = Player(player4,dice_count)
        player5 = Player('null', 1)

    elif player_count == 3:
        dice_count = 6
        player1 = input("Please input player 1 name\n")
        player1 = Player(player1,dice_count)
        player2 = input("Please input player 2 name\n")
        player2 = Player(player2,dice_count)
        player3 = input("Please input player 3 name\n")
        player3 = Player(player3,dice_count)
        player4 = Player('null', 1)
        player5 = Player('null', 1)

    elif player_count == 2:
        dice_count = 6
        player1 = input("Please input player 1 name\n")
        player1 = Player(player1,dice_count)
        player2 = input("Please input player 2 name\n")
        player2 = Player(player2,dice_count)
        player3 = Player('null', 1)
        player4 = Player('null', 1)
        player5 = Player('null', 1)

    elif player_count > 5:
        print("Too many players")
    else:
        print("Too few players")

    players = [player1, player2, player3, player4, player5]
    return(player_count, dice_count, player1, player2, player3, player4, player5, players)

    # print(r.randint(1,4))

def game_end_logic(active_players):
    for player in active_players:
        if player.dice <= 0:
            winner = player.name
            game_end = True
            return winner, game_end
        else:
            winner = "Nobody"
            game_end = False
    return winner, game_end

def dice_logic(player_count, dice_count, player1, player2, player3, player4, player5, players):

    turn = 0
    bamboo_round = 0
    bamboo_on = False
    carryover = 0
    old_bamboo=0
    active_players = players[:player_count]
    game_end = False

    while game_end == False:
        water = 0

        if turn >= len(active_players):
            turn = 0
            # print("RESET")
        if turn == 0:
            player_turn = player1
        elif turn == 1:
            player_turn = player2
        elif turn == 2:
            player_turn = player3
        elif turn == 3:
            player_turn = player4
        elif turn == 4:
            player_turn = player5

        dice_values = []
        dice_temp = []
        x=0

        if old_bamboo > 0:
            print(player_turn.name, ", you need to roll", old_bamboo, "bamboo to avoid gaining dice!")
        print("\n\n{0} ROLL THE DICE!!!!\n".format(player_turn.name.upper()))
        wait()
        while x < player_turn.dice:
            # if player_turn.name.lower() == "joshua":
            #     dice_values.append(r.randint(5,5))
            # else:
            dice_values.append(r.randint(1,6))
            x+=1
        for values in dice_values:
            dice_temp.append(dict[values])

        for die in dice_temp:
            print(die)
            if die == 'Water':
                water+=1
            time.sleep(.5)

        if water > 0:
            print("\nWater was evaporated\n")
        dice=[i for i in dice_temp if i != 'Water']
        player_turn.dice = len(dice)
        # winner, game_end = game_end_logic(active_players)


        for die in dice:
            if die == "Panda":
                for person in active_players:
                    print("[",person.name, "has", person.dice, "dice]")

                pass_pandas = input("\n{0}, Who would you like to pass your panda to?\n".format(player_turn.name))
                print()

                if pass_pandas.lower()=='null':
                    print("Whoops, I don't have error handling, guess you lose your turn :(")

                elif pass_pandas.lower() == player1.name.lower():
                    player1.dice+=1
                    player_turn.dice-=1
                    print(player1.name, "now has", player1.dice, "dice.")
                    print(player_turn.name, "now has", player_turn.dice, "dice.\n")

                elif pass_pandas.lower() == player2.name.lower():
                    player2.dice+=1
                    player_turn.dice-=1
                    print(player2.name, "now has", player2.dice, "dice.")
                    print(player_turn.name, "now has", player_turn.dice, "dice.\n")

                elif pass_pandas.lower() == player3.name.lower():
                    player3.dice+=1
                    player_turn.dice-=1
                    print(player3.name, "now has", player3.dice, "dice.")
                    print(player_turn.name, "now has", player_turn.dice, "dice.")

                elif pass_pandas.lower() == player4.name.lower():
                    player4.dice+=1
                    player_turn.dice-=1
                    print(player4.name, "now has", player4.dice, "dice.")
                    print(player_turn.name, "now has", player_turn.dice, "dice.")

                elif pass_pandas.lower() == player5.name.lower():
                    player5.dice+=1
                    player_turn.dice-=1
                    print(player5.name, "now has", player5.dice, "dice.")
                    print(player_turn.name, "now has", player_turn.dice, "dice.")
                # winner, game_end = game_end_logic(active_players)
        # player = input('Please choose player to give panda to\n')

        if bamboo_on == False:
            old_bamboo = dice.count("Bamboo")
        else:
            new_bamboo = dice.count("Bamboo")

        if bamboo_on is True:
            if old_bamboo > 0 or new_bamboo > 0:
                # print("BAMBOO PHASE")
                carryover = bamboo_logic(old_bamboo, new_bamboo, player_turn, players, turn, player_count)
            if carryover == None:
                old_bamboo = 0
            else:
                old_bamboo = carryover

        bamboo_on=True
        # bamboo_round+=1
        winner = winner, game_end = game_end_logic(active_players)


        # print("\n",player_turn.name,"now has", player_turn.dice, "dice\n")
        turn +=1
    congrats()
    winning_name(winner)
    # print("\n *********** ", winner.upper(), " IS THE WINNER **************")
        # print(dice)
    # for die in dice:
    #     print(die)
    #     time.sleep(.4)

def congrats():
    print("""\
    _______      ,-----.    ,---.   .--.  .-_'''-.   .-------.       ____   ,---------.   .-'''-.
   /   __  \   .'  .-,  '.  |    \  |  | '_( )_   \  |  _ _   \    .'  __ `.\          \ / _     \\
  | ,_/  \__) / ,-.|  \ _ \ |  ,  \ |  ||(_ o _)|  ' | ( ' )  |   /   '  \  \`--.  ,---'(`' )/`--'
,-./  )      ;  \  '_ /  | :|  |\_ \|  |. (_,_)/___| |(_ o _) /   |___|  /  |   |   \  (_ o _).
\  '_ '`)    |  _`,/ \ _/  ||  _( )_\  ||  |  .-----.| (_,_).' __    _.-`   |   :_ _:   (_,_). '.
 > (_)  )  __: (  '\_/ \   ;| (_ o _)  |'  \  '-   .'|  |\ \  |  |.'   _    |   (_I_)  .---.  \  :
(  .  .-'_/  )\ `"/  \  ) / |  (_,_)\  | \  `-'`   | |  | \ `'   /|  _( )_  |  (_(=)_) \    `-'  |
 `-'`-'     /  '. \_/``".'  |  |    |  |  \        / |  |  \    / \ (_ o _) /   (_I_)   \       /
   `._____.'     '-----'    '--'    '--'   `'-...-'  ''-'   `'-'   '.(_,_).'    '---'    `-...-'

    """)

def winning_name(winner):
    winner_final = winner.upper() + " YOU WIN"
    tprint(winner_final, 'fantasy')

def bamboo_logic(old_bamboo, new_bamboo,player_turn, players, turn, player_count):
    # players=[i for i in players.name if i != 'null']
    # if turn == 0:
    active_players = players[:player_count]
    prev_player = active_players[turn-1]

    if old_bamboo > new_bamboo:
        over = (old_bamboo - new_bamboo)
        player_turn.dice += over
        prev_player.dice -= over
        print("{0} lost {1} dice. from the bamboo".format(prev_player.name, over))
        print("{0} gained {1} dice. from the bamboo\n".format(player_turn.name, over))
        time.sleep(1)
        pass

    elif old_bamboo < new_bamboo:
        carryover = (new_bamboo - old_bamboo)
        # print(prev_player.name," did not pass any bamboo to ", player_turn.name)
        # print(carryover)
        return carryover

    elif old_bamboo == new_bamboo:
        print(player_turn.name, "had the same amount of bamboo as", prev_player.name)
        time.sleep(1)
        pass

def welcome():
    print("""\
.--.      .--.    .-''-.    .---.        _______      ,-----.    ,---.    ,---.    .-''-.          ,---------.    ,-----.
|  |_     |  |  .'_ _   \   | ,_|       /   __  \   .'  .-,  '.  |    \  /    |  .'_ _   \         \          \ .'  .-,  '.
| _( )_   |  | / ( ` )   ',-./  )      | ,_/  \__) / ,-.|  \ _ \ |  ,  \/  ,  | / ( ` )   '         `--.  ,---'/ ,-.|  \ _ \\
|(_ o _)  |  |. (_ o _)  |\  '_ '`)  ,-./  )      ;  \  '_ /  | :|  |\_   /|  |. (_ o _)  |            |   \  ;  \  '_ /  | :
| (_,_) \ |  ||  (_,_)___| > (_)  )  \  '_ '`)    |  _`,/ \ _/  ||  _( )_/ |  ||  (_,_)___|            :_ _:  |  _`,/ \ _/  |
|  |/    \|  |'  \   .---.(  .  .-'   > (_)  )  __: (  '\_/ \   ;| (_ o _) |  |'  \   .---.            (_I_)  : (  '\_/ \   ;
|  '  /\  `  | \  `-'    / `-'`-'|___(  .  .-'_/  )\ `"/  \  ) / |  (_,_)  |  | \  `-'    /           (_(=)_)  \ `"/  \  ) /
|    /  \    |  \       /   |        \`-'`-'     /  '. \_/``".'  |  |      |  |  \       /             (_I_)    '. \_/``".'
`---'    `---`   `'-..-'    `--------`  `._____.'     '-----'    '--'      '--'   `'-..-'              '---'      '-----'
.-------.    ____       .-'''-.    .-'''-.         ,---------. .---.  .---.     .-''-.          .-------.    ____    ,---.   .--. ______        ____       .-'''-.
\  _(`)_ \ .'  __ `.   / _     \  / _     \        \          \|   |  |_ _|   .'_ _   \         \  _(`)_ \ .'  __ `. |    \  |  ||    _ `''.  .'  __ `.   / _     \\
| (_ o._)|/   '  \  \ (`' )/`--' (`' )/`--'         `--.  ,---'|   |  ( ' )  / ( ` )   '        | (_ o._)|/   '  \  \|  ,  \ |  || _ | ) _  \/   '  \  \ (`' )/`--'
|  (_,_) /|___|  /  |(_ o _).   (_ o _).               |   \   |   '-(_{;}_). (_ o _)  |        |  (_,_) /|___|  /  ||  |\_ \|  ||( ''_'  ) ||___|  /  |(_ o _).
|   '-.-'    _.-`   | (_,_). '.  (_,_). '.             :_ _:   |      (_,_) |  (_,_)___|        |   '-.-'    _.-`   ||  _( )_\  || . (_) `. |   _.-`   | (_,_). '.
|   |     .'   _    |.---.  \  :.---.  \  :            (_I_)   | _ _--.   | '  \   .---.        |   |     .'   _    || (_ o _)  ||(_    ._) '.'   _    |.---.  \  :
|   |     |  _( )_  |\    `-'  |\    `-'  |           (_(=)_)  |( ' ) |   |  \  `-'    /        |   |     |  _( )_  ||  (_,_)\  ||  (_.\.' / |  _( )_  |\    `-'  |
/   )     \ (_ o _) / \       /  \       /             (_I_)   (_{;}_)|   |   \       /         /   )     \ (_ o _) /|  |    |  ||       .'  \ (_ o _) / \       /
`---'      '.(_,_).'   `-...-'    `-...-'              '---'   '(_,_) '---'    `'-..-'          `---'      '.(_,_).' '--'    '--''-----'`     '.(_,_).'   `-...-'

""")

def main():
    # player1=Player('Joshua', 4)
    # player2=Player('Danielle', 5)
    # player3=Player('null',4)
    # player4=Player('null',5)
    # player_count = 2
    #
    # player = player2
    # players = [player1, player2,player3,player4]
    # active_players = players[:player_count]
    # for person in active_players:
    #     print(person.name)

    # old_bamboo = 4
    # new_bamboo = 3
    # turn = 1
    # bamboo_logic(old_bamboo,new_bamboo,player, players, turn)
    # print(player.name, player.dice)
    # player = input('Please choose player to give panda to\n')
    # if player.lower() == player1.name.lower():
    #     player1.dice -= 1
    #     print("WOWZA")
    # print(player1.dice)

    welcome()
    time.sleep(3)
    rule = input('would you like to see the rules?\n')
    if 'y' in rule:
        rules()
    player_count, dice_count, player1, player2, player3, player4, player5, players= game_setup()
    dice_logic(player_count, dice_count, player1, player2, player3, player4, player5, players)

if __name__ == '__main__':
    main()
