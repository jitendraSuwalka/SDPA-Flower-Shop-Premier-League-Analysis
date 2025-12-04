# orders.py
# Author: Jitendra Suwalka
# Section: Data Science Course: SDPA_EMATM0048
# Description: Collects the user's desired monthly sales quantities for each bouquet type, 
#              then checks if you have enough inventory on hand to fill the user's orders.


from utils import get_valid_integer


def collect_orders(bouquet_types, max_vals):
    """
    Collect the information from the user regarding their monthly sales 
    quantities for each bouquet type. 

    Args:
        bouquet_types::list[str]
            List of the names of all bouquets for which you want to gather information.
        max_vals::list[int]
            Maximum quantity that may be ordered for each bouquet type in the same order
            as bouquet_types.

    Returns:
        dict[str, int]
            Mapping from bouquet type to the quantity the user wants to buy this month.
    """
    orders = {}
    for i, b in enumerate(bouquet_types):
        prompt = f"{b} (Max {max_vals[i]}): "
        qty = get_valid_integer(prompt, minimum=0, maximum=max_vals[i])
        orders[b] = qty
    return orders


def check_supplies_for_order(orders, ingredient_usage, inventory):
    """
    Determine if your current inventory will allow you to meet all of the user's requests.

    Args:
        orders::dict[str, int]
            Bouquet quantities the user would like to sell.
        ingredient_usage::dict[str, dict[str, int]]
            Mapping from bouquet type to the number of bunches of each
            flower type are required to make each type of bouquet.
        inventory::dict[str, int]
            mapping from flower type to the current quantity of that flower available in inventory.

    Returns:
        tuple:
            ok::bool
                True if there is enough inventory available to satisfy fulfill all orders;
                 otherwise return false.
            reason::str
                Empty string if ok is true; otherwise writes a message
                of which flower was missing not available and by what amount.

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
