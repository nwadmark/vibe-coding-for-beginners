# A/B Test Sample Size Calculator
# Calculates how many visitors you need and how long to run the test.
# Uses the math module only — no scipy or numpy required.

import math

# Z-scores for common confidence levels (two-tailed test)
# These come from the standard normal distribution table
Z_SCORES = {90: 1.645, 95: 1.96, 99: 2.576}

# Z-score for 80% statistical power (industry standard)
Z_BETA = 0.84


def get_float(prompt):
    """Ask for a number. Keep asking until valid."""
    while True:
        try:
            value = float(input(prompt))
            if value > 0:
                return value
            print("   Enter a positive number.")
        except ValueError:
            print("   That's not a valid number.")


def get_confidence():
    """Ask for confidence level — must be 90, 95, or 99."""
    while True:
        try:
            value = int(input("  Confidence level (90/95/99): "))
            if value in Z_SCORES:
                return value
            print("   Enter 90, 95, or 99.")
        except ValueError:
            print("   Enter 90, 95, or 99.")


def calculate_sample_size(baseline, mde, confidence):
    """
    Calculate required sample size per variant.
    Formula: n = (Z_alpha + Z_beta)^2 * (p1(1-p1) + p2(1-p2)) / (p2-p1)^2
    where p1 = baseline rate, p2 = baseline + minimum detectable effect.
    """
    p1 = baseline / 100
    p2 = (baseline + mde) / 100
    z_alpha = Z_SCORES[confidence]

    numerator = (z_alpha + Z_BETA) ** 2 * (p1 * (1 - p1) + p2 * (1 - p2))
    denominator = (p2 - p1) ** 2

    return math.ceil(numerator / denominator)


def main():
    print("━" * 50)
    print("  A/B TEST SAMPLE SIZE CALCULATOR")
    print("  Plan your experiment before you ship it")
    print("━" * 50)

    while True:
        print()
        baseline = get_float("  Baseline conversion rate (%): ")
        mde = get_float("  Minimum detectable effect (%): ")
        confidence = get_confidence()
        traffic = get_float("  Daily traffic (visitors per day): ")

        per_variant = calculate_sample_size(baseline, mde, confidence)
        total = per_variant * 2
        days = math.ceil(total / traffic)
        relative_lift = mde / baseline * 100

        print()
        print("━" * 50)
        print("  TEST PLAN")
        print("━" * 50)
        print(f"  Baseline rate:     {baseline:.2f}%")
        print(f"  Target rate:       {baseline + mde:.2f}%")
        print(f"  Relative lift:     {relative_lift:.1f}%")
        print()
        print(f"  Sample needed:     ~{per_variant:,} per variant")
        print(f"  Total visitors:    ~{total:,} across both variants")
        print(f"  Estimated time:    ~{days} days")
        print()
        print(f"  ℹ️  At {confidence}% confidence, if the true effect is {mde}%")
        print(f"  or larger, this test has ~80% power to detect it.")
        print("━" * 50)

        again = input("\nRun another calculation? (yes/no): ").strip().lower()
        if again not in ("yes", "y"):
            break


if __name__ == "__main__":
    main()
