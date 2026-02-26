import ast
import astor


class MediumRefactor(ast.NodeTransformer):
    """
    Level 2 Refactoring:
    - Add docstrings to functions that do not have one
    """

    def visit_FunctionDef(self, node):
        self.generic_visit(node)

        # If function has no docstring
        if not ast.get_docstring(node):
            docstring = ast.Expr(
                value=ast.Constant(
                    value=f"Auto-generated docstring for function '{node.name}'."
                )
            )
            node.body.insert(0, docstring)

        return node


def refactor_medium(code_text):
    tree = ast.parse(code_text)
    transformer = MediumRefactor()
    new_tree = transformer.visit(tree)
    ast.fix_missing_locations(new_tree)

    return astor.to_source(new_tree)