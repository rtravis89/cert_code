def arithmetic_arranger(problems, answers = False):
    """Takes in a list of arithmetic problems arranged horizontally
     and prints them vertically side by side."""

    if len(problems) > 5:
        return "Error: Too many problems."
    # format each problem and store in a list
    output_list = []
    for i in range(len(problems)):
        x = problems[i].split()
        if x[1] not in ['-','+']:
            return "Error: Operator must be '+' or '-'."
        if len(x[0]) > 4 or len(x[2]) > 4:
            return 'Error: Numbers cannot be more than four digits.'    
        try:
            int(x[0])    
            int(x[2])
        except ValueError:
            return "Error: Numbers must only contain digits."

        if x[1] == '+':
            ans = int(x[0]) + int(x[2])
        if x[1] == '-':
            ans = int(x[0]) - int(x[2])    
        line_length = len(max(x, key = len)) + 2
        num1_format = '{:>' + str(line_length) + '}'
        num2_format = "{:>" + str(line_length - 2) + '}'
        ans_format =  '{:>' + str(line_length) + '}'
        format_string = num1_format + '\n{:<} ' + num2_format
        if answers:
            complete_string = format_string.format(*x) + '\n' + '-' * line_length \
                + '\n' + ans_format.format(str(ans))
        else:
            complete_string = format_string.format(*x) + '\n' + '-' * line_length      

        output_list.append(complete_string)

# combine formatted problems into single string
    split_list = [x.split('\n') for x in output_list]
    row_list = ['    '.join(i) for i in list(zip(*split_list))]
    arranged_problems = '\n'.join(row_list)
    return arranged_problems