"""My first challenge question"""

__author__ = "730770048"


def mimic(message: str) -> str:
    """This function will repeat back what you say to it"""
    return message


def main() -> None:
    """This will print the result of the mimic function"""
    print(mimic(message=input("What is your message?")))


if __name__ == "__main__":
    main()
