# inventory.py
# Author: Jitendra Suwalka
# Section: Data Science Course: SDPA_EMATM0048
# Description: This is basically the Greenhouse inventory model, which includes 
#              functions to calculate depreciation for greenhouse inventory, 
#              greenhouse storage cost for current inventory and restocking logic.            

import math
from vendor import SUPPLIERS, get_supplier_by_user_choice

# Greenhouse capacity, depreciation and storage cost per bunch
CAPACITY = {"roses": 200.0, "daisies": 250.0, "greenery": 400.0}
DEPRECIATION = {"roses": 0.40, "daisies": 0.15, "greenery": 0.05}
STORAGE_COST = {"roses": 1.50, "daisies": 0.80, "greenery": 0.20}


def apply_depreciation(inventory: dict):
    """
    Apply depreciation to the currently available inventory

    As per Coursework Rule:
        loss = ceil(current_qty * depreciation_rate)
        new_qty = current_qty - loss

    Note that the quantity in the inventory dictionary is always a 
    whole number (there can never be a fraction of a bunch).

    Args:
        inventory::dict[str, int]
            A mutable map of flower names to bunch counts. 
            This dictionary is changed directly.

    Returns:
        dict[str, int]
            The inventory dictionary, with depreciation applied.
    """
    for f in list(inventory.keys()):
        qty = inventory.get(f, 0)

        loss_raw = qty * DEPRECIATION[f]
        loss = math.ceil(loss_raw)

        remaining = qty - loss
        if remaining < 0:
            remaining = 0

        inventory[f] = int(remaining)

    return inventory


def greenhouse_storage_cost(inventory: dict) -> float:
    """
    Compute the monthly storage cost of the greenhouse for the current inventory.

    Args:
        inventory::dict[str, int]
            Current bunch counts for each flower type in the inventory.

    Returns:
        float
            The total storage cost for the month.
    """
    total = 0.0
    for f, qty in inventory.items():
        total += qty * STORAGE_COST[f]
    return total


def restock_to_capacity(inventory: dict, chosen_suppliers: dict) -> float:
    """
    Restock all flowers to the capacity of the greenhouse.

    The function modifies the inventory in place and returns 
    the total cost of the restocking process.

    This function modifies the inventory in place and returns 
    the total cost of the restocking.

    Args:
        inventory::dict[str, int]
            Counts of bunches in the current inventory for each flower type. 
            Each flower type will be adjusted so it has reached its CAPACITY.
        chosen_suppliers::dict[str, str]
            Mapping of flower name to selected supplier index
           ("0" or "1") from the player's choices in the game.

    Returns:
        float
            Total amount of money spent on restocking.
    """
    restock_cost = 0.0
    for f in ["roses", "daisies", "greenery"]:
        supplier_choice = chosen_suppliers.get(f)
        if supplier_choice is None:
            continue

        supplier_name = get_supplier_by_user_choice(supplier_choice)
        price = SUPPLIERS[supplier_name][f]

        cap = int(CAPACITY[f])
        current = int(inventory.get(f, 0))
        to_buy = cap - current
        if to_buy < 0:
            to_buy = 0

        cost = to_buy * price
        restock_cost += cost

        inventory[f] = current + to_buy

    return restock_cost
