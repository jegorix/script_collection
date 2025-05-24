


# def isValid(s: str) -> bool:
    
#     data = {
#         '(': 0,
#         ')': 0,
#         '[': 0,
#         ']': 0,
#         '{': 0,
#         '}': 0
#     }

#     for char in s:
#         if char == '(' or char == '[' or char == "{":
#             data[char] += 1
#         if char == ')' or char == ']' or char == "}":
#             data[char] -= 1

#     result = bool(data['('] + data[')'] or data['['] + data[']'] or data['{'] + data['}'])
#     return not result








# print(isValid(s = "()"))
# print(isValid(s = "()[]{}"))
# print(isValid(s = "([])"))
# print(isValid(s = "(]"))
# print(isValid(s = "[["))
# print(isValid(s = "{"))
# print(isValid(s = "([)]"))




# def reverse(number):
#     if number >= 2**31 - 1 or number <= -2**31:
#         return 0

#     elif number > 0:
#         new_number = int(str(number)[::-1])
#     else:
#         number *= -1
#         new_number = int(str(number)[::-1]) * -1
#     print(new_number)



# reverse(123)
# reverse(-321)
# reverse(120)
# reverse(1534236469)
# print(9646324351 > 2**31 - 1)


# def longestPalidrome(string):
#     longest = 0
#     palidrome = ""
#     max_pol = 0
#     for i in range(len(string)-1):
#         if string[i] == string[-1-i]:
#             longest += 1
#         else:
#            longest = 0
        
#         max_pol = max(longest, max_pol)
            
#     print(max_pol)
        






# longestPalidrome(string = "babad")
# longestPalidrome(string = "cbbd")
# longestPalidrome(string = "abcdefg")
# longestPalidrome(string = "bbckabakbb")


# def my_atoi(s: str) -> int:
#     s = s.strip()
#     if not s:
#         return 0
    
#     INT_MIN = -2**31
#     INT_MAX = 2**31 - 1
#     result = 0
#     sign = 1
#     i = 0
#     if s[i] == '-':
#         sign = -1
#         i += 1
#     elif s[i] == '+': 
#         i += 1

#     while i < len(s) and s[i].isdigit():
#         result = result * 10 + int(s[i])
#         i += 1

#     result *= sign

#     if result > INT_MAX:
#         return INT_MAX
#     elif result < INT_MIN:
#         return INT_MIN
    
#     return result


    



#     # digits = ['0','1', '2', '3', '4', '5', '6', '7', '8', '9', '+']
#     # result = ''
#     # number_stripped = number_string.strip()
#     # for i in range(len(number_stripped)):
#     #     if (number_stripped[0] == '-' or number_stripped[0] == '+') and i == 0:
#     #         result += number_stripped[i]
#     #     elif number_stripped[i] in digits:
#     #         result += number_stripped[i]
#     #     else:
#     #         break

#     # try:
#     #     result = int(result)
#     #     if result > 2**31 - 1 or result < -2**31:
#     #         result = 2**31 - 1 if result > 0 else -2**31
#     #     return result
    
#     # except ValueError:
#     #     return 0
        

# print(my_atoi('42')) 

# print(my_atoi('     -0000000042')) 
# print(my_atoi('     -000000004sdcsad2asdada'))
# print(my_atoi("0-1"))
# print(my_atoi("words and 987"))
# print(my_atoi("-91283472332"))
# print(my_atoi("91283472332"))