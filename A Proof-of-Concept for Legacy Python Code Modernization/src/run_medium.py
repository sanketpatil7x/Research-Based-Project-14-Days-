import os
from medium_refactor import refactor_medium
from syntax_sanitizer import sanitize_incomplete_blocks

INPUT_FILE = "data/input/legacy_module_1.py"
OUTPUT_FILE = "data/output/thinking_medium/legacy_module_1.py"

os.makedirs("data/output/thinking_medium", exist_ok=True)

with open(INPUT_FILE, "r", encoding="utf-8") as f:
    code = f.read()

code = sanitize_incomplete_blocks(code)
refactored = refactor_medium(code)

with open(OUTPUT_FILE, "w", encoding="utf-8") as f:
    f.write(refactored)

print("Medium refactor completed.")