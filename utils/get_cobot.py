#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Gets the MyCobot robot instance using the pymycobot library.

https://docs.elephantrobotics.com/docs/gitbook-en/7-ApplicationBasePython/7.2_API.html#introduction-to-api
"""

import sys
import subprocess
import logging


# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s",
    handlers=[
        logging.StreamHandler(sys.stdout)
    ]
)


def ensure_package_installed(package_name: str) -> None:
    """
    Ensures a Python package is installed. If not, attempts to install it.

    Args:
        package_name (str): The name of the package to check/install.
    """
    try:
        __import__(name=package_name)
        logging.info("The package '%s' is already installed.", package_name)
    except ImportError:
        logging.warning(
            "The package '%s' is not installed. Attempting to install...", package_name)
        try:
            subprocess.check_call(
                [sys.executable, "-m", "pip", "install", package_name])
            logging.info(
                "The package '%s' has been installed successfully.", package_name)
        except subprocess.CalledProcessError as e:
            logging.error(
                "Failed to install the package '%s'. Error: %s", package_name, e)
            sys.exit(1)


def cobot():
    """
    Gets the MyCobot robot instance using the pymycobot library.

    Returns:
        MyCobot280: The MyCobot robot instance.
    """
    package_name: str = "pymycobot"
    ensure_package_installed(package_name)

    try:
        # from pymycobot.mycobot import MyCobot
        # depreated since version 3.6.0, using MyCobot280 instead
        from pymycobot import MyCobot280
        from pymycobot import PI_PORT, PI_BAUD
        logging.info("Successfully imported '%s'. Ready to use.", package_name)

        return MyCobot280(port=PI_PORT, baudrate=str(PI_BAUD), timeout=0.1, debug=False)

    except ImportError as e:
        logging.error(
            "Unexpected error while importing '%s'. Error: %s", package_name, e)
        sys.exit(1)


def main():
    """
    The main function prints the usage of the script.
    """
    print("""\
Usage:
from utils.get_cobot import cobot
bot = cobot()
bot.get_angles()\
          """)


if __name__ == "__main__":
    main()
