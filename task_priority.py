# Task Priority Scorer

def assign_priority(tasks):
    if tasks["deadline"] == "today":
        return "High"
    elif tasks["deadline"] == "this week":
        return "Medium"
    else:
        return "Low"
