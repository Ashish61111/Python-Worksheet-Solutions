def assign_grade(score):
    if score < 0 or score > 100:
        return "Invalid Score"
    elif score >= 90:
        return "A"
    elif score >= 80:
        return "B"
    elif score >= 70:
        return "C"
    elif score >= 60:
        return "D"
    else:
        return "F"

score1 = 95
score2 = 85
score3 = 75
score4 = 65
score5 = 50
score6 = 110

print("Score:", score1, "Grade:", assign_grade(score1))
print("Score:", score2, "Grade:", assign_grade(score2))
print("Score:", score3, "Grade:", assign_grade(score3))
print("Score:", score4, "Grade:", assign_grade(score4))
print("Score:", score5, "Grade:", assign_grade(score5))
print("Score:", score6, "Grade:", assign_grade(score6))