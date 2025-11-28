# utils.py
# Author: Jitendra Suwalka
# Section: Data Science Course: SDPA_EMATM0048
# Description: Small helper functions for robust user input handling.

def yes_no(prompt):
    """
    Prompt the user for a yes/no decision.

    The function only accepts 'y' or 'n' (lowercase) and will keep
    asking until a valid answer is provided.

    Args:
        prompt::str
            Text to display to the user, usually ending with '(y/n): '.

    Returns:
        str
            Either 'y' or 'n', depending on the user's choice.
    """
    """Return 'y' or 'n' only; keep asking until valid."""
    while True:
        ans = input(prompt).strip().lower()
        if ans in ("y", "n"):
            return ans
        print("Invalid input. Please enter 'y' for yes or 'n' for no.")


def safe_int(prompt, minimum=None, maximum=None, default=None):
    """
    Ask for an integer repeatedly until a valid value is entered.

    Args:
        prompt::str
            Text displayed to the user.
        minimum::int | None
            Optional lower bound. If provided, values below this are
            rejected with an explanatory message.
        maximum::int | None
            Optional upper bound. If provided, values above this are
            rejected with an explanatory message.
        default::int | None
            If not None and the user just presses Enter, this value is
            returned instead of asking again.

    Returns:
        int
            A validated integer supplied by the user (or the default).
    """
    # Original implementation kept; only documentation added.
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


def safe_name(prompt):
    """
    Ask for a florist name and apply simple validation rules.

    The input may not be empty and may not contain digits. This keeps
    staff names readable in reports.

    Args:
        prompt::str
            Text used when asking for the name.

    Returns:
        str
            A validated, non-empty name containing letters (and
            possibly spaces) only.
    """
    """Ask for a florist name (simple validation: non-empty, no digits)."""
    while True:
        name = input(prompt).strip()
        if not name:
            print("Please enter a name.")
            continue
        if any(ch.isdigit() for ch in name):
            print("Invalid name. Please use letters only.")
            continue
        return name
