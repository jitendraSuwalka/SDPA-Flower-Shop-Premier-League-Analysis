# utils.py
# Author: Jitendra Suwalka
# Course: SDPA_EMATM0048
# Section: Data Science 
# Description: 
# This module contains small helper functions that are used throughout
# the program to safely and consistently handle user inputs.

def get_yes_no_input(prompt):
    """
    Prompt the user for a yes/no decision.

    The function only accepts 'y' or 'n' (lowercase) and and will 
    continue to ask for input until it receives one of these two choices.

    Args:
        prompt::str
            Text to display to the user, usually ending with '(y/n): '.

    Returns:
        str
            Either 'y' or 'n', depending on the user's choice.
    """
    
    while True:
        ans = input(prompt).strip().lower()
        if ans in ("y", "n"):
            return ans
        print("Invalid input. Please enter 'y' for yes or 'n' for no.")


def get_valid_integer(prompt, minimum=None, maximum=None, default=None):
    """
    Repeatedly ask the user for an integer until a valid number is given.

    Args:
        prompt::str
            Text displayed to the user.
        minimum::int | None
            The lowest number that can be entered. Any number entered that
              is less than this will have an error message displayed and 
              the user will be asked to enter a number again.
        maximum::int | None
            The highest number that can be entered. Any number entered that
              is greater than this will have an error message displayed and
                the user will be asked to enter a number again.
        default::int | None
            If the user simply enters an Enter key without entering a number,
              then this will be displayed as if it was entered.

    Returns:
        int
            A validated integer that was entered by the user (or the default).
    """
    
    while True:
        raw = input(prompt).strip()
        if raw == "" and default is not None:
            return default
        try:
            val = int(raw)
        except ValueError:
            print("Invalid input. Numbers only.")
            continue
        if minimum is not None and val < minimum:
            print(f"Value must be at least {minimum}.")
            continue
        if maximum is not None and val > maximum:
            print(f"Value must not exceed {maximum}.")
            continue
        return val


def get_valid_name(prompt):
    """
    Ask for a florist name and then validate it

    The input may not be empty and may not include numbers. This is
    done to help ensure that employee names are readable in reports.

    Args:
        prompt::str
            The text that you will use when asking the user for their name.

    Returns:
        str
            A validated, non-empty name that includes only letters and/or spaces.
    """
    
    while True:
        name = input(prompt).strip()
        if not name:
            print("Please enter a name.")
            continue
        if any(ch.isdigit() for ch in name):
            print("Invalid name. Please use letters only.")
            continue
        return name
