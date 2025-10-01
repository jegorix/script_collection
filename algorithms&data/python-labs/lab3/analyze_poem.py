# Демон Лермонтов

# Запишите в файл ваше любимое стихотворение.
# Выведите его на экран и укажите, 
# каких слов в нем больше: начинающихся 
# на гласную или на согласную (регистр букв не учитывать). 
from typing import List, Optional

CONSONANTS = "бвгджзйклмнпрстфхцчшщ"
VOWELS = "аеёиоуыэюя"


def _get_poem(filename: str) ->  Optional[List[str]]:
    try:
        with open(filename, encoding='utf-8', mode='r') as f:
            return f.readlines()
    except (FileExistsError, FileNotFoundError) as e:
        raise Exception(f"Возникла проблема с файлом: {e}")

    except Exception as e:
        raise Exception(f"Возникла ошибка: {e}")

    
def show_poem(filename: str) -> None:
    lines = _get_poem(filename)
    for row in lines:
        print(row)
        

def _estimate_words(filename: str) -> dict:
    lines = _get_poem(filename)
    
    vowels_count = 0
    consonants_count = 0
    
    for line in lines:
        for word in line.split():
            
            if word[0].lower() in CONSONANTS:
                consonants_count += 1
            elif word[0].lower() in VOWELS:
                vowels_count += 1
                
                
    if consonants_count > vowels_count:
        greater = "согласную"
    elif vowels_count > consonants_count:
        greater = "гласную"
    else:
        greater = "одинаково"
                
    return {
        'consonants_words': consonants_count,
        'vowels_words': vowels_count,
        'greater_words': greater
    }
    
    
def result_words_count(filename: str) -> None:
    data = _estimate_words(filename)  
    
    response = f"""
          Количество слов, начинающихся на согласную букву: {data['consonants_words']}
          Количество слов, начинающифхся на гласную букву: {data['vowels_words']}
          Больше слов на: {data['greater_words']}
          """
   
    print(response)
    
        
if __name__ == '__main__':
   show_poem('files/poem.txt')
   result_words_count('files/poem.txt')
    
        