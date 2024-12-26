#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
This script moves the robotic arm to the angles specified using the pymycobot library.

https://docs.elephantrobotics.com/docs/gitbook-en/7-ApplicationBasePython/7.7_example.html#8-controlling-sucking-pump
"""

from typing import Dict, List, Literal
from time import sleep

from pymycobot.mycobot import MyCobot
from pymycobot import PI_PORT, PI_BAUD

from src.pump import pump_on, pump_off


init_angles: List[float] = [0, 0, 0, 0, 0, 0]
demo_angles: List[List[float]] = [
    [92.9, -10.1, -60, 5.8, -2.02, -37.7],
    [92.9, -53.7, -83.05, 50.09, -0.43, -38.75],
    [92.9, -10.1, -87.27, 5.8, -2.02, -37.7]
]

bins_angles: Dict[Literal["A", "B", "C", "D"], List[float]] = {
    "A": [],
    "B": [],
    "C": [],
    "D": []
}


def main():
    """
    Main function that moves the robotic arm to the angles specified.
    """
    mc: MyCobot = MyCobot(port=PI_PORT, baudrate=str(PI_BAUD))

    angles = mc.get_angles()
    print(angles)
    print(type(angles))

    # robotic arm recovery
    mc.send_angles(init_angles, 30)
    sleep(3)

    # turn on the suction pump
    pump_on()
    mc.send_angles(demo_angles[2], 30)
    sleep(2)

    # absorb small blocks
    mc.send_angles(demo_angles[1], 30)
    sleep(2)
    mc.send_angles(demo_angles[0], 30)
    sleep(2)
    mc.send_angles(demo_angles[1], 30)
    sleep(2)

    # turn off the suction pump
    pump_off()
    mc.send_angles(demo_angles[0], 40)
    sleep(1.5)


if __name__ == "__main__":
    main()
