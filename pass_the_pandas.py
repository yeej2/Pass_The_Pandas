import random as r
import time


dict={1:"Blank", 2:"Bamboo", 3:"Water", 4:"Panda"}

class Player :

    # The age and gender parameters has a default value.
    def __init__ (self, name, dice_count):

        self.name = name
        self.dice = dice_count

    def showInfo(self):
        print ("Name: ", self.name)
        print ("Dice: ", self.dice)

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
        players = [player1, player2, player3, player4, player5]

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
        players = [player1, player2, player3, player4]

    elif player_count == 3:
        dice_count = 6
        player1 = input("Please input player 1 name\n")
        player1 = Player(player1,dice_count)
        player2 = input("Please input player 2 name\n")
        player2 = Player(player2,dice_count)
        player3 = input("Please input player 3 name\n")
        player3 = Player(player3,dice_count)
        players = [player1, player2, player3]

    elif player_count == 2:
        dice_count = 6
        player1 = input("Please input player 1 name\n")
        player1 = Player(player1,dice_count)
        player2 = input("Please input player 2 name\n")
        player2 = Player(player2,dice_count)
        players = [player1, player2]

    elif player_count > 5:
        print("Too many players")
    else:
        print("Too few players")

    return(player_count, dice_count, players)

    # print(r.randint(1,4))
def dice_logic(player_count, dice_count, players):

    turn = 0
    bamboo_round = 0
    bamboo_on = False
    carryover = 0
    old_bamboo = 0
    game_end = False


    while game_end == False:
        water = 0

        if players[turn].name == 'null':
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
        input("\n\n{0} ROLL THE DICE!!!!\n".format(player_turn.name.upper()))
        while x < player_turn.dice:
            dice_values.append(r.randint(1,4))
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

        for die in dice:
            if die == "Panda":
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
        # player = input('Please choose player to give panda to\n')

        if bamboo_round == 0:
            old_bamboo = dice.count("Bamboo")
        else:
            new_bamboo = dice.count("Bamboo")

        if bamboo_on is True:
            if old_bamboo > 0:
                print("BAMBOO PHASE")
                time.sleep(2)
                carryover = bamboo_logic(old_bamboo, new_bamboo, player_turn, players, turn, player_count)
            if carryover == None:
                old_bamboo=0
            else:
                old_bamboo = carryover

        bamboo_on=True
        bamboo_round+=1


        print("\n",player_turn.name,"now has", player_turn.dice, "dice\n")
        turn +=1
    print("\n *********** ", player_turn.name.upper(), " IS THE WINNER **************")
        # print(dice)
    # for die in dice:
    #     print(die)
    #     time.sleep(.4)

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
        carryover = new_bamboo - old_bamboo
        print(prev_player.name," did not pass any bamboo to ", player_turn.name)
        # print(carryover)
        time.sleep(1)
        return carryover

    elif old_bamboo == new_bamboo:
        print(player_turn.name, "had the same amount of bamboo as", prev_player.name)
        time.sleep(1)
        pass

def main():
    game_end = False
    # player_count, dice_count, players= game_setup()
    player1=Player('Joshua', 4)
    player2=Player('Danielle', 5)
    players = [player1, player2]
    player=player1
    while game_end == False:
        for player in players:
            if player.dice == 0:
                game_end = True
        print("GAME STILL GOES")
        print(player.dice)
        player.dice -=1
    # dice_logic(player_count, dice_count, players)

if __name__ == '__main__':
    main()
