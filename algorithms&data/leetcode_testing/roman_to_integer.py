
# class Solution:
#     @staticmethod
#     def romanToInt(string: str) -> int:
#         roman_dict = {
#             'I': 1,
#             'V': 5,
#             'X': 10,
#             'L': 50,
#             'C': 100,
#             'D': 500,
#             'M': 1000,
#         }
        
#         roman_adds = {
#             'IV': 4,
#             'IX': 9,
#             'XL': 40,
#             'XC': 90,
#             'CD': 400,
#             'CM': 900
#         }

#         res = 0
#         i = 0

#         while i < len(string):

#             if string[i:i+2] in roman_adds:
#                 res += roman_adds[string[i:i+2]]
#                 i += 2
#             else:
#                 res += roman_dict[string[i]]
#                 i += 1

#         return res

            

            

class Solution:
    @staticmethod
    def romanToInt(string: str) -> int:

        roman_dict = {
            'I': 1,
            'V': 5,
            'X': 10,
            'L': 50,
            'C': 100,
            'D': 500,
            'M': 1000,
        }
        
        res = 0
        prev_value = 0

        for char in reversed(string):
            value = roman_dict[char]
            if value < prev_value:
                res -= value
            else:
                res += value
                prev_value = value
        return res



print(Solution.romanToInt(string = "III"))
print(Solution.romanToInt(string = "LVIII"))
print(Solution.romanToInt(string = "MCMXCIV"))
print(Solution.romanToInt(string = "IX"))
print(Solution.romanToInt(string = "MCDLXXVI"))
