# RICE Feature Prioritizer
# Rank features using the RICE framework: Reach, Impact, Confidence, Effort.
# No external libraries needed — runs on Python built-ins only.

def get_number(prompt, allow_float=False):
    """Ask for a number. Keep asking until the user gives a valid one."""
    while True:
        try:
            value = float(input(prompt)) if allow_float else int(input(prompt))
            if value > 0:
                return value
            print("   Please enter a positive number.")
        except ValueError:
            print("   That's not a valid number. Try again.")


def get_impact():
    """Ask for Impact on a 1-3 scale with labels."""
    while True:
        try:
            value = int(input("  Impact (1=minimal, 2=medium, 3=massive): "))
            if value in (1, 2, 3):
                return value
            print("   Enter 1, 2, or 3.")
        except ValueError:
            print("   Enter 1, 2, or 3.")


def get_confidence():
    """Ask for Confidence as a decimal between 0 and 1."""
    while True:
        try:
            value = float(input("  Confidence (0.0 to 1.0): "))
            if 0 < value <= 1.0:
                return value
            print("   Enter a value between 0.0 and 1.0.")
        except ValueError:
            print("   Enter a decimal like 0.8 or 0.5.")


def main():
    print("━" * 50)
    print("  RICE FEATURE PRIORITIZER")
    print("  Rank features by Reach, Impact, Confidence, Effort")
    print("━" * 50)

    features = []

    while True:
        print()
        name = input("Feature name: ")
        reach = get_number("  Reach (users affected per quarter): ")
        impact = get_impact()
        confidence = get_confidence()
        effort = get_number("  Effort (person-weeks): ", allow_float=True)

        # RICE formula: (Reach × Impact × Confidence) / Effort
        rice = (reach * impact * confidence) / effort
        print(f"  → RICE Score: {rice:.1f}")

        features.append({"name": name, "rice": rice})

        again = input("\nAdd another feature? (yes/no): ").strip().lower()
        if again not in ("yes", "y"):
            break

    # Sort by RICE score, highest first
    features.sort(key=lambda f: f["rice"], reverse=True)

    # Display the ranked table
    print()
    print("RANKED FEATURES")
    print("━" * 50)
    print(f" {'Rank':<6}{'Feature':<22}{'RICE Score':>10}")
    print("━" * 50)
    for i, feat in enumerate(features, 1):
        print(f"  {i}.   {feat['name']:<22}{feat['rice']:>8.1f}")
    print("━" * 50)
    print(f"🏆 Top priority: {features[0]['name']}")
    print("━" * 50)


if __name__ == "__main__":
    main()
