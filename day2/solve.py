def solve(program):
    i = 0
    while (program[i] != 99):
        if program[i] == 1:
            program[program[i+3]] = program[program[i+1]] + program[program[i+2]]
        elif program[i] == 2:
            program[program[i+3]] = program[program[i+1]] * program[program[i+2]]
        i = i+4
    return program

def alarm(program, noun = 12, verb = 2):
    program = program[:]
    program[1] = noun
    program[2] = verb
    return solve(program)[0]

program = [1,0,0,3,1,1,2,3,1,3,4,3,1,5,0,3,2,1,6,19,1,19,5,23,2,13,23,27,1,10,27,31,2,6,31,35,1,9,35,39,2,10,39,43,1,43,9,47,1,47,9,51,2,10,51,55,1,55,9,59,1,59,5,63,1,63,6,67,2,6,67,71,2,10,71,75,1,75,5,79,1,9,79,83,2,83,10,87,1,87,6,91,1,13,91,95,2,10,95,99,1,99,6,103,2,13,103,107,1,107,2,111,1,111,9,0,99,2,14,0,0]
#print("Program1 after solving: ", alarm(program))

target = 19690720

for noun in range(100):
    for verb in range(100):
        if alarm(program, noun, verb) == target:
            print("Result:", noun, verb, 100*noun+verb)
            break;
