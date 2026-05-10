# Task Priority Scorer

def assign_priority(task):
    if task["deadline"] == "today":
        return "High"
    elif task["deadline"] == "this week":
        return "Medium"
    else:
        return "Low"
