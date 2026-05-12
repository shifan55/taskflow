# Task Priority Scorer

def assign_priority(task):
    deadline = task.get("deadline")
    
    if deadline is None:
        return "Unknown"
    elif deadline == "today":
        return "High"
    elif deadline == "this week":
        return "Medium"
    else:
        return "Low"


# CI check — runs automatically on every PR
if __name__ == "__main__":
    test1 = assign_priority({"deadline": "today"})
    assert test1 == "High", f"Expected High, got {test1}"

    test2 = assign_priority({"deadline": "this week"})
    assert test2 == "Medium", f"Expected Medium, got {test2}"

    test3 = assign_priority({})
    assert test3 == "Unknown", f"Expected Unknown, got {test3}"

    print("All tests passed! ✅")