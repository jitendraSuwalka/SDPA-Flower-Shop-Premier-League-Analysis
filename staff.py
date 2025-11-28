# staff.py
# Author: Jitendra Suwalka
# Section: Data Science Course: SDPA_EMATM0048
# Description: Utility functions for hiring, listing and removing florists
#              in the simulation.

from florist import Florist
from utils import get_valid_name, get_valid_integer, get_yes_no_input

MAX_FLORISTS = 4


def print_staff_list(staff):
    """
    Build a nicely formatted representation of the current staff list.

    Args:
        staff::list[Florist]
            List of florist objects currently employed.

    Returns:
        list[str]
            List of string descriptions, ready to print or display.
    """
    display = []
    for f in staff:
        display.append(str(f))
    return display


def hire_interactive(existing_staff):
    """
    Interactively hire new florists.

    The user chooses how many florists to hire (respecting the maximum
    staff limit) and then enters each name and optional speciality.

    Duplicate names are NOT allowed (case-insensitive).

    Args:
        existing_staff::list[Florist]
            Florists that are already employed. This list is not
            modified directly; instead a list of new hires is returned.

    Returns:
        list[Florist]
            Newly created Florist instances representing the hires
            made in this interaction. May be empty.
    """
    slots = MAX_FLORISTS - len(existing_staff)
    if slots <= 0:
        return []

    to_hire = get_valid_integer(
        f"\nHow many florists would you like to hire? ({slots} slots available): ",
        minimum=0,
        maximum=slots,
    )

    # If no staff at all, require at least one florist to be hired
    if len(existing_staff) == 0:
        while to_hire == 0:
            print("You must hire at least one florist.")
            to_hire = get_valid_integer(
                f"How many florists would you like to hire? ({slots} slots available): ",
                minimum=1,
                maximum=slots,
            )

    # NEW: Track existing names (case-insensitive)
    existing_names = {f.name.lower() for f in existing_staff}
    new_names = set()

    new = []
    for _ in range(to_hire):

        # Prevent duplicate florist names (case-insensitive)
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
    Interactively remove florists at the start of a month.

    Flow:
      - Ask the player whether they want to remove any florists.
      - If yes, compute the maximum removable (len(staff) - 1).
      - Ask for how many to remove and then for each name in turn.
      - Never remove the last remaining florist.

    Args:
        staff::list[Florist]
            List of currently employed florists. This list is modified
            in-place as florists are removed.

    Returns:
        list[str]
            Names of florists that were successfully removed.
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

    # Ask how many to remove
    num_remove = get_valid_integer(
        f"How many florists would you like to remove? (1–{max_removable}): ",
        minimum=1,
        maximum=max_removable,
    )

    for i in range(num_remove):
        while True:
            # Stop if only one florist left
            if len(staff) <= 1:
                print("You must keep at least one florist. Cannot remove more.")
                return removed

            name = input("Enter florist name (one at a time): ").strip()
            if not name:
                print("Please enter a florist name.")
                continue

            found = False
            for f in staff:
                if f.name.lower() == name.lower():
                    staff.remove(f)
                    removed.append(f.name)
                    print(f"Removed florist {f.name}.")
                    found = True
                    break
            if not found:
                print("Florist not found. Please enter a valid name.")
            else:
                break

    if removed:
        print(f"Florists removed: {removed}")
    return removed
