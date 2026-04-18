def performance(score):
    if score >= 70:
        return "Good"
    elif score >= 50:
        return "Average"
    else:
        return "Poor"

score = int(input("Enter score: "))
print (performance(score))