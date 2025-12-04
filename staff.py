# staff.py
# Author: Jitendra Suwalka
# Section: Data Science Course: SDPA_EMATM0048
# Description: Functions to assist with adding (hiring), listing and 
#              removing (firing) florists from the simulation.

from florist import Florist
from utils import get_valid_name, get_valid_integer, get_yes_no_input

MAX_FLORISTS = 4


def print_staff_list(staff):
    """
    Format and create a nice readable view of the current staff list.

    Args:
        staff::list[Florist]
            List of florist objects which are currently employed.

    Returns:
        list[str]
            List of string descriptions of florists, ready for printing or display.
    """
    display = []
    for f in staff:
        display.append(str(f))
    return display


def hire_interactive(existing_staff):
    """
    Interactively hire new florists,base on the input from user.

    The user decides how many florists to hire (respecting the maximum hiring
    limit of staff) and then user enters each name and speciality(optional)
    for each new hire.
    
    Duplicate names are NOT permitted (case-insensitive).

    Args:
        existing_staff::list[Florist]
            Florists that are already employed. This list is not
            modified directly; instead a new list is returned, which
            contains newly hired florists names.

    Returns:
        list[Florist]
            A list of newly created Florist objects which represent the new 
            hires made in this interactive session. The length of the returned
            list could be zero.

    """
    slots = MAX_FLORISTS - len(existing_staff)
    if slots <= 0:
        return []

    to_hire = get_valid_integer(
        f"\nHow many florists would you like to hire? ({slots} slots available): ",
        minimum=0,
        maximum=slots,
    )

    # If there is no staff hired at all, it requires at least one florist to be hired
    if len(existing_staff) == 0:
        while to_hire == 0:
            print("You must hire at least one florist.")
            to_hire = get_valid_integer(
                f"How many florists would you like to hire? ({slots} slots available): ",
                minimum=1,
                maximum=slots,
            )

    # Store existing staff names (case-insensitive)
    existing_names = {f.name.lower() for f in existing_staff}
    new_names = set()

    new = []
    for _ in range(to_hire):

        # Do not permit duplicate names for florists (case-insensitive)
        while True:
            name = get_valid_name("Please input florist name (one at a time): ")
            name_key = name.lower()

            if name_key in existing_names or name_key in new_names:
                print("A florist with this name already exists. Please choose a different name.")
                continue
            break

        new_names.add(name_key)

        spec = None
        if get_yes_no_input("Does this florist have a speciality ? (y/n): ") == "y":
            print("\nChoose speciality:")
            print("0 - Fern-tastic")
            print("1 - Be-Leaf in Yourself")
            print("2 - You Rose to the Occasion")
            ch = get_valid_integer("Enter choice (0/1/2): ", minimum=0, maximum=2)
            spec_map = {
                0: "Fern-tastic",
                1: "Be-Leaf in Yourself",
                2: "You Rose to the Occasion",
            }
            spec = spec_map[ch]

        new.append(Florist(name, spec))

    return new


def remove_interactive(staff):
    """
    Remove florists at the beginning of the month interactively.

    Flow:
      - Ask if you would like to remove any florists.
      - If so, calculate the maximum number of florists you can remove (max(len(staff)-1)).
      - Ask how many you would like to remove and ask for each name in turn.
      - Never remove the last florist.

    Args:
        staff::list[Florist]
            List of currently employed florists. The list will change
            in place as florists are removed.

    Returns:
        list[str]
            List of the names of the florists who were removed.
    """
    removed = []
    if not staff:
        return removed

    if get_yes_no_input("\nWould you like to remove any florists? (y/n): ") != "y":
        return removed

    if len(staff) <= 1:
        print("You must keep at least one florist. You cannot remove any.")
        return removed

    max_removable = len(staff) - 1
    print(f"You can remove up to {max_removable} florists (at least one must remain).")

    # Ask how many florists to remove
    num_remove = get_valid_integer(
        f"How many florists would you like to remove? (1–{max_removable}): ",
        minimum=1,
        maximum=max_removable,
    )

    for i in range(num_remove):
        while True:

            # If only one florist is left, we stop the removal process.
            # The shop must always have at least one florist.
            if len(staff) <= 1:
                print("You must keep at least one florist. Cannot remove more.")
                return removed
            # Prompt the user to enter the name of the florist they wish to remove
            name = input("Enter florist name (one at a time): ").strip()
            if not name:
                print("Please enter a florist name.")
                continue

            found = False

             # Search in the staff list to find out user entered florist name
            for f in staff:
                if f.name.lower() == name.lower():
                    staff.remove(f)
                    removed.append(f.name)
                    print(f"Removed florist {f.name}.")
                    found = True
                    break

            # If no matching florist was found, display an error message to the user
            if not found:
                print("Florist not found. Please enter a valid name.")
            else:
                break

    # Display names of florists removed
    if removed:
        print(f"Florists removed: {removed}")
    return removed
