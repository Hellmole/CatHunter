

from SimplyServos import KitronikSimplyServos
from time import sleep

servos = KitronikSimplyServos()

# fce servo move

def move_legs(positions, delay=0.2):
    for servo, position in positions.items():
        servos.goToPosition(servo, position)
    sleep(delay)

# move

def move1():
    move_legs({1: 90, 6: 90, 3: 160, 5: 20})
    move_legs({2: 90, 7: 90, 4: 90, 8: 90})


def move2():
    move_legs({3: 90, 5: 90, 1: 30, 6: 150})
    move_legs({2: 140, 7: 30, 4: 60, 8: 120})


def move3():
    move_legs({1: 90, 6: 90, 3: 90, 5: 90})
    move_legs({4: 90, 8: 90, 2: 30, 7: 150})


def move4():
    move_legs({4: 180, 8: 0, 2: 60, 7: 60})
    move_legs({4: 90, 8: 90, 2: 30, 7: 150})

# main loop
while True:
    move1()
    move2()
    move3()
    move4()
