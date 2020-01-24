#!/usr/bin/python

"""
     v
[r,p,s]
recursive call n -1

[["rock", rock],["rock", paper],[rock]]


"""

import sys


def rock_paper_scissors(n):

    options = ["rock", "paper", "scissors"]
    plays = []
    # def another fn in here

    def play_rps(num, plays_list=[]):
        if num == 0:
            return plays.append(plays_list)
        else:
            for i in range(len(options)):
                play_rps(num - 1, plays_list + [options[i]])

    play_rps(n)

    return plays


print(rock_paper_scissors(2))

# if __name__ == "__main__":
#     if len(sys.argv) > 1:
#         num_plays = int(sys.argv[1])
#         print(rock_paper_scissors(num_plays))
#     else:
#         print('Usage: rps.py [num_plays]')
