# Your puzzle input is 307237-769058.

def check_num_for_constraints(number):
    has_adj_values = False
    is_always_increasing = False

    values = [int(i) for i in str(number)]
    for i in range(len(values)):
        #print(values[i])
        try:
            if values[i] == values[i+1]:
                #print(values[i], "is equals to", values[i+1])
                has_adj_values = True

            if values[i] <= values[i+1]:
                #print(values[i], "should be bigger or equals than", values[i+1])
                is_always_increasing = True
            else:
                is_always_increasing = False
                break
        except:
            if values[i-1] > values[i]:
                is_always_increasing = False
    return has_adj_values & is_always_increasing

#print(check_num_for_constraints(111111)) # true
#print(check_num_for_constraints(223450)) # false
#print(check_num_for_constraints(123789)) # false
#print(check_num_for_constraints(122345)) # true
#print(check_num_for_constraints(135679)) # false
#print(check_num_for_constraints(339300)) # false

print(check_num_for_constraints(112233)) # true
print(check_num_for_constraints(123444)) # false
print(check_num_for_constraints(111122)) # true

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