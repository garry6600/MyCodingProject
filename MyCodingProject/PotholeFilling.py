"""
File: PotholeFilling.py
Name: Garry:
--------------------------
This program shows karel filling 3
potholes. Students learn the concept of
decomposition through the process.
"""

from karel.stanfordkarel import *


def main():
    """
    Pre-condition: Karel is at the (2,1)
    Post-condition: Karel is at the (2,7)
    """
    for i in range(3):
        go_in()
        put_33_beepers()
        go_out()


def go_in():
    """
    Pre-condition: Karel is at the upper left, facing East.
    Post-condition: Karel is in the pothole, facing South.
    """
    move()
    turn_right()
    move()


def put_33_beepers():
    """
    Karel will put 33 beepers
    """
    for i in range(33):
        put_beeper()


def go_out():
    """
    Pre-condition: Karel is in the pothole, facing South.
    Post-condition: Karel is at the upper left, facing East.
    """
    turn_around()
    move()
    turn_right()
    move()

def turn_right():
    turn_left()
    turn_left()
    turn_left()

def turn_around():
    turn_left()
    turn_left()

    pass


"""
def main():
    for i in range(3):
        move()
        turn_right()
        move()
        put_33_beepers()
        turn_around()
        move()
        turn_right()
        move()


def turn_right():
    turn_left()
    turn_left()
    turn_left()


def turn_around():
    turn_left()
    turn_left()


def put_33_beepers():
    for i in range(33):
        put_beeper()
"""


# ----- DO NOT EDIT CODE BELOW THIS LINE ----- #
if __name__ == '__main__':
    execute_karel_task(main)
