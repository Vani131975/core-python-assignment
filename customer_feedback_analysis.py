def calculate_positive_feedback_percentage(ratings):
    if not ratings:
        return 0.0
    positive_count = 0
    for rating in ratings:
        if rating >= 4:
            positive_count += 1
    total_count = len(ratings)
    return (positive_count / total_count) * 100
ratings = list(map(int, input("Enter the ratings: ").split(",")))
positive_feedback_percentage = calculate_positive_feedback_percentage(ratings)
print(f"Positive Feedback: {positive_feedback_percentage:.1f}%")