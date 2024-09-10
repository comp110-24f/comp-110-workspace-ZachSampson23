"""State what the point of the function is"""

__author__: str = "730770048"


def main_planner(guests: int) -> None:
    """This function calls each function and producs printed output"""
    print("A Cozy Tea Party for " + str(guests) + " People!")
    print("Tea Bags: " + str(tea_bags(guests)))
    print("Treats: " + str(treats(guests)))
    print("Cost: $" + str(cost(tea_count=tea_bags(guests), treat_count=treats(guests))))


def tea_bags(people: int) -> int:
    """This is a function to compute the number of tea bags needed."""
    return people * 2


def treats(people: int) -> int:
    """This is a function to find out how many treats are needed"""
    return int(tea_bags(people) * 1.5)


def cost(tea_count: int, treat_count: int) -> float:
    """This function finds out what the total cost is between the treats and tea"""
    return 0.5 * tea_count + 0.75 * treat_count


if __name__ == "__main__":
    main_planner(guests=int(input("How many guests are attending your tea party?")))
