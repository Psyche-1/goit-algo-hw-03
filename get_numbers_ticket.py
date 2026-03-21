import random


def get_numbers_ticket(min: int, max: int, quantity: int) -> list[int]:
    """Function return random numbers between min and max in quantity"""
    if min < 1 or max > 1000 or max < min or (((max + 1) - min) < quantity):
        return []

    return sorted(random.sample(range(min, max + 1), quantity))


# lottery_numbers = get_numbers_ticket(1, 49, 6)
# print("Ваші лотерейні числа:", lottery_numbers)
