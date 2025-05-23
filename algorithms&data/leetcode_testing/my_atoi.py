def my_atoi(s: str) -> int:
    s = s.strip()
    if not s:
        return 0
    
    INT_MIN = -2**31
    INT_MAX = 2**31 - 1
    result = 0
    sign = 1
    i = 0
    if s[i] == '-':
        sign = -1
        i += 1
    elif s[i] == '+': 
        i += 1

    while i < len(s) and s[i].isdigit():
        result = result * 10 + int(s[i])
        i += 1

    result *= sign

    if result > INT_MAX:
        return INT_MAX
    elif result < INT_MIN:
        return INT_MIN
    
    return result


    



    # digits = ['0','1', '2', '3', '4', '5', '6', '7', '8', '9', '+']
    # result = ''
    # number_stripped = number_string.strip()
    # for i in range(len(number_stripped)):
    #     if (number_stripped[0] == '-' or number_stripped[0] == '+') and i == 0:
    #         result += number_stripped[i]
    #     elif number_stripped[i] in digits:
    #         result += number_stripped[i]
    #     else:
    #         break

    # try:
    #     result = int(result)
    #     if result > 2**31 - 1 or result < -2**31:
    #         result = 2**31 - 1 if result > 0 else -2**31
    #     return result
    
    # except ValueError:
    #     return 0
        

print(my_atoi('42')) 

print(my_atoi('     -0000000042')) 
print(my_atoi('     -000000004sdcsad2asdada'))
print(my_atoi("0-1"))
print(my_atoi("words and 987"))
print(my_atoi("-91283472332"))
print(my_atoi("91283472332"))