import re

def sanitize_incomplete_blocks(code_text):
    lines = code_text.splitlines()
    sanitized = []
    indent_stack = []

    for i, line in enumerate(lines):
        sanitized.append(line)

        stripped = line.strip()

        # Detect block starters
        if stripped.endswith(":"):
            next_line = ""
            if i + 1 < len(lines):
                next_line = lines[i + 1].strip()

            # If next line is empty OR dedented OR another block
            if next_line == "" or next_line.startswith(("elif", "else", "except", "finally")):
                indent = len(line) - len(line.lstrip())
                sanitized.append(" " * (indent + 4) + "pass")

    return "\n".join(sanitized)