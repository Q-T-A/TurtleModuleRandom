"""
Author: Quinton Austin, qaustin@purdue.edu
Assignment: 06.4 - log spiral
Date: MM/DD/YYYY

Description:
    This program provides an algorithm to produce a log spiral 

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

"""Import additional modules below this line (starting with unit 6)."""
from turtle import *
import math


"""Write new functions below this line (starting with unit 4)."""


def start():
    """This function initializes the window and the turtle.
    Do not modify this function or any of the properties it sets.
    """
    setup(564, 564)
    width(5)


def main():
    """Write your mainline logic below this line (then delete this line)."""
     # Define constants
    a = 4
    b = 0.22

    # Move turtle to initial position
    x0 = a * math.cos(0)
    y0 = a * math.sin(0)
    penup()
    goto(x0, y0)
    pendown()

    # Draw spiral
    for theta_degrees in range(0, 1085, 5):
        # Convert degrees to radians
        theta = math.radians(theta_degrees)

        # Calculate x and y coordinates
        x = a * math.exp(b * theta) * math.cos(theta)
        y = a * math.exp(b * theta) * math.sin(theta)

        # Move turtle to next point
        goto(x, y)



"""Do not change anything below this line."""
if __name__ == "__main__":
    start()
    main()
    done()
