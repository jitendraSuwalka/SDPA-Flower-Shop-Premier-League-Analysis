# flowershop.py
# Author: Jitendra Suwalka
# Section: Data Science Course: SDPA_EMATM0048
# Description: Core FlowerShop class tying together staff, inventory,
#              orders and bouquet allocation.

from florist import Florist
from inventory import CAPACITY, apply_depreciation, greenhouse_storage_cost, restock_to_capacity
from orders import collect_orders, check_supplies_for_order
from staff import print_staff_list, hire_interactive, remove_interactive
from utils import safe_int, yes_no
from allocation import allocate_bouquets_among_florists


class FlowerShop:
    """
    High-level model of the flower shop business.

    This class owns the florists and inventory and provides helper
    methods used by the main simulation loop to progress each month.
    """

    # bouquet types and max demand/price
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

    # Supply usage per bouquet (bunches)
    SUPPLY_USAGE = {
        "Fern-tastic": {"roses": 0, "daisies": 2, "greenery": 4},
        "Be-Leaf in Yourself": {"roses": 1, "daisies": 3, "greenery": 2},
        "You Rose to the Occasion": {"roses": 4, "daisies": 2, "greenery": 2},
    }

    def __init__(self):
        """
        Initialise a new FlowerShop with starting cash, no staff and
        a full greenhouse inventory.
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
        Add new Florist objects to the shop's staff list.

        Args:
            new_list::list[Florist]
                Florists that have just been hired.
        """
        for f in new_list:
            self.florists.append(f)

    def remove_by_name(self, name):
        """
        Remove a florist from the staff list by name.

        Args:
            name::str
                Name of the florist to remove (case-insensitive).

        Returns:
            bool
                True if a matching florist was removed, False otherwise.
        """
        for f in self.florists:
            if f.name.lower() == name.lower():
                self.florists.remove(f)
                return True
        return False

    def run_month_production(self, orders):
        """
        Run the production part of the month and update inventory.

        This uses the allocation engine to:
        - Apply speciality rules.
        - Respect the 80-hour limit per florist.
        - Split orders fairly across staff.
        It then subtracts the ingredients consumed from the inventory.

        Args:
            orders::dict[str, int]
                Mapping from bouquet type to quantity ordered.

        Returns:
            tuple:
                income::float
                    Total sales revenue this month.
                revenue_by_florist::dict[str, float]
                    Revenue contribution per florist.
                bouquets_by_florist::dict[str, dict[str, int]]
                    How many bouquets each florist produced by type.
                unmet::dict[str, int]
                    Unfulfilled bouquet orders due to lack of labour.
        """
        total_income, revenue_by_florist, bouquets_by_florist, unmet = \
            allocate_bouquets_among_florists(orders, self.florists)

        # Reduce inventory according to SUPPLY_USAGE and bouquets actually made
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
        Compute the fixed monthly salary cost for all florists.

        Returns:
            float
                Total staff cost for the month.
        """
        return len(self.florists) * self.EMPLOYEE_MONTH_COST

    def monthly_greenhouse_cost(self):
        """
        Compute the greenhouse storage cost for the current inventory.

        Returns:
            float
                Total greenhouse cost for this month.
        """
        return greenhouse_storage_cost(self.inventory)

    def apply_depreciation(self):
        """
        Apply bunch depreciation to the current inventory in-place.

        This is a thin wrapper around the inventory.apply_depreciation
        function for convenience.
        """
        apply_depreciation(self.inventory)
