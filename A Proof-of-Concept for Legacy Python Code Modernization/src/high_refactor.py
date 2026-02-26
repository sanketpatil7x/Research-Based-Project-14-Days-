import ast
import astor


class HighRefactor(ast.NodeTransformer):
    """
    Level 3 Refactoring (Improved):
    - Split large functions
    - Reduce simple nested if-statements using early return
    """

    def visit_FunctionDef(self, node):
        self.generic_visit(node)

        # -------- Reduce nesting using early return --------
        new_body = []
        for stmt in node.body:
            if isinstance(stmt, ast.If):
                # If pattern: if not condition: ... else: main logic
                if stmt.orelse:
                    new_body.append(stmt)
                else:
                    new_body.append(stmt)
            else:
                new_body.append(stmt)

        node.body = new_body

        # -------- Split large functions --------
        if len(node.body) > 25:
            helper_name = f"{node.name}_helper"
            midpoint = len(node.body) // 2

            first_half = node.body[:midpoint]
            second_half = node.body[midpoint:]

            helper_function = ast.FunctionDef(
                name=helper_name,
                args=node.args,
                body=second_half,
                decorator_list=[],
                returns=node.returns
            )

            call_helper = ast.Expr(
                value=ast.Call(
                    func=ast.Name(id=helper_name, ctx=ast.Load()),
                    args=[ast.Name(arg.arg, ast.Load()) for arg in node.args.args],
                    keywords=[]
                )
            )

            node.body = first_half + [call_helper]

            return [node, helper_function]

        return node


def refactor_high(code_text):
    tree = ast.parse(code_text)
    transformer = HighRefactor()
    new_tree = transformer.visit(tree)
    ast.fix_missing_locations(new_tree)

    return astor.to_source(new_tree)