# Task Priority Scorer

def assign_priority(task):
    deadline = task.get("deadline")  # safely handles missing key
    
    if deadline is None:
        return "Unknown"  # no deadline provided
    elif deadline == "today":
        return "High"
    elif deadline == "this week":
        return "Medium"
    else:
        return "Low"
