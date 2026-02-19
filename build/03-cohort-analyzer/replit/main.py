# Cohort Retention Analyzer
# Reads user data from CSV, groups into weekly cohorts, calculates retention.
# Uses only Python built-ins (csv, datetime).

import csv
from datetime import datetime, timedelta


def load_users(filename):
    """Read the CSV and return a list of user dicts with parsed dates."""
    users = []
    with open(filename, newline="") as f:
        reader = csv.DictReader(f)
        for row in reader:
            users.append({
                "user_id": row["user_id"],
                "signup": datetime.strptime(row["signup_date"], "%Y-%m-%d"),
                "last_active": datetime.strptime(row["last_active_date"], "%Y-%m-%d"),
            })
    return users


def get_cohort_label(date):
    """Return a cohort label like '2024-W01' based on ISO week number."""
    iso = date.isocalendar()
    return f"{iso[0]}-W{iso[1]:02d}"


def build_cohorts(users):
    """Group users by their signup week and return a sorted dict of cohorts."""
    cohorts = {}
    for user in users:
        label = get_cohort_label(user["signup"])
        if label not in cohorts:
            cohorts[label] = []
        cohorts[label].append(user)
    return dict(sorted(cohorts.items()))


def calculate_retention(cohort_users, latest_date, max_weeks=5):
    """
    For each week 0..4, count what fraction of users were still active.
    A user is 'retained' in Week N if their last_active_date is at least
    N weeks after their signup_date. Week 0 is always 100%.
    Returns None for weeks where not enough time has passed.
    """
    total = len(cohort_users)
    if total == 0:
        return []

    earliest_signup = min(u["signup"] for u in cohort_users)
    weeks_available = (latest_date - earliest_signup).days // 7

    retention = []
    for week in range(max_weeks):
        if week > weeks_available:
            retention.append(None)
            continue
        retained = sum(
            1 for u in cohort_users
            if (u["last_active"] - u["signup"]).days >= week * 7
        )
        retention.append(round(retained / total * 100))
    return retention


def main():
    filename = "sample-data.csv"
    print(f"Reading {filename}...")

    try:
        users = load_users(filename)
    except FileNotFoundError:
        print(f"Error: {filename} not found. Place it in the same folder as this script.")
        return

    # Find the latest date in the dataset to know how many weeks of data exist
    latest_date = max(u["last_active"] for u in users)

    # Group users into weekly cohorts
    cohorts = build_cohorts(users)
    max_weeks = 5

    # Display the retention table
    print()
    print("COHORT RETENTION ANALYSIS")
    print("━" * 56)
    print(f"{'Cohort':<13}{'Users':>5}  {'Week0':>5}  {'Week1':>5}  {'Week2':>5}  {'Week3':>5}  {'Week4':>5}")
    print("━" * 56)

    all_retention = [[] for _ in range(max_weeks)]

    for label, cohort_users in cohorts.items():
        retention = calculate_retention(cohort_users, latest_date, max_weeks)
        row = f"{label:<13}{len(cohort_users):>5}"
        for w, pct in enumerate(retention):
            if pct is None:
                row += "     --"
            else:
                row += f"   {pct:>3}%"
                all_retention[w].append(pct)
        print(row)

    print("━" * 56)

    # Key insights
    print()
    print("KEY INSIGHTS")
    averages = []
    for w in range(max_weeks):
        if all_retention[w]:
            avg = sum(all_retention[w]) / len(all_retention[w])
            averages.append(avg)
            print(f"  Avg Week {w} retention: {avg:.0f}%")
        else:
            averages.append(None)

    # Find biggest drop between consecutive weeks
    biggest_drop = 0
    drop_week = 0
    for w in range(1, len(averages)):
        if averages[w] is not None and averages[w - 1] is not None:
            drop = averages[w - 1] - averages[w]
            if drop > biggest_drop:
                biggest_drop = drop
                drop_week = w
    if biggest_drop > 0:
        print(f"  Biggest drop: Week {drop_week - 1} → Week {drop_week} ({biggest_drop:.0f}% loss)")
    print("━" * 56)


if __name__ == "__main__":
    main()
