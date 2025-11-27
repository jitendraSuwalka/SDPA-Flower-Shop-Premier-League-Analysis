# orders.py
# Author: Jitendra Suwalka
# Section: Data Science Course: SDPA_EMATM0048
# Description: Handles interactive collection of monthly bouquet orders
#              and checks them against available inventory.

from utils import safe_int


def collect_orders(bouquet_types, max_vals):
    """
    Interactively collect order quantities for each bouquet type.

    Args:
        bouquet_types::list[str]
            Names of the bouquet types to ask the user about.
        max_vals::list[int]
            Maximum amount that can be ordered for each bouquet type,
            in the same order as bouquet_types.

    Returns:
        dict[str, int]
            Mapping from bouquet type to the quantity the player wants
            to sell this month.
    """
    orders = {}
    for i, b in enumerate(bouquet_types):
        prompt = f"{b} (Max {max_vals[i]}): "
        qty = safe_int(prompt, minimum=0, maximum=max_vals[i])
        orders[b] = qty
    return orders


def check_supplies_for_order(orders, ingredient_usage, inventory):
    """
    Verify if inventory is sufficient for the requested orders.

    Args:
        orders::dict[str, int]
            Bouquet quantities the player would like to sell.
        ingredient_usage::dict[str, dict[str, int]]
            Mapping from bouquet type to the number of bunches of each
            flower required per bouquet.
        inventory::dict[str, int]
            Current stock level of each flower type.

    Returns:
        tuple:
            ok::bool
                True if every order can be satisfied with the current
                inventory, otherwise False.
            reason::str
                Empty string when ok is True; otherwise a short message
                explaining which flower is short and by how much.
    """
    required = {"roses": 0, "daisies": 0, "greenery": 0}
    for b, q in orders.items():
        usage = ingredient_usage[b]
        required["roses"] += usage.get("roses", 0) * q
        required["daisies"] += usage.get("daisies", 0) * q
        required["greenery"] += usage.get("greenery", 0) * q

    for f in required:
        if required[f] > inventory.get(f, 0):
            return False, f"{f} short: need {required[f]}, have {inventory.get(f, 0)}"
    return True, ""
