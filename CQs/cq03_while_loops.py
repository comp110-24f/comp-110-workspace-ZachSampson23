"""Challenge question with While Loops"""

__author__ = "730770048"


def num_instances(phrase: str, search_char: str) -> int:
    index = 0
    count = 0
    while index < len(phrase):
        if phrase[index] == search_char:
            count = count + 1
            index = index + 1
        else:
            index = index + 1
    print(count)
    return count
