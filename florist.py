# florist.py
# Author: Jitendra Suwalka
# Course: SDPA_EMATM0048
# Section: Data Science
# Description:This module defines the Florist class, which represents an individual
#             employee working in the flower shop called florist. Each florist may also
#             have a speciality, which helps them produce certain bouquets more efficiently. 
class Florist:
    """
    This class represent a single florist employed by the flower shop.

    A florist can either be a general worker or can have a specific
    bouquet speciality (eg. Fern-tastic,Be-Leaf in Youself,
    You rose to the Occasion)that improves production efficiency for 
    that bouquet type.

    Attributes:
        name::str
            Display name of the florist.
        speciality::str | None
            The bouquet type in which this florist specialises in, or None if the florist
            is not specialist.
    """

    def __init__(self, name, speciality=None):
        """
        This method create and initialise a new Florist object.

        Args:
            name::str
                The name of the florist as entered by the user.
            speciality::str | None,optional
                The bouquet type this florist specialises in.
                Defaults to none if the florist has no speciality.

        """
        self.name = name
        self.speciality = speciality  # Example:"Fern-tastic", or None for general employee

    def __str__(self):
        """
        This method return a string representation of the florist.

        This method is used when printing staff names list.
        If the florist has a speciality, it is shown in brackets
        after their name.

        Returns:
            str :
                The formatted name of the florist, including their
                speciality if one exists.

        """
        if self.speciality:
            return f"{self.name} ({self.speciality})"
        return self.name
