

class Solution:

    @staticmethod
    def polindrom_number(number):
        string_number = str(number)
        return string_number[::-1] == string_number


print(Solution.polindrom_number(10))
print(Solution.polindrom_number(-121))
print(Solution.polindrom_number(1001))

# solution_obj = Solution()
# solution_obj.polindrom_number(121)

    