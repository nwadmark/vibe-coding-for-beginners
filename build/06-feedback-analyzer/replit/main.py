# Feedback Sentiment Analyzer
# Reads user feedback from a text file and classifies sentiment using keywords.
# No external libraries needed — runs on Python built-ins only.

# Keyword lists for sentiment detection
# A line is positive if it contains any positive keyword, negative if it contains
# any negative keyword. If both match, the category with more matches wins.
# If neither matches, it's neutral.
POSITIVE_WORDS = {
    "love", "great", "awesome", "easy", "helpful", "excellent",
    "amazing", "fast", "intuitive", "perfect", "fantastic", "smooth",
}
NEGATIVE_WORDS = {
    "hate", "broken", "confusing", "slow", "frustrating", "terrible",
    "awful", "bug", "crash", "unusable", "painful", "horrible",
}


def classify(line):
    """Classify a feedback line as positive, neutral, or negative."""
    words = line.lower().split()
    pos_count = sum(1 for w in words if w.strip(".,!?;:'\"") in POSITIVE_WORDS)
    neg_count = sum(1 for w in words if w.strip(".,!?;:'\"") in NEGATIVE_WORDS)

    if pos_count > neg_count:
        return "positive"
    elif neg_count > pos_count:
        return "negative"
    elif pos_count > 0:
        # Equal positive and negative — default to neutral
        return "neutral"
    return "neutral"


def main():
    filename = "sample-feedback.txt"

    try:
        with open(filename) as f:
            lines = [line.strip() for line in f if line.strip()]
    except FileNotFoundError:
        print(f"Error: {filename} not found. Place it in the same folder as this script.")
        return

    # Sort feedback into buckets
    buckets = {"positive": [], "neutral": [], "negative": []}
    for line in lines:
        category = classify(line)
        buckets[category].append(line)

    total = len(lines)

    # Display results
    print()
    print("FEEDBACK SENTIMENT ANALYSIS")
    print("━" * 50)
    print(f"Total feedback items: {total}")

    for label, emoji in [("positive", "😊"), ("neutral", "😐"), ("negative", "😞")]:
        items = buckets[label]
        count = len(items)
        pct = count / total * 100 if total > 0 else 0
        print(f"\n{emoji} {label.title()}: {count} ({pct:.1f}%)")
        # Show up to 3 sample quotes
        for item in items[:3]:
            print(f'   "{item}"')

    print("━" * 50)


if __name__ == "__main__":
    main()
