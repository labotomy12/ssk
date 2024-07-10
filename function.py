def evaluate_expression(expression):
    try:
        result = eval(expression)
        if isinstance(result, (int, float)):
            return "{:.2e}".format(result) if result > 1e12 or result < 1e-12 else str(result)
        return "Error"
    except Exception:
        return "Error"

def add_to_history(history, expression, result):
    history.append(f"{expression} = {result}")
    return history

def clear_history():
    return []
