#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
`pip install .`
"""

from setuptools import setup, find_packages

setup(
    name="cobot",
    version="1.0.0",
    author="Xuhua Huang and al.",
    author_email="xhuan484@uwo.ca",
    description=(
        "A minimum Python library for controlling a 6-axis robotic arm, designed for "
        "educational purposes led by the Machine Intelligence (MIN) Lab at the "
        "University of Western Ontario."
    ),
    long_description=open("README.md", encoding='utf-8').read(),
    long_description_content_type="text/markdown",
    url="https://github.com/XuhuaHuang/cobot",
    roject_urls={
        "Documentation": "https://github.com/XuhuaHuang/cobot/doc",
        "Source Code": "https://github.com/XuhuaHuang/cobot",
    },
    license="MIT",
    classifiers=[
        "Development Status :: 4 - Beta",
        "Intended Audience :: Education",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Topic :: Education :: Robotics",
        "Topic :: Scientific/Engineering :: Artificial Intelligence",
    ],
    keywords=[
        "robotics",
        "6-axis robot arm",
        "mycobot 280 pi",
        "education",
        "machine intelligence",
        "university",
        "robotics control",
    ],
    packages=find_packages(where="src"),
    package_dir={"": "src"},
    python_requires=">=3.8",
    install_requires="requirements.txt",  # Use dependencies from requirements.txt
    extras_require={
        "dev": ["pytest>=7.0", "sphinx>=5.0", "black>=23.0"],
    },
    entry_points={
        "console_scripts": [
            "cobot=calibrate:main",  # Maps the command `cobot` to `main` in `src/calibrate.py`
        ],
    },
    include_package_data=True,
    zip_safe=False,
)
