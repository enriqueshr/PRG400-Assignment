# Sample list of exam scores
exam_scores = [45, 55, 75, 85, 95, 65, 35, 80]

# Filter out scores below 50
filtered_scores = list(filter(lambda score: score >= 50, exam_scores))

# Map to letter grades
def get_grade(score):
    if score >= 90:
        return 'A'
    elif score >= 80:
        return 'B'
    elif score >= 70:
        return 'C'
    elif score >= 60:
        return 'D'
    else:
        return 'E'

letter_grades = list(map(lambda score: get_grade(score), filtered_scores))

print("Original scores:", exam_scores)
print("Filtered scores (>= 50):", filtered_scores)
print("Letter grades:", letter_grades)