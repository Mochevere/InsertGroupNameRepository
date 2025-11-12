# ===========================================
# Euro Exchange Calculator (Bills + Coins)
# Author: [Your Name]
# License: MIT License
# ===========================================

# This program calculates how much change you should receive when paying for a product,
# and gives the breakdown in Euro bills and coins using the largest denominations first.
#
# Example:
# Product price: €13.87
# Amount paid: €20.00
# Output:
#   Total change: €6.13
#   - 1 × 5€ bill
#   - 1 × 1€ coin
#   - 1 × 10c coin
#   - 1 × 2c coin
#   - 1 × 1c coin

def calculate_euro_exchange(price_eur, paid_eur):
    """
    Calculates the change to be returned and its breakdown into Euro bills and coins.
    :param price_eur: Product price in euros (float)
    :param paid_eur: Amount paid in euros (float)
    :return: Tuple (change_in_cents, breakdown_dict)
    """

    # Convert both values to cents to avoid floating-point errors
    price_cents = int(round(price_eur * 100))
    paid_cents = int(round(paid_eur * 100))

    # Calculate total change in cents
    change_cents = paid_cents - price_cents

    if change_cents < 0:
        raise ValueError("Error: The paid amount is less than the product price.")

    # Euro denominations in cents, from largest to smallest
    euro_denominations = {
        "500€ bill": 50000,
        "200€ bill": 20000,
        "100€ bill": 10000,
        "50€ bill": 5000,
        "20€ bill": 2000,
        "10€ bill": 1000,
        "5€ bill": 500,
        "2€ coin": 200,
        "1€ coin": 100,
        "50c coin": 50,
        "20c coin": 20,
        "10c coin": 10,
        "5c coin": 5,
        "2c coin": 2,
        "1c coin": 1
    }

    # Dictionary to store how many of each denomination are used
    breakdown = {denom: 0 for denom in euro_denominations}

    # Calculate number of each bill/coin
    remaining = change_cents
    for denom, value in euro_denominations.items():
        breakdown[denom] = remaining // value
        remaining = remaining % value

    return change_cents, breakdown


def display_exchange(change_cents, breakdown):
    """
    Displays the exchange amount and denomination breakdown.
    :param change_cents: Total change in cents (int)
    :param breakdown: Dictionary of denominations and counts
    """
    # Convert back to euros for display
    euros = change_cents / 100
    print(f"\nTotal change: €{euros:.2f}")

    print("\nBills:")
    for denom, count in breakdown.items():
        if "bill" in denom and count > 0:
            print(f"- {count} × {denom}")

    print("\nCoins:")
    for denom, count in breakdown.items():
        if "coin" in denom and count > 0:
            print(f"- {count} × {denom}")


# ===========================
# Example of program execution
# ===========================

if __name__ == "__main__":
    try:
        # Input: product price and amount paid
        price = float(input("Enter the product price (€): "))
        paid = float(input("Enter the amount paid (€): "))

        # Process: calculate exchange
        change_cents, result = calculate_euro_exchange(price, paid)

        # Output: display the results
        display_exchange(change_cents, result)

    except ValueError as e:
        print(e)
