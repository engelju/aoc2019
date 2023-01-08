# Your puzzle input is 307237-769058.

def check_num_for_constraints(number):
    has_adj_values = False
    adj_values = {}

    is_always_increasing = False
    
    prev_value = 0
    for i in str(number):
        value = int(i)

        if (value == prev_value):
            has_adj_values = True
            if value not in adj_values:
                adj_values[value] = 1
            else:
                adj_values[value] += 1

            if (adj_values[value] > 1):
                has_adj_values = False

        if (value >= prev_value):
            is_always_increasing = True
        else:
            is_always_increasing = False
            break
        prev_value = value

    return has_adj_values & is_always_increasing

def assert_tests():
    print(check_num_for_constraints(111111)) # true
    print(check_num_for_constraints(223450)) # false
    print(check_num_for_constraints(123789)) # false

    print(check_num_for_constraints(122345)) # true
    print(check_num_for_constraints(135679)) # false
    print(check_num_for_constraints(339300)) # false

    print(check_num_for_constraints(112233)) # true
    #print(check_num_for_constraints(123444)) # false
    #print(check_num_for_constraints(111122)) # true

assert_tests()

"""
counter = 0
value = 307237
while value < 769058:
    if check_num_for_constraints(value):
        #print(value, "matches constraints, increasing counter to", counter)
        counter+=1
    value+=1

print(counter)
"""