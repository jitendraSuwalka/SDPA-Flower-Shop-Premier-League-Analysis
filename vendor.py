# vendor.py
# Author: Jitendra Suwalka
# Section: Data Science 
# Course: SDPA_EMATM0048
# Description: 
# This module stores supplies names along with pricing information  
# Also this module will have one function to help us to find out the supplier names
# based on user input for flower restocking process

# This is a dictionary having supplier names and their flower price information
SUPPLIERS = {
    "Evergreen Essentials": {"roses": 2.80, "daisies": 1.50, "greenery": 0.95},
    "FloraGrow Distributors": {"roses": 1.60, "daisies": 1.20, "greenery": 1.80},
}

# This function will help to find supplier name based on user choice
def get_supplier_by_user_choice(choice):
    """
    
    This function converts a numeric user choice into a supplier name.
    This function safely converts the user's numeric input (0 or 1)
    into the corresponding supplier name from the SUPPLIERS dictionary.
    If the input is invalid, none is returned.

    Args:
        choice::int | str
            Numeric input entered by the user (expected to be 0 or 1).

    Returns:
        str | None:
            The supplier name if the input is valid, 
            otherwise None.

    """
    names = list(SUPPLIERS.keys())
    try:
        return names[int(choice)]
    except Exception:
        return None
