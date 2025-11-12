# ===========================================
# Euro Exchange Calculator (Bills + Coins)
# Author: [Your Name]
# License: MIT License
# ===========================================

# This program calculates change and updates a cash register's inventory.
#

# --- NUEVO: Definiciones movidas fuera de las funciones ---
# Ahora son globales para que el inventario persista

# Euro denominations in cents, from largest to smallest
EURO_DENOMINATIONS = {
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

# ==========================================================
# --- NUEVO: El inventario de la caja vive aquí ---
# Se modificará con cada transacción.
# ==========================================================
cash_register_stock = {
    "500€ bill": 2,    # 2 billetes de 500€
    "200€ bill": 3,
    "100€ bill": 5,
    "50€ bill": 10,
    "20€ bill": 20,
    "10€ bill": 7,     # Tu ejemplo
    "5€ bill": 15,
    "2€ coin": 30,
    "1€ coin": 30,
    "50c coin": 40,
    "20c coin": 40,
    "10c coin": 40,
    "5c coin": 20,
    "2c coin": 20,
    "1c coin": 20
}
# ==========================================================


# --- MODIFICADO: La función ahora acepta el inventario ---
def calculate_euro_exchange(price_eur, paid_eur, current_stock):
    """
    Calculates the change and updates the stock dictionary in place.
    :param price_eur: Product price in euros (float)
    :param paid_eur: Amount paid in euros (float)
    :param current_stock: The cash register inventory dictionary (will be modified)
    :return: Tuple (change_in_cents, breakdown_dict, remaining_cents_unpaid)
    """

    # Convert both values to cents to avoid floating-point errors
    price_cents = int(round(price_eur * 100))
    paid_cents = int(round(paid_eur * 100))

    # Calculate total change in cents
    change_cents = paid_cents - price_cents

    if change_cents < 0:
        raise ValueError("Error: The paid amount is less than the product price.")

    # Dictionary to store how many of each denomination are used
    breakdown = {denom: 0 for denom in EURO_DENOMINATIONS}

    # Calculate number of each bill/coin
    remaining = change_cents
    for denom, value in EURO_DENOMINATIONS.items():
        if remaining == 0:
            break # No more change needed

        # 1. ¿Cuántos billetes/monedas necesitaríamos idealmente?
        ideal_count = remaining // value
        
        # 2. ¿Cuántos billetes/monedas tenemos en la caja?
        available_count = current_stock[denom]
        
        # 3. ¿Cuántos podemos dar en realidad? (El mínimo de los dos)
        actual_count = min(ideal_count, available_count)
        
        # --- NUEVO: Restar del inventario de la caja ---
        if actual_count > 0:
            current_stock[denom] -= actual_count
        # ---------------------------------------------
        
        # 4. Guardamos la cantidad real que daremos
        breakdown[denom] = actual_count
        
        # 5. Actualizamos el cambio que AÚN nos falta por dar
        remaining = remaining - (actual_count * value)

    # Devuelve el desglose y cualquier cantidad que no se pudo pagar
    return change_cents, breakdown, remaining


def display_exchange(change_cents, breakdown, remaining_cents_unpaid):
    """
    Displays the exchange amount and denomination breakdown.
    :param change_cents: Total change in cents (int)
    :param breakdown: Dictionary of denominations and counts
    :param remaining_cents_unpaid: Amount of change that could not be returned
    """
    # Convert back to euros for display
    euros = change_cents / 100
    print(f"\nTotal change to return: €{euros:.2f}")

    if remaining_cents_unpaid > 0:
        unpaid_euros = remaining_cents_unpaid / 100
        print("======================================================================")
        print(f" WARNING: Could not provide exact change. Amount pending: €{unpaid_euros:.2f}")
        print(" The cash register ran out of the required bills/coins.")
        print("======================================================================")

    print("\nBills to give:")
    for denom, count in breakdown.items():
        if "bill" in denom and count > 0:
            print(f"- {count} × {denom}")

    print("\nCoins to give:")
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
        # MODIFICADO: Pasamos el 'cash_register_stock' a la función
        change_cents, result, remaining_unpaid = calculate_euro_exchange(price, paid, cash_register_stock)

        # Output: display the results
        display_exchange(change_cents, result, remaining_unpaid)


        # --- NUEVO: Mostrar inventario final y valor total ---
        print("\n========================================")
        print("   Final Cash Register Inventory")
        print("========================================")
        
        total_value_cents = 0
        for denom, count in cash_register_stock.items():
            print(f"- {denom}: {count} units")
            # Usamos el diccionario global para calcular el valor restante
            total_value_cents += count * EURO_DENOMINATIONS[denom] 
        
        total_value_euros = total_value_cents / 100
        print("----------------------------------------")
        print(f"Total value in register: €{total_value_euros:.2f}")
        # ----------------------------------------------------

    except ValueError as e:
        print(e)
