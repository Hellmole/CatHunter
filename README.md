# CatHunter
 "CatHunter" - super easy spider robot powered by Raspberry Pi Pico

Material:

- Raspberyy Pi Pico
- Kitronik Simply Servos (https://resources.kitronik.co.uk/pdf/5339-kitronik-simply-servos-raspberry-pi-pico-datashseet.pdf)
- Micro servo SG90
- NiMH 6V or AC/DC adapter 4A 5V
- HY-SRF05 SRF05
- Body: https://www.gutta.cz/product/colured-plates-for-crafts/


Library for Kitronik:
https://github.com/KitronikLtd/Kitronik-Pico-Simply-Servos-MicroPython

MicroPython:
https://micropython.org/download/RPI_PICO/

![obrazek](https://github.com/user-attachments/assets/037459ef-2290-447e-9232-8cee4701572a)
![obrazek](https://github.com/user-attachments/assets/ea8af646-57ac-40c6-a803-de6b6adfb3fe)
![Uploading obrazek.png…]()

Code:

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







