from metrics import cyclomatic_complexity, line_count, pylint_score

BASELINE = "data/input/legacy_module_1.py"
INSTANT = "data/output/instant/legacy_module_1.py"
MEDIUM = "data/output/thinking_medium/legacy_module_1.py"
HIGH = "data/output/thinking_xhigh/legacy_module_1.py"


def evaluate(filepath):
    with open(filepath, "r", encoding="utf-8") as f:
        code = f.read()

    return {
        "Lines": line_count(code),
        "Complexity": cyclomatic_complexity(code),
        "Pylint": pylint_score(filepath)
    }


print("===== BASELINE =====")
print(evaluate(BASELINE))

print("\n===== INSTANT =====")
print(evaluate(INSTANT))

print("\n===== MEDIUM =====")
print(evaluate(MEDIUM))

print("\n===== HIGH =====")
print(evaluate(HIGH))