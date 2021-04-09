from functions import *

def execute_code(func_name, line, variables, index, lines, functions):
    if func_name == 'say':
        text = ""
        if "'" in line[0] or '"' in line[0]:
            for t in line:
                text += t + ' '
            text = text.replace("'" if "'" in t else '"', '')
        elif line[0] in variables:
            text = variables.get(line[0])
        else:
            variable_not_found(line[0])

        say(text)
    elif func_name == 'create_var':
        var_name = line[0]
        var_value = line[1]

        text = ""

        if "'" in var_value or '"' in var_value:
            var_value = var_value.split(' ')
            text = ' '.join(var_value)
            text = text.replace("'" if "'" in text else '"', '')
        elif var_value in variables:
            text = variables.get(var_value)
        else:
            variable_not_found(var_value)

        variables[var_name] = text
    elif func_name == 'create_function':
        function_name = line[0]
        current_lines = lines
        function_lines = []

        if not function_name.endswith(':'):
            syntax_error()

        function_name = function_name[:len(function_name) - 1]

        for current_line in current_lines:
            if current_line.startswith('    '):
                function_lines.append(current_line.replace('    ', ''))

        functions[function_name] = function_lines
    elif func_name in functions:
        function_lines = functions[func_name]
        
        for i in range(len(functions[func_name])):
            run_function(function_lines[i], variables, i, lines, functions)
    elif func_name == 'import':
        module_name = line[0]
        if not module_name.endswith('.cobra'):
            module_name += '.cobra'
        elif module_name.endswith('.cobra'):
            pass
        else:
            syntax_error()

        with open(module_name, 'r') as f:
            module_code = f.read()

        module_code = module_code.split('\n')
        for i in range(len(module_code)):
            run_main(module_code[0], variables, 0, module_code, functions)
    elif func_name == '' or func_name.startswith('#'):
        pass
    else:
        function_not_recognized(func_name)

def run_function(line, variables, index, lines, functions):
    line = line.split(' ')

    func_name = line[0]
    del line[0]

    execute_code(
        func_name,
        line,
        variables,
        index,
        lines,
        functions
    )

def run_main(line, variables, index, lines, functions):
    run_function(line, variables, index, lines, functions)
    del lines[index]
