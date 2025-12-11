def parse_token_as_number(token_str, var_storage):
    """Convert token to integer from variable or literal"""
    token_str = token_str.strip()
    if token_str.lstrip('-').isdigit():
        return int(token_str)
    return var_storage.get(token_str, 0)


def locate_else_or_terminator(instruction_list, start_position):
    """Search for else branch or block terminator at same nesting"""
    bracket_depth = 1
    current_index = start_position
    while current_index < len(instruction_list):
        instruction = instruction_list[current_index].strip()
        if instruction.startswith('if ') or instruction.startswith('for '):
            bracket_depth += 1
        elif instruction == 'end':
            bracket_depth -= 1
            if bracket_depth == 0:
                return current_index, 'end'
        elif instruction == 'No' and bracket_depth == 1:
            return current_index, 'No'
        current_index += 1
    return current_index, 'end'


def test_boolean_expression(expr, var_storage):
    """Check if conditional expression evaluates to true"""
    if '==' in expr:
        left_part, right_part = expr.split('==')
        left_result = parse_token_as_number(left_part.strip(), var_storage)
        right_result = parse_token_as_number(right_part.strip(), var_storage)
        return left_result == right_result
    elif '!=' in expr:
        left_part, right_part = expr.split('!=')
        left_result = parse_token_as_number(left_part.strip(), var_storage)
        right_result = parse_token_as_number(right_part.strip(), var_storage)
        return left_result != right_result
    elif '<=' in expr:
        left_part, right_part = expr.split('<=')
        left_result = parse_token_as_number(left_part.strip(), var_storage)
        right_result = parse_token_as_number(right_part.strip(), var_storage)
        return left_result <= right_result
    elif '>=' in expr:
        left_part, right_part = expr.split('>=')
        left_result = parse_token_as_number(left_part.strip(), var_storage)
        right_result = parse_token_as_number(right_part.strip(), var_storage)
        return left_result >= right_result
    elif '<' in expr:
        left_part, right_part = expr.split('<')
        left_result = parse_token_as_number(left_part.strip(), var_storage)
        right_result = parse_token_as_number(right_part.strip(), var_storage)
        return left_result < right_result
    elif '>' in expr:
        left_part, right_part = expr.split('>')
        left_result = parse_token_as_number(left_part.strip(), var_storage)
        right_result = parse_token_as_number(right_part.strip(), var_storage)
        return left_result > right_result
    return False


def jump_to_matching_closer(instruction_list, start_position):
    """Skip to the end marker that matches current block"""
    bracket_depth = 1
    current_index = start_position
    while current_index < len(instruction_list) and bracket_depth > 0:
        instruction = instruction_list[current_index].strip()
        if instruction.startswith('if ') or instruction.startswith('for '):
            bracket_depth += 1
        elif instruction == 'end':
            bracket_depth -= 1
        current_index += 1
    return current_index


def process_instructions(instruction_list, start_pos, stop_pos, var_storage):
    """Run through instruction list from start to stop position"""
    pointer = start_pos
    
    while pointer < stop_pos:
        current_instruction = instruction_list[pointer].strip()
        
        if not current_instruction or current_instruction == 'Yes' or current_instruction == 'No':
            pointer += 1
            continue
        
        if current_instruction == 'end':
            return pointer
        
        if current_instruction.startswith('print '):
            output_token = current_instruction[6:].strip()
            output_value = parse_token_as_number(output_token, var_storage)
            print(output_value)
            pointer += 1
        
        elif current_instruction.startswith('if '):
            condition_expr = current_instruction[3:].strip()
            pointer += 1
            
            if pointer < len(instruction_list) and instruction_list[pointer].strip() == 'Yes':
                pointer += 1
                true_branch_start = pointer
                
                else_position, branch_marker = locate_else_or_terminator(instruction_list, true_branch_start)
                
                if test_boolean_expression(condition_expr, var_storage):
                    process_instructions(instruction_list, true_branch_start, else_position, var_storage)
                    if branch_marker == 'No':
                        pointer = jump_to_matching_closer(instruction_list, else_position + 1)
                    else:
                        pointer = else_position + 1
                else:
                    if branch_marker == 'No':
                        false_branch_start = else_position + 1
                        block_terminator = jump_to_matching_closer(instruction_list, false_branch_start)
                        process_instructions(instruction_list, false_branch_start, block_terminator - 1, var_storage)
                        pointer = block_terminator
                    else:
                        pointer = else_position + 1
        
        elif current_instruction.startswith('for '):
            loop_components = current_instruction[4:].split()
            counter_var = loop_components[0]
            lower_bound = parse_token_as_number(loop_components[1], var_storage)
            upper_bound = parse_token_as_number(loop_components[2], var_storage)
            
            loop_body_start = pointer + 1
            loop_terminator = jump_to_matching_closer(instruction_list, loop_body_start) - 1
            
            for iteration_value in range(lower_bound, upper_bound + 1):
                var_storage[counter_var] = iteration_value
                process_instructions(instruction_list, loop_body_start, loop_terminator, var_storage)
            
            pointer = loop_terminator + 1
        
        else:
            pointer += 1
    
    return pointer


# Collect all input lines
input_lines = []
while True:
    try:
        current_line = input()
        input_lines.append(current_line)
    except EOFError:
        break

# Extract variable definitions from last two lines
variable_names = input_lines[-2].split()
variable_values = list(map(int, input_lines[-1].split()))

# Build variable dictionary
var_map = {}
for idx in range(len(variable_names)):
    var_map[variable_names[idx]] = variable_values[idx]

# Process program (excluding variable definitions)
program_code = input_lines[:-2]
process_instructions(program_code, 0, len(program_code), var_map)