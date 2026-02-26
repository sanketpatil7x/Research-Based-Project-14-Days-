import os
from instant_refactor import refactor_instant
from syntax_sanitizer import sanitize_incomplete_blocks

INPUT_FILE = "data/input/legacy_module_1.py"
OUTPUT_FILE = "data/output/instant/legacy_module_1.py"

os.makedirs("data/output/instant", exist_ok=True)

with open(INPUT_FILE, "r", encoding="utf-8") as f:
    code = f.read()
code = sanitize_incomplete_blocks(code)
refactored = refactor_instant(code)

with open(OUTPUT_FILE, "w", encoding="utf-8") as f:
    f.write(refactored)

print("Instant refactor completed.")