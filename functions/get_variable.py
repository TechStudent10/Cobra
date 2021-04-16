def get_variable(var_name, variables, line):
    text = ""
    if "'" in var_name or '"' in var_name:
        # for t in line:
        #     text += t + ' '
        text = ' '.join(line)
        text = text.replace("'" if text[0] == "'" else '"', '')
    elif var_name in variables:
        text = variables.get(var_name)
    else:
        variable_not_found(var_name)

    return text