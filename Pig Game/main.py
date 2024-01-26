# Pig Game
# Joao Pedro Costa
# These Game will function as follows:
# The user roll a dice(1 to 6), any times he wants and
# the number that comes up will be added to a total score,
# but if it comes up a 1 all the score is lost
import random


def users():
    name_users = []
    score = []
    num_users = int(input("How many users will play the game: "))
    for i in range(num_users):
        name = input("What is your name: ")
        name_users.append(name)
        score.append(0)

    roll_dice(name_users, score)


def roll_dice(name_users, score):
    i = 0
    while score[i] < 51:
        print("\nPlayer: {}".format(name_users[i]))
        while True:
            roll = random.randint(1, 6)
            if roll == 1:
                print("You got number: {}".format(roll))
                score[i] = 0
                print("Your score: 0\n")
            else:
                print("You got number: {}".format(roll))
                score[i] = score[i] + roll
                print("Your score: {}\n".format(score[i]))

            choice = input("Do you want to roll again? (y/n) : ")
            if choice.lower() == 'y':
                continue
            else:
                if i == len(name_users) - 1:
                    i = 0
                else:
                    i += 1
                break


def main():
    users()


main()

