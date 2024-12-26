#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
This script moves the robotic arm to the coordinates specified using the pymycobot library.

https://docs.elephantrobotics.com/docs/gitbook-en/7-ApplicationBasePython/7.3_coord.html
"""

from time import sleep
from enum import Enum

from pymycobot.mycobot import MyCobot
from pymycobot import PI_PORT, PI_BAUD
from pymycobot.genre import Coord


class CoordinateMovementManner(Enum):
    """
    Enum for the manner of movement of the robotic arm.
    """
    ANGULAR = 0
    LINEAR = 1


def main():
    """
    Main function that moves the robotic arm to the coordinates specified.
    """
    mc: MyCobot = MyCobot(port=PI_PORT, baudrate=str(PI_BAUD))

    coords = mc.get_coords()
    print(coords)
    print(type(coords))

    # plans the route and reaches the end effector to the following coordinates
    mc.send_coords(
        coords=[57.0, -107.4, 316.3, -93.81, -12.71, -163.49],
        speed=50,
        mode=CoordinateMovementManner.LINEAR.value)
    sleep(1)
    # only changes the x coordinate
    mc.send_coord(id=Coord.X.value, coord=-40, speed=70)


if __name__ == "__main__":
    main()
