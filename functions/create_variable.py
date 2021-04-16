def create_variable(var_name, var_value, variables):
    text = ""

    if "'" in var_value or '"' in var_value:
        var_value = var_value.split(' ')
        text = ' '.join(var_value)
        text = text.replace("'" if text[0] == "'" else '"', '')
    elif var_value in variables:
        text = variables.get(var_value)
    else:
        variable_not_found(var_value)

    variables[var_name] = text