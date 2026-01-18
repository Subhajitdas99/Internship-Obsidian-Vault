import ast
import sys
from pathlib import Path


def analyze_file(file_path):
    code = Path(file_path).read_text()
    tree = ast.parse(code)

    classes = []
    functions = []

    # 🔹 New: structured call graph
    call_graph = {}

    current_class = None

    for node in ast.walk(tree):

        # Track class context
        if isinstance(node, ast.ClassDef):
            classes.append(node.name)
            current_class = node.name

        # Track functions and calls INSIDE them
        if isinstance(node, ast.FunctionDef):
            functions.append(node.name)

            # Build fully qualified caller name
            if current_class:
                caller_name = f"{current_class}.{node.name}"
            else:
                caller_name = node.name

            call_graph.setdefault(caller_name, [])

            # Walk inside function body
            for inner_node in ast.walk(node):
                if isinstance(inner_node, ast.Call):

                    called_function = None

                    # helper()
                    if isinstance(inner_node.func, ast.Name):
                        called_function = inner_node.func.id

                    # self.calculate_tax()
                    elif isinstance(inner_node.func, ast.Attribute):
                        called_function = inner_node.func.attr

                    if called_function:
                        # Build callee name (best-effort)
                        if current_class:
                            callee_name = f"{current_class}.{called_function}"
                        else:
                            callee_name = called_function

                        if callee_name not in call_graph[caller_name]:
                            call_graph[caller_name].append(callee_name)

    # ---------- Output ----------
    print("\n📄 File analyzed:", file_path)
    print("📦 Classes found:", classes)
    print("🔧 Functions found:", functions)

    print("\n📊 Call Graph")
    for caller, callees in call_graph.items():
        print(caller)
        for callee in callees:
            print(f"  └── {callee}")

    total_calls = sum(len(v) for v in call_graph.values())
    print(f"\n📊 Summary: {len(classes)} classes, {len(functions)} functions, {total_calls} calls\n")


if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python analyzer.py <python_file>")
        sys.exit(1)

    analyze_file(sys.argv[1])



