"""Using filter and lambda to select list values."""

scores = [45, 67, 90, 38, 76, 59]

# Here is filter with lambda to keep passing scores.
passing_scores = list(filter(lambda score: score >= 50, scores))

print(passing_scores)
