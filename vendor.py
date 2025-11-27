# vendor.py
# Author: Jitendra Suwalka
# Section: Data Science 
# Course: SDPA_EMATM0048
# Description: Supplier price information and a small helper for
#              converting user choices into supplier names.

# Supplier name and price information used by inventory/restock

SUPPLIERS = {
    "Evergreen Essentials": {"roses": 2.80, "daisies": 1.50, "greenery": 0.95},
    "FloraGrow Distributors": {"roses": 1.60, "daisies": 1.20, "greenery": 1.80},
}


def get_supplier_by_index(idx):
    """
    This function Converts a numeric user choice into a supplier name.

    Args:
        idx::int | str
            Index entered by the user, expected to be 0 or 1.

    Returns:
        str | None
            Supplier name if idx is valid, otherwise None.
    """
    names = list(SUPPLIERS.keys())
    try:
        return names[int(idx)]
    except Exception:
        return None
