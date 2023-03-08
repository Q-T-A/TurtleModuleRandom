"""
Author: Quinton Austin, qaustin@purdue.edu
Assignment: 06.3 - Random Vowels
Date: 03/03/2023

Description:
    This program draws a random vowel

Contributors:
    Quinton Austin, qaustin@purdue.edu [repeat for each]

My contributor(s) helped me:
    [x] understand the assignment expectations without
        telling me how they will approach it.
    [x] understand different ways to think about a solution
        without helping me plan my solution.
    [x] think through the meaning of a specific error or
        bug present in my code without looking at my code.
    Note that if you helped somebody else with their code, you
    have to list that person as a contributor.

Academic Integrity Statement:
    I have not used source code obtained from any unauthorized
    source, either modified or unmodified; nor have I provided
    another student access to my code.  The project I am
    submitting is my own original work.
"""

"""Import modules below this line (starting with unit 6)."""
from turtle import *
import vowels
import random

"""Write new functions below this line (starting with unit 4)."""


def start():
    """This function initializes the window and the turtle.
    Do not modify this function or any of the properties it sets.
    """
    setup(600, 400)
    width(9)
    speed(10)
    penup()
    goto(-220, -30)


def main():
    """Write your mainline logic below this line (then delete this line)."""
    x, y = -220, -30
    r = [1,2,3,4,5]
    random.shuffle(r)
    for i in range(5):
        if r[i] == 1:
            vowels.draw_a()
        elif r[i] == 2:
            vowels.draw_e()
        elif r[i] == 3:
            vowels.draw_i()
        elif r[i] == 4:
            vowels.draw_o()
        elif r[i] == 5:
            vowels.draw_u()

        setheading(0)
        penup()
        forward(95)
        sety(-30)


"""Do not change anything below this line."""
if __name__ == "__main__":
    start()
    main()
    done()
