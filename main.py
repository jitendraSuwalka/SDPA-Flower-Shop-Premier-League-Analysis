# main.py
# Author: Jitendra Suwalka
# Section: Data Science Course: SDPA_EMATM0048
# Description: Command-line entry point that runs the interactive
#              flower shop simulation for a chosen number of months.

from flowershop import FlowerShop
from staff import print_staff_list, hire_interactive, remove_interactive
from orders import collect_orders, check_supplies_for_order
from inventory import restock_to_capacity
from utils import yes_no


def main():
    """
    Run the full FlowerShop simulation.

    The player chooses how many months to simulate, hires or removes
    florists, chooses bouquet orders, restocks the greenhouse and
    observes how the cash balance changes over time.
    """
    shop = FlowerShop()
    print()
    print("==============================================")
    print()
    print("Welcome to the FlowerShop Simulator!")
    print()
    print("==============================================\n")

    # ❗ FIXED: Now EMPTY input shows warning instead of auto-starting Month 1
    while True:
        months_input = input("How many months would you like to run the game for? (Default 6): ").strip()

        if months_input == "":
            print("⚠️  Warning: You must enter a number between 1 and 6.")
            continue

        try:
            total_months = int(months_input)
            if 1 <= total_months <= 6:
                break
            else:
                print("Please enter a number between 1 and 6.")
        except ValueError:
            print("Please enter a valid whole number.")

    bankrupt = False

    for month in range(1, total_months + 1):
        print(f"\nMonth: {month}\n")
        print("Before the month starts, there are some owner actions for you to carry out.")
        print("First, review the number of staff, then decide how many bouquets to sell.\n")

        print(f"Current number of florists: {len(shop.florists)}")
        print(f"Current staff: {print_staff_list(shop.florists)}")

        # Hire
        newly_hired = hire_interactive(shop.florists)
        if newly_hired:
            shop.hire_florists(newly_hired)

        # Remove florists (start of month only)
        remove_interactive(shop.florists)

        print(f"\nCurrent staff: \n{' '*4}{print_staff_list(shop.florists)}\n")

        # Ask the player how many bouquets of each type they want to sell this month
        print("How much of each bouquet would you like to sell?")

        max_vals = [175, 100, 250]
        orders = collect_orders(FlowerShop.BOUQUET_TYPES, max_vals)

        # Check supplies
        ok, reason = check_supplies_for_order(
            orders, FlowerShop.SUPPLY_USAGE, shop.inventory
        )
        if not ok:
            print("This exceeds the available supplies. You must try again.")
            orders = collect_orders(FlowerShop.BOUQUET_TYPES, max_vals)
        #print("\n" + "=" * 50)
        #print("END OF MONTH SUMMARY".center(50))
        #print("=" * 50)
        
        # Speciality & labour engine
        #income, revenue_by_florist, bouquets_by_florist, unmet = \
         #   shop.run_month_production(orders)
        #print("\nFINANCIAL OVERVIEW")
        #print("-" * 50)

        #print(f"{' ' * 4}Cash Balance (Month Start) : £{shop.cash_balance:.2f}")
        #print(f"{' ' * 4}Income                     : £{income:.2f}\n")
        
        #employee_cost = shop.monthly_employee_cost()
        #greenhouse_cost = shop.monthly_greenhouse_cost()
        #rent = shop.RENT

        #print(f"{' ' * 4}Outgoings:")
        #print(f"{' ' * 8}Employee Costs   : £{employee_cost:.2f}")
        #print(f"{' ' * 8}Greenhouse Costs : £{greenhouse_cost:.2f}")
        #print(f"{' ' * 8}Rent             : £{rent:.2f}")
        
        # Depreciation (ceil-loss + integer stock)
        #shop.apply_depreciation()

        #print("\nCURRENT SHOP STATUS")
        #print("-" * 50)

        # ✅ Staff remains printed as a LIST (as you requested)
        #print(f"{' ' * 4}Current Staff:")
        #print(f"{' ' * 8}{print_staff_list(shop.florists)}")

        #print(f"\n{' ' * 4}Greenhouse Quantity:")
        #for k, v in shop.inventory.items():
         #   print(f"{' ' * 8}{k.capitalize():<10} : {v:.1f}")
        print("-" * 60)
        print("\nMonth in progress...\n")
        print("-" * 60)
        
         # Speciality & labour engine
        income, revenue_by_florist, bouquets_by_florist, unmet = \
            shop.run_month_production(orders)

         # Improve formatting and alignment of End of month calculations
        print("\nEnd of month calculations:\n")

        print(f"{' ' * 2}{'Cash Balance, Month Start':<28}: £{shop.cash_balance:.2f}")
        print(f"{' ' * 2}{'Income':<28}: £{income:.2f}")
        employee_cost = shop.monthly_employee_cost()
        greenhouse_cost = shop.monthly_greenhouse_cost()
        rent = shop.RENT
        print(f"{' ' * 2}Outgoings:")

        print(f"{' ' * 6}{'Employee costs':<22}: £{employee_cost:.2f}")
        print(f"{' ' * 6}{'Greenhouse costs':<22}: £{greenhouse_cost:.2f}")
        print(f"{' ' * 6}{'Rent':<22}: £{rent:.2f}\n")

       # Depreciation (ceil-loss + integer stock)
        shop.apply_depreciation()


        print("Current shop status:\n")

        print(f"{' ' * 4}Current staff:")
        print(f"{' ' * 8}{print_staff_list(shop.florists)}\n")

        print(f"{' ' * 4}Greenhouse quantity:")
        for k, v in shop.inventory.items():
            print(f"{' ' * 8}{k.capitalize():<10}: {v:.1f}")

        #print("=" * 50)

       # print("---------------------------------------------------------")
       #  print("\nMonth in progress...\n")

        # Speciality & labour engine
        #income, revenue_by_florist, bouquets_by_florist, unmet = \
        #    shop.run_month_production(orders)

        #print("---------------------------------------------------------\n")
        #print("End of month calculations:\n")
        #print(f"Cash Balance, Month Start: £{shop.cash_balance:.2f}")
        #print(f"{' '*4}Income: £{income:.2f}")

        #employee_cost = shop.monthly_employee_cost()
        #greenhouse_cost = shop.monthly_greenhouse_cost()
        #rent = shop.RENT

        #print(f"{' '*4}Outgoings:")
        #print(f"{' '*8}Employee costs: £{employee_cost:.2f}")
        #print(f"{' '*8}Greenhouse costs: £{greenhouse_cost:.2f}")
        #print(f"{' '*8}Rent: £{rent:.2f}\n")

        # Depreciation (ceil-loss + integer stock)
        #shop.apply_depreciation()

        #print("Current shop status:\n")
        #print(f"{' '*4}Current staff:\n{' '*8}{print_staff_list(shop.florists)}\n")
        #print(f"{' '*4}Greenhouse quantity:")
        #for k, v in shop.inventory.items():
         #   print(f"{' '*8}{k.capitalize()}: {v:.1f}")
        #print()

        # Restock for greenhouse
        print("The greenhouse has spare capacity and needs to be restocked...\n")
        if yes_no("Do you want to replenish your stock? (y/n): ") == "y":
            chosen = {}
            for flower in ["roses", "daisies", "greenery"]:
                while True:
                    print(
                        f"\nDo you want to purchase {flower} from Evergreen Essentials (0), or FloraGrow Distributors (1)?"
                    )
                    print("Press (i) if you would like to see price information.")
                    inp = input("Input: ").strip().lower()
                    if inp == "i":
                        print("\nSupplier Price List:")
                        print("-" * 20)

                        print(f"{' ' * 4}Evergreen Essentials")
                        print(f"{' ' * 8}Roses    : £2.80")
                        print(f"{' ' * 8}Daisies  : £1.50")
                        print(f"{' ' * 8}Greenery : £0.95\n")

                        print(f"{' ' * 4}FloraGrow Distributors")
                        print(f"{' ' * 8}Roses    : £1.60")
                        print(f"{' ' * 8}Daisies  : £1.20")
                        print(f"{' ' * 8}Greenery : £1.80\n")

                       # print("\nEvergreen Essentials -> roses £2.80 / daisies £1.50 / greenery £0.95")
                       # print("FloraGrow Distributors -> roses £1.60 / daisies £1.20 / greenery £1.80\n")
                        continue
                    if inp not in ("0", "1"):
                        print("Invalid option.")
                        continue
                    chosen[flower] = inp
                    break
            restock_cost = restock_to_capacity(shop.inventory, chosen)
            print(f"\n{' '*4}+ Flower restock costs: £{restock_cost:.2f}")
        else:
            restock_cost = 0.0

        shop.cash_balance += income - employee_cost - greenhouse_cost - rent - restock_cost
        
        # Show florist revenue contribution this month
        print("\nFlorist Revenue Contribution This Month:")
        print("-" * 40)

        for name, rev in revenue_by_florist.items():
            print(f"{' ' * 4}{name.capitalize():<12} :")
            print(f"{' ' * 8}Total Revenue = £{rev:.2f}")

        #print("\nFlorist revenue contribution this month:")
        #for name, rev in revenue_by_florist.items():
         #   print(f"      {name}: £{rev:.2f}")

        # Show bouquet production per florist
        print("\nBouquets Made By Each Florist:")
        print("-" * 30)

        for name, breakdown in bouquets_by_florist.items():
            print(f"{' ' * 4}{name.capitalize():<12} :")
            for bouquet_name in FlowerShop.BOUQUET_TYPES:
                qty = breakdown.get(bouquet_name, 0)
                print(f"{' ' * 8}{bouquet_name:<28} : {qty}")

       # print("\nBouquets made by each florist:")
        #for name, breakdown in bouquets_by_florist.items():
        #    parts = [f"{b}= {c}" for b, c in breakdown.items() if c > 0]
         #   if parts:
          #      print(f"      {name}: " + ", ".join(parts))
           # else:
            #    print(f"      {name}: 0 bouquets")
         
        print()
        print(f"\n{' '*4}End of month Cash Balance: £{shop.cash_balance:.2f}")
        print("\n=========================================================\n")

        if shop.cash_balance < 0:
            print("The shop has gone bankrupt! Simulation ending.")
            bankrupt = True
            break

    print("\n***************************************************************")
    print("Congratulations! You have completed the simulation!")
    print("***************************************************************")


if __name__ == "__main__":
    main()
