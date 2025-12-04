# flowershop.py
# Author: Jitendra Suwalka
# Section: Data Science Course: SDPA_EMATM0048
# Description: The FlowerShop class represents all aspects of the flower shop business;
#              including staff, inventory, orders and how many bouquets are allocated
#              to which florists.

from florist import Florist
from inventory import CAPACITY, apply_depreciation, greenhouse_storage_cost, restock_to_capacity
from orders import collect_orders, check_supplies_for_order
from staff import print_staff_list, hire_interactive, remove_interactive
from utils import get_valid_integer, get_yes_no_input
from allocation import allocate_bouquets_among_florists


class FlowerShop:
    """
    A high level model of the flower shop business.

    This class contains the florists and inventory and has
    a number of helper methods available to be called by the
    main simulation loop each month to advance the simulation.

    """

    # Types of bouquets and maximum demand/prices per bouquet
    BOUQUET_TYPES = ["Fern-tastic", "Be-Leaf in Yourself", "You Rose to the Occasion"]
    MAX_DEMAND = {
        "Fern-tastic": 175,
        "Be-Leaf in Yourself": 100,
        "You Rose to the Occasion": 250,
    }
    PRICES = {
        "Fern-tastic": 18.50,
        "Be-Leaf in Yourself": 17.75,
        "You Rose to the Occasion": 32.50,
    }

    EMPLOYEE_HOURLY = 15.50
    EMPLOYEE_MONTH_HOURS = 80
    EMPLOYEE_MONTH_COST = EMPLOYEE_HOURLY * EMPLOYEE_MONTH_HOURS  # 1240

    RENT = 800.0

    # Supply usage per bouquet (bunches) of flowers
    SUPPLY_USAGE = {
        "Fern-tastic": {"roses": 0, "daisies": 2, "greenery": 4},
        "Be-Leaf in Yourself": {"roses": 1, "daisies": 3, "greenery": 2},
        "You Rose to the Occasion": {"roses": 4, "daisies": 2, "greenery": 2},
    }

    def __init__(self):
        """
        Creates a new FlowerShop object based on the given parameters; 
        including initial cash balance, an empty list of florists and a 
        full greenhouse inventory.

        """
        self.cash_balance = 7500.0
        self.florists: list[Florist] = []
        self.inventory = {
            "roses": CAPACITY["roses"],
            "daisies": CAPACITY["daisies"],
            "greenery": CAPACITY["greenery"],
        }

    # Staff wrappers
    def hire_florists(self, new_list):
        """
        Add one or more Florist objects to the FlowerShop's
        list of florists.

        Args:
            new_list::list[Florist]
                The newly employed florists.
        """
        for f in new_list:
            self.florists.append(f)

    def remove_by_name(self, name):
        """
        Remove a Florist object from the FlowerShop's list of
        florists by their name.

        Args:
            name::str
                The name of the florist to remove (case-insensitive).

        Returns:
            bool
                If a florist was found and removed, returns True.
                Otherwise returns False.
        """
        for f in self.florists:
            if f.name.lower() == name.lower():
                self.florists.remove(f)
                return True
        return False

    def run_month_production(self, orders):
        """
        Run the production partion of the month and update the FloweShop's inventory.

        Allocation process is used to:
        - Apply speciality rules.
        - Enforce the 80-hour work limit per florist per month.
        - Allocate orders evenly among staff
        Subtracts the ingredients used to create bouquets from the inventory.

        Args:
            orders::dict[str, int]
                The number of bouquets of each type ordered

        Returns:
            tuple:
                income::float
                    The total revenue generated during this month.
                revenue_by_florist::dict[str, float]
                    Each florist's contribution to revenue.
                bouquets_by_florist::dict[str, dict[str, int]]
                    The number of bouquets each florist produced by type.
                unmet::dict[str, int]
                    Number of unmet bouquet orders because there wasn't enough labor.
        """
        total_income, revenue_by_florist, bouquets_by_florist, unmet = \
            allocate_bouquets_among_florists(orders, self.florists)

        # Reduces inventory by amount of ingredients required to produce bouquets 
        # and the actual amount of bouquets produced.
        for florist_name, bmap in bouquets_by_florist.items():
            for btype, qty in bmap.items():
                if qty <= 0:
                    continue
                usage = self.SUPPLY_USAGE[btype]
                for flower, bunches_used in usage.items():
                    self.inventory[flower] -= qty * bunches_used
                    if self.inventory[flower] < 0:
                        self.inventory[flower] = 0

        return total_income, revenue_by_florist, bouquets_by_florist, unmet

    def monthly_employee_cost(self):
        """
        Calculates the fixed salary costs for all florists for the month.

        Returns:
            float
                Total cost of all florists for the month.
        """
        return len(self.florists) * self.EMPLOYEE_MONTH_COST

    def monthly_greenhouse_cost(self):
        """
        Calculate the total cost of the greenhouse storage for the current inventory.

        Returns:
            float
                Total greenhouse cost for this month.
        """
        return greenhouse_storage_cost(self.inventory)

    def apply_depreciation(self):
        """
        Apply depreciation of flower bunches to the currently available inventory .

        This is a small wrapper for the inventory.apply_depreciation
        function for conveniencesimple use.
        """
        apply_depreciation(self.inventory)
