"""Functions for parsing file input for AoC 2020."""

from typing import List


def get_file_input(url: str) -> List[str]:
    with open(url) as file:
        return file.readlines()

