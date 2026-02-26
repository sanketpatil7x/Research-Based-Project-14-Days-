import subprocess
from radon.complexity import cc_visit


def cyclomatic_complexity(code_text):
    """
    Returns total cyclomatic complexity of a Python file.
    """
    blocks = cc_visit(code_text)
    return sum(block.complexity for block in blocks)


def line_count(code_text):
    """
    Returns total number of lines.
    """
    return len(code_text.splitlines())


def pylint_score(filepath):
    """
    Returns pylint score (0–10).
    """
    result = subprocess.run(
        ["pylint", filepath, "--score=y"],
        capture_output=True,
        text=True
    )

    for line in result.stdout.split("\n"):
        if "rated at" in line:
            score = line.split("rated at")[1].split("/")[0].strip()
            try:
                return float(score)
            except:
                return None

    return None