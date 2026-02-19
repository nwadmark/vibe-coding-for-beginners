# Decision Framework Tool
# For use in Cursor or local Python environment
# Run: python main.py

# A command-line tool for PMs to score and evaluate feature ideas.
# Uses a weighted formula to turn gut feelings into structured decisions.
# No external libraries needed — runs on Python built-ins only.

# ── Helper functions ─────────────────────────────────────────────────

def get_score(prompt):
    """Ask the user for a 1-10 score. Keep asking until they give a valid number."""
    while True:
        try:
            value = int(input(prompt))
            if 1 <= value <= 10:
                # Show a label so the user gets instant feedback on their choice
                label = "Low" if value <= 3 else "Medium" if value <= 6 else "High" if value <= 9 else "Maximum"
                print(f"   → {label}")
                return value
            print("   Please enter a number between 1 and 10.")
        except ValueError:
            print("   That's not a number. Enter a value from 1 to 10.")


def draw_bar(label, score, width=18):
    """Draw a single ASCII bar like: Customer Value    ████████░░  8/10"""
    filled = "█" * score
    empty = "░" * (10 - score)
    # Pad the label so all bars line up neatly in a column
    print(f"  {label:<{width}} {filled}{empty}  {score}/10")


def calculate_score(customer, effort, alignment, confidence):
    """
    Weighted formula that balances value against effort.
    Customer Value counts double because user impact matters most.
    Strategic Alignment gets 1.5x because roadmap fit matters.
    Confidence is 1x — it tempers the score when we're guessing.
    Effort is the denominator — harder features need higher value to justify.
    The ×10 scales the result into a readable range (roughly 0-25).
    """
    return (customer * 2 + alignment * 1.5 + confidence * 1) / effort * 10


def get_recommendation(score):
    """Turn the numeric score into a decision with emoji and action step."""
    if score > 15:
        decision = "🟢 Strong Go — Prioritize this"
        action = "📌 Suggested action: Add to next sprint backlog"
    elif score >= 10:
        decision = "🟡 Maybe — Needs more validation"
        action = "🔍 Suggested action: Schedule discovery session"
    else:
        decision = "🔴 No Go — Deprioritize or kill"
        action = "📁 Suggested action: Document reasoning and archive"
    return decision, action


# ── Main loop ────────────────────────────────────────────────────────

def evaluate_feature():
    """Run one full evaluation cycle: gather scores, calculate, display results."""
    print()
    feature = input("Describe the feature idea: ")
    print()

    # Gather the four criteria scores
    customer = get_score("  Customer Value (1-10): ")
    effort = get_score("  Implementation Effort (1-10): ")
    alignment = get_score("  Strategic Alignment (1-10): ")
    confidence = get_score("  Confidence (1-10): ")

    # Crunch the numbers
    score = calculate_score(customer, effort, alignment, confidence)
    decision, action = get_recommendation(score)

    # ── Display results ──────────────────────────────────────────
    print()
    print("━" * 50)
    print(f"  Feature: {feature}")
    print(f"  Score:   {score:.1f}")
    print(f"  Result:  {decision}")
    print("━" * 50)

    # Score breakdown — shows how each criterion contributed to the total
    print()
    print("  Score Breakdown:")
    print(f"    Customer Value × 2    = {customer * 2}")
    print(f"    Strategic Align × 1.5 = {alignment * 1.5:.1f}")
    print(f"    Confidence × 1        = {confidence}")
    print(f"    ÷ Effort ({effort})         = {score:.1f}")
    print()

    # Visual bar chart — makes it easy to spot which scores are high or low
    draw_bar("Customer Value", customer)
    draw_bar("Effort (impact)", effort)
    draw_bar("Strategic Align", alignment)
    draw_bar("Confidence", confidence)
    print()

    # Risk flag — high-effort features deserve extra scrutiny
    if effort > 7:
        print("  ⚠️  High effort — validate with engineering first")
        print()

    # PM action — gives a concrete next step so the evaluation leads to action
    print(f"  {action}")
    print("━" * 50)


def main():
    print("━" * 50)
    print("  PM DECISION FRAMEWORK")
    print("  Evaluate feature ideas with a weighted scorecard")
    print("━" * 50)

    while True:
        evaluate_feature()
        print()
        again = input("Evaluate another feature? (yes/no): ").strip().lower()
        if again not in ("yes", "y"):
            print()
            print("Done. Use your evaluations to drive the next planning session.")
            break
        # Separator between evaluations for readability
        print()
        print("─" * 50)


# ── Entry point ──────────────────────────────────────────────────────

if __name__ == "__main__":
    main()
