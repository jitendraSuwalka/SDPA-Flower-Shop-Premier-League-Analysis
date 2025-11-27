# inventory.py
# Author: Jitendra Suwalka
# Section: Data Science Course: SDPA_EMATM0048
# Description: Greenhouse inventory model, including depreciation,
#              storage cost calculation and restocking logic.

import math
from vendor import SUPPLIERS, get_supplier_by_index

# Greenhouse capacity, depreciation and storage cost per bunch
CAPACITY = {"roses": 200.0, "daisies": 250.0, "greenery": 400.0}
DEPRECIATION = {"roses": 0.40, "daisies": 0.15, "greenery": 0.05}
STORAGE_COST = {"roses": 1.50, "daisies": 0.80, "greenery": 0.20}


def apply_depreciation(inventory: dict):
    """
    Apply depreciation to the current inventory in-place.

    Coursework rule:
        loss = ceil(current_qty * depreciation_rate)
        new_qty = current_qty - loss

    The quantities in the inventory dictionary are always stored as
    whole numbers (no fractional bunches).

    Args:
        inventory::dict[str, int]
            Mutable mapping from flower name to bunch count. This
            dictionary is modified directly.

    Returns:
        dict[str, int]
            The same inventory dictionary, after depreciation.
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
    Compute monthly greenhouse storage cost for the current inventory.

    Args:
        inventory::dict[str, int]
            Current bunch counts for each flower type.

    Returns:
        float
            Total storage cost for this month.
    """
    total = 0.0
    for f, qty in inventory.items():
        total += qty * STORAGE_COST[f]
    return total


def restock_to_capacity(inventory: dict, chosen_suppliers: dict) -> float:
    """
    Restock all flowers up to the greenhouse capacity.

    This function adjusts inventory in-place and returns the total cost
    of the restocking step.

    Args:
        inventory::dict[str, int]
            Current bunch counts for each flower type. It will be
            updated so that every flower reaches CAPACITY.
        chosen_suppliers::dict[str, str]
            Mapping from flower name to supplier index ("0" or "1")
            as chosen by the player in the game.

    Returns:
        float
            The total amount of money spent on restocking.
    """
    restock_cost = 0.0
    for f in ["roses", "daisies", "greenery"]:
        supplier_choice = chosen_suppliers.get(f)
        if supplier_choice is None:
            continue

        supplier_name = get_supplier_by_index(supplier_choice)
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
