import ast
import os
import pandas as pd

def extract_variables_and_functions(file_path):
    with open(file_path, "r") as f:
        tree = ast.parse(f.read(), filename=file_path)

    variables = set()
    functions = set()

    for node in ast.walk(tree):
        if isinstance(node, ast.Name) and isinstance(node.ctx, ast.Store):
            variables.add(node.id)
        elif isinstance(node, ast.FunctionDef):
            functions.add(node.name)

    return variables, functions

def generate_report(code1_vars, code1_funcs, code2_vars, code2_funcs):
    report = {
        "File": ["code1.py", "code2.py"],
        "Variables": [", ".join(code1_vars), ", ".join(code2_vars)],
        "Functions": [", ".join(code1_funcs), ", ".join(code2_funcs)],
    }

    common_vars = code1_vars.intersection(code2_vars)
    common_funcs = code1_funcs.intersection(code2_funcs)

    df = pd.DataFrame(report)
    summary = pd.DataFrame({
        "Type": ["Common Variables", "Common Functions"],
        "Values": [", ".join(common_vars), ", ".join(common_funcs)]
    })

    # Save both reports to Excel
    with pd.ExcelWriter("code_analysis_report.xlsx") as writer:
        df.to_excel(writer, sheet_name="File Overview", index=False)
        summary.to_excel(writer, sheet_name="Conflicts & Redundancy", index=False)

    print("✅ Report generated: code_analysis_report.xlsx")

# Define paths (assuming files are in the same folder)
code1_path = "code1.py"
code2_path = "code2.py"

# Extract details
code1_vars, code1_funcs = extract_variables_and_functions(code1_path)
code2_vars, code2_funcs = extract_variables_and_functions(code2_path)

# Generate report
generate_report(code1_vars, code1_funcs, code2_vars, code2_funcs)
