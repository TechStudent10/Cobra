from functions import *

def run_function(line):
    line = line.split(' ')

    func_name = line[0]

    if func_name == 'say':
        del line[0]
        text = ""
        for t in line:
            text += t + ' '
        
        say(text)
    elif func_name == '':
        pass
    else:
        function_not_recognized(func_name)