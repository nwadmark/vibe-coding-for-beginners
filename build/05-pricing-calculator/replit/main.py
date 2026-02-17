# Pricing & Revenue Calculator
# Model pricing tiers and calculate MRR/ARR with revenue breakdown.
# No external libraries needed — runs on Python built-ins only.

def get_int(prompt):
    """Ask for a whole number. Keep asking until valid."""
    while True:
        try:
            value = int(input(prompt))
            if value > 0:
                return value
            print("   Enter a positive number.")
        except ValueError:
            print("   That's not a valid number.")


def get_float(prompt):
    """Ask for a number (allows decimals). Keep asking until valid."""
    while True:
        try:
            value = float(input(prompt))
            if value > 0:
                return value
            print("   Enter a positive number.")
        except ValueError:
            print("   That's not a valid number.")


def main():
    print("━" * 50)
    print("  PRICING & REVENUE CALCULATOR")
    print("  Model your tiers, see your revenue")
    print("━" * 50)

    while True:
        # Get tier count
        while True:
            try:
                num_tiers = int(input("\nHow many pricing tiers? (1-5): "))
                if 1 <= num_tiers <= 5:
                    break
                print("  Enter a number between 1 and 5.")
            except ValueError:
                print("  Enter a number between 1 and 5.")

        tiers = []
        for i in range(num_tiers):
            print(f"\nTier {i + 1}:")
            name = input("  Name: ")
            price = get_float("  Monthly price ($): ")
            customers = get_int("  Number of customers: ")
            tiers.append({"name": name, "price": price, "customers": customers})

        # Calculate MRR per tier and total
        total_mrr = 0
        for tier in tiers:
            tier["mrr"] = tier["price"] * tier["customers"]
            total_mrr += tier["mrr"]

        # Display revenue breakdown table
        print()
        print("REVENUE BREAKDOWN")
        print("━" * 54)
        print(f"  {'Tier':<14} {'Price':>6} {'Customers':>10} {'MRR':>10} {'Share':>8}")
        print("━" * 54)

        for tier in tiers:
            share = tier["mrr"] / total_mrr * 100 if total_mrr > 0 else 0
            print(
                f"  {tier['name']:<14}"
                f" ${tier['price']:>5,.0f}"
                f" {tier['customers']:>9}"
                f" ${tier['mrr']:>8,.0f}"
                f" {share:>6.1f}%"
            )

        print("━" * 54)

        # Totals
        total_customers = sum(t["customers"] for t in tiers)
        arr = total_mrr * 12

        print()
        print("TOTALS")
        print(f"  Customers:     {total_customers:,}")
        print(f"  MRR:           ${total_mrr:,.0f}")
        print(f"  ARR:           ${arr:,.0f}")
        print("━" * 54)

        again = input("\nModel another scenario? (yes/no): ").strip().lower()
        if again not in ("yes", "y"):
            break


if __name__ == "__main__":
    main()
