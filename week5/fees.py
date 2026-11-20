"""Module for calculating student fees."""


def calculate_fee(amount, discount):
    """Calculate the final fee after applying a discount."""
    if amount < 0 or discount < 0 or discount > 100:
        raise ValueError("Invalid amount or discount")

    return amount - (amount * discount / 100)