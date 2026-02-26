import os
import csv

from instant_refactor import refactor_instant
from medium_refactor import refactor_medium
from high_refactor import refactor_high
from syntax_sanitizer import sanitize_incomplete_blocks
from metrics import cyclomatic_complexity, line_count, pylint_score


INPUT_DIR = "data/input"
OUTPUT_DIR = "data/output"
RESULT_FILE = "experiments/results.csv"

os.makedirs("data/output/instant", exist_ok=True)
os.makedirs("data/output/thinking_medium", exist_ok=True)
os.makedirs("data/output/thinking_xhigh", exist_ok=True)
os.makedirs("experiments", exist_ok=True)


def evaluate(filepath):
    with open(filepath, "r", encoding="utf-8") as f:
        code = f.read()

    return (
        line_count(code),
        cyclomatic_complexity(code),
        pylint_score(filepath),
    )


with open(RESULT_FILE, mode="w", newline="", encoding="utf-8") as csvfile:
    writer = csv.writer(csvfile)

    writer.writerow([
        "Module",
        "Level",
        "Lines",
        "Complexity",
        "Pylint"
    ])

    for filename in os.listdir(INPUT_DIR):
        if not filename.endswith(".py"):
            continue

        input_path = os.path.join(INPUT_DIR, filename)

        with open(input_path, "r", encoding="utf-8") as f:
            code = f.read()

        code = sanitize_incomplete_blocks(code)

        # ----- BASELINE -----
        lines, complexity, pylint_val = evaluate(input_path)
        writer.writerow([filename, "Baseline", lines, complexity, pylint_val])

        # ----- INSTANT -----
        instant_code = refactor_instant(code)
        instant_path = os.path.join("data/output/instant", filename)

        with open(instant_path, "w", encoding="utf-8") as f:
            f.write(instant_code)

        lines, complexity, pylint_val = evaluate(instant_path)
        writer.writerow([filename, "Instant", lines, complexity, pylint_val])

        # ----- MEDIUM -----
        medium_code = refactor_medium(code)
        medium_path = os.path.join("data/output/thinking_medium", filename)

        with open(medium_path, "w", encoding="utf-8") as f:
            f.write(medium_code)

        lines, complexity, pylint_val = evaluate(medium_path)
        writer.writerow([filename, "Medium", lines, complexity, pylint_val])

        # ----- HIGH -----
        high_code = refactor_high(code)
        high_path = os.path.join("data/output/thinking_xhigh", filename)

        with open(high_path, "w", encoding="utf-8") as f:
            f.write(high_code)

        lines, complexity, pylint_val = evaluate(high_path)
        writer.writerow([filename, "High", lines, complexity, pylint_val])

        print(f"Processed {filename}")

print("Full experiment completed.")