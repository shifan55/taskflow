def predict_priority(task):
    return "high" if len(task) > 10 else "low"
