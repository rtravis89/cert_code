# Steps
# 1. split string into components
# 2. arrange components vertically
# 3. right align components
## string format starts at left most character, so start position is total length of line - length of number
# 4. create dash line (-) with length = max(nums) + 2, 1 empty spot and 1 for '+'


test_list = ["32 + 698","3801 - 2", "45 + 43", "123 + 49", "1 + 1", "1 + 3"]
answers = True

# format each problem and store in a list

if len(test_list) > 5:
    raise ValueError("Error: Too many problems.")
output_list = []
for i in range(len(test_list)):
    x = test_list[i].split()
    if x[1] == '+':
        ans = int(x[0]) + int(x[2])
    if x[1] == '-':
        ans = int(x[0]) - int(x[2])    
    line_length = len(max(x, key = len)) + 2
    num1_format = '{:>' + str(line_length) + '}'
    num2_format = '{:>' + str(line_length - 2) + '}'
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
'\n'.join(row_list)
print('\n'.join(row_list))







