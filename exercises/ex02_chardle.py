"""EX02 - Chardle - a cute step toward wordle."""

__author__ = "730770048"


def input_word() -> str:
    userWord = input("Enter a 5-character word: ")
    """Function used to determine what word will be searched in the main function"""
    if len(userWord) == 5:
        print("'" + userWord + "'")
    else:
        print("Error: Word must contain 5 characters.")
        exit()
        print("'" + userWord + "'")

    return userWord


def input_letter() -> str:
    userCharacter = input("Enter a single character: ")
    """Function to determine what character will be searched for in the word"""
    if len(userCharacter) == 1:
        print("'" + userCharacter + "'")
    else:
        print("Error: Character must be a single character. ")
        """Using the exit function to exit the function early because of the error"""
        exit()
    return userCharacter


def contains_char(word: str, letter: str) -> None:
    index = 0
    count = 0
    """Function to determine if a certain character is in a certain word."""
    print("Searching for " + letter + " in " + word + ".")
    while index + 1 <= len(word):
        if word[index] == letter:
            print(letter + " found at index " + str(index))
            index = index + 1
            count = count + 1
        else:
            index = index + 1

    if count >= 1:
        print(str(count) + " instances of " + letter + " in " + word)
    else:
        print("No instances of " + letter + " in " + word)


def main() -> None:
    contains_char(input_word(), input_letter())


if __name__ == "__main__":
    main()
