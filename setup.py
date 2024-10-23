from setuptools import find_packages, setup
from typing import List


def get_requirements() -> List[str]:
    """
    This function reads the requirements.txt file and returns a list of requirements,
    excluding '-e .' and comments or empty lines.
    """
    requirement_list: List[str] = []

    try:
        with open("requirements.txt", "r") as file:
            requirement_list = file.readlines()
            # Strip whitespace and filter out empty lines, comments, and '-e .'
            requirement_list = [
                req.strip() for req in requirement_list if req.strip() and not req.startswith("#") and req != "-e ."
            ]

    except FileNotFoundError:
        print("requirements.txt file not found.")
    
    return requirement_list

setup(
    name="flipkart",
    version="0.0.1",
    author="Tanna-Prasanth-kumar",
    author_email="tannaprasanthkumar76@gmail.com",
    packages=find_packages(),
    install_requires=get_requirements()
)
