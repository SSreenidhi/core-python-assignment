"""6. Customer Feedback Analysis
Scenario:
A company collects customer feedback in the form of ratings (1-5). Write a program to calculate the **percentage of positive feedback** (4 or 5).
Requirements:
- Use a function to calculate the positive feedback percentage.
- Handle cases where no ratings are available.
Input Example:
```python
ratings = [5, 4, 3, 5, 2, 4, 1, 5]
```
Expected Output:
```
Positive Feedback: 62.5%
```
---"""


def calculate_positive_feedback(ratings):
    if not ratings:
        return "No ratings available."
    positive = len([rating for rating in ratings if rating >= 4])
    percentage = (positive / len(ratings)) * 100
    return f"Positive Feedback: {percentage}%"

ratings = [5, 4, 3, 5, 2, 4, 1, 5]
print(calculate_positive_feedback(ratings))
