import numpy as np
import random
from pprint import pprint

class Student():
    count = 0
    def __init__(self, age, gender, scores_math, scores_physics, scores_cs) -> None:
        self.__count = Student.count + 1
        self._age = age
        self._gender = gender
        self._scores_math = scores_math
        self._scores_physics = scores_physics
        self._scores_cs = scores_cs
        Student.count += 1
        
    def get_average(self, array):
        return sum(array) / len(array)
    
    
    def __repr__(self) -> str:
        response = f"""
            Student-{self.__count}
            Age: {self._age}
            Scores math: {self._scores_math},
            Scores physics: {self._scores_physics},
            Scores cs: {self._scores_cs},
        """
        return response
        
    def __str__(self) -> str:
        return f'Student-{self.__count}'
    
    
def fill_scores():
    return np.random.randint(0, 101, size=15)

def show_students(students):
    for student in students:
        print(student)

        
        
age = np.random.randint(17, 25, size=100)
gender = np.random.randint(0, 2, size=100)
        
students = [Student(age=np.random.choice(age), gender=np.random.choice(gender), scores_math=fill_scores(), scores_physics=fill_scores(), scores_cs=fill_scores()) for i in range(101)]

show_students(students)


def test(students):
    
    #Indexing and slices
    response = {
        'students>20': [str(student) for student in students if student._age > 20],
        'ages': age[age>20],
        'Cs>80': [student for student in students if student.get_average(student._scores_cs) > 80]
    }
    
    pprint(response, indent=4, sort_dicts=False)
    


if __name__ == '__main__':
    test(students)