from . import get_variable

def run_python(string, variables, line, python_funcs_and_vars):
    # print("Running inside Python environment...")
    string = get_variable(string, variables, line)
    exec(string, python_funcs_and_vars)