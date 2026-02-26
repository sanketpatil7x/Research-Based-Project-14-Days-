import ast
import astor


class InstantRefactor(ast.NodeTransformer):
    """
    Level 1 Refactoring:
    - Remove print() statements
    - Preserve block integrity
    """

    def visit_Expr(self, node):
        # Remove print() calls
        if isinstance(node.value, ast.Call):
            if isinstance(node.value.func, ast.Name):
                if node.value.func.id == "print":
                    return None
        return node


def ensure_non_empty_blocks(node):
    """
    Ensures that all blocks (if, for, while, function, class)
    have at least one statement.
    """
    for child in ast.walk(node):
        if hasattr(child, "body") and isinstance(child.body, list):
            if len(child.body) == 0:
                child.body.append(ast.Pass())
    return node


def refactor_instant(code_text):
    tree = ast.parse(code_text)

    transformer = InstantRefactor()
    new_tree = transformer.visit(tree)
    ast.fix_missing_locations(new_tree)

    new_tree = ensure_non_empty_blocks(new_tree)

    refactored_code = astor.to_source(new_tree)

    return refactored_code