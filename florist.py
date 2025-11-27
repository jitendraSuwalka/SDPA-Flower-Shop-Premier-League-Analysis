# florist.py
# Author: Jitendra Suwalka
# Section: Data Science Course: SDPA_EMATM0048
# Description: Represents a single florist and their optional speciality.

class Florist:
    """
    Represent a florist employed by the flower shop.

    Attributes:
        name::str
            Display name of the florist.
        speciality::str | None
            Bouquet type this florist specialises in, or None if they
            are a generalist.
    """

    def __init__(self, name, speciality=None):
        """
        Create a new Florist instance.

        Args:
            name::str
                Name of the florist as entered by the player.
            speciality::str | None
                Optional bouquet-type speciality string, or None if
                the florist has no speciality.
        """
        self.name = name
        self.speciality = speciality  # "Fern-tastic", etc., or None

    def __str__(self):
        """
        Return a user-friendly string for menus and reports.

        Returns:
            str
                The florist's name, including their speciality in
                brackets when they have one.
        """
        if self.speciality:
            return f"{self.name} ({self.speciality})"
        return self.name
