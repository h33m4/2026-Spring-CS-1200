# Simulator file for question 1.
# Fill in the implementation of the different commands of the simulator.
# You can use `tests.py` to run your simulator on some prewritten RAM programs.

from collections import defaultdict

variableList = []
# Note: defaultdict works exactly the same as a normal Python dictionary except it returns a default 
#       value (in this case, 0) when accessing a key that is not defined rather than raising KeyError.
#       We are using a dictionary rather than a list/array to manage the memory so that we don't need to 
#       initialize and store memory cells that are never accessed by the RAM program.
memory = defaultdict(int)

# Creates the variable list and the memory dictionary.
# Initializes the 0th variable, input_len, to be the first element of the program array.
def setupEnv(programArr, inputArr):
    variableList.clear()
    memory.clear()

    for i in range(programArr[0]):
        variableList.append(0)
    
    variableList[0] = len(inputArr)
    for i in range(len(inputArr)):
        memory[i] = inputArr[i]
        
# Runs the given RAM program on the input.
def executeProgram(programArr, inputArr):
    setupEnv(programArr, inputArr)
    
    programArr = programArr[1:]
    programCounter = 0
    while programCounter < len(programArr):
        # Store the command and the list of operands.
        cmd = programArr[programCounter][0]
        ops = programArr[programCounter][1:]
        
        # Assignment commands
        if cmd == "read":       
            # ['read', i, j]: lookup the var_j location in memory and assign that value to var_i                    
            variableList[ops[0]] = memory[variableList[ops[1]]]
        if cmd == "write":
            # ['write', i, j]: store the value of var_j in memory at the location var_i 
            memory[variableList[ops[0]]] = variableList[ops[1]]
        if cmd == "assign":
            # ['assign', i, j]: assign var_i to the value j
            variableList[ops[0]] = ops[1]
            pass
            
        # Arithmetic commands
        if cmd == "+":
            # ['+', i, j, k]: compute (var_j + var_k) and store in var_i
            variableList[ops[0]] = variableList[ops[1]] + variableList[ops[2]]
            pass
        if cmd == "-":
            # ['-', i, j, k]: compute max((var_j - var_k), 0) and store in var_i.
            # print(variableList[ops[1]] - variableList[ops[2]])
            variableList[ops[0]] = max(0, variableList[ops[1]] - variableList[ops[2]])
            pass
        if cmd == "*":
            # ['*', i, j, k]: compute (var_j * var_k) and store in var_i.
            variableList[ops[0]] = variableList[ops[1]] * variableList[ops[2]]
            pass
        if cmd == "/":
            #  ['/', i, j, k]: compute (var_j // var_k) and store in var_i.
            # Note that this is integer division. You should return an integer, not a float.
            # Remember division by 0 results in 0.
            variableList[ops[0]] = variableList[ops[1]] // variableList[ops[2]] if variableList[ops[2]] != 0 else 0
            pass
            
        # Control commands
        if cmd == "goto":
            # ['goto', i, j]: if var_i is equal to 0, go to line j
            if variableList[ops[0]] == 0:
                programCounter = ops[1]
                continue

        programCounter += 1
    
    # Return the memory starting at output_ptr with length of output_len
    return [memory[i] for i in range(variableList[1], variableList[1]+variableList[2])]


# variables
input_len_id = 0
output_ptr_id = 1
output_len_id = 2
zero_id = 3
one_id = 4
counter_id = 5
result_id = 6
two_id = 7    # Used only in log

# RAM Program computing factorial
fac = [7, 
            ['assign', zero_id, 0],
            ['assign', one_id, 1],
            ['assign', output_len_id, 1], 
            ['assign', output_ptr_id, 0], 
            ['assign', result_id, 1],
            ['read', counter_id, zero_id],
            ['goto', counter_id, 10],
            ['*', result_id, result_id, counter_id],
            ['-', counter_id, counter_id, one_id],
            ['goto', zero_id, 6],
            ['write', output_ptr_id, result_id],
        ]

# RAM Program computing floor of log base 2
log = [8, 
            ['assign', zero_id, 0],
            ['assign', one_id, 1],
            ['assign', two_id, 2],
            ['assign', output_len_id, 1], 
            ['assign', output_ptr_id, 0], 
            ['assign', result_id, -1],
            ['read', counter_id, zero_id],
            ['goto', counter_id, 11],
            ['+', result_id, result_id, one_id],
            ['/', counter_id, counter_id, two_id],
            ['goto', zero_id, 7],
            ['write', output_ptr_id, result_id],
        ]

# Computes subtraction of two vars, returns 0 (clamped)
add = [5, 
            ['assign', output_len_id, 1], 
            ['assign', output_ptr_id, 0], 
            ['assign', 3, 3],
            ['assign', 4, 15],
            ['+', 3, 3, 4],
            ['write', output_ptr_id, 3],
        ]

# Computes subtraction of two vars, returns 0 (clamped)
minus = [5, 
            ['assign', output_len_id, 1], 
            ['assign', output_ptr_id, 0], 
            ['assign', zero_id, 3],
            ['assign', one_id, 15],
            ['-', zero_id, zero_id, one_id],
            ['write', output_ptr_id, 3],
        ]

# Computes division of two vars, returns 0 (clamped)
divide = [5, 
            ['assign', output_len_id, 1], 
            ['assign', output_ptr_id, 0], 
            ['assign', 3, 3],
            ['assign', 4, 0],
            ['/', 3, 3, 4],
            ['write', output_ptr_id, 3],
        ]


multiply = [5, 
            ['assign', output_len_id, 1], 
            ['assign', output_ptr_id, 0], 
            ['assign', 3, 3],
            ['assign', 4, 15],
            ['*', 3, 3, 4],
            ['write', output_ptr_id, 3],
        ]

def main():
    print("Result of divide: ", executeProgram(divide,[0]))
    print("Result of minus: ", executeProgram(minus,[0]))
    print("Result of add: ", executeProgram(add,[0]))
    print("Result of mult: ", executeProgram(multiply,[0]))


if __name__ == "__main__":
    main()
