from random import choice
import os

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')


def main():
    HANGMAN = (
        """
        ------
        |    |
        |
        |
        |
        |
        |
        ----------
        """,
        """
        ------
        |    |
        |    O
        |
        |
        |
        |
        ----------
        """,
        """
        ------
        |    |
        |    O
        |    |
        | 
        |   
        |    
        ----------
        """,
        """
        ------
        |    |
        |    O
        |   /|
        |   
        |   
        |   
        ----------
        """,
        """
        ------
        |    |
        |    O
        |   /|\\
        |   
        |   
        |     
        ----------
        """,
        """
        ------
        |    |
        |    O
        |   /|\\
        |   /
        |   
        |    
        ----------
        """,
        """
        ------
        |    |
        |    O
        |   /|\\
        |   / \\
        |   
        |   
        ----------
        """
    )

    max_wrong = len(HANGMAN) - 1
    WORDS = (
        "кошка",
        "машина",
        "дерево",
        "глобус",
        "библиотека",
        "пальто",
        "инструмент",
        "загадка",
        "картина",
        "перемена",
        "грамматика",
        "воспитание",
        "инженер",
        "торжество",
        "экспедиция",
        "свидетель",
        "путешествие",
        "рассуждение",
        "ответственность",
        "вдохновение",
    )
    word = choice(WORDS)

    so_far = "_" * len(word)
    wrong = 0
    used = []

    while wrong < max_wrong and so_far != word:
        print(HANGMAN[wrong])
        print("\nВы использовали следующие буквы:\n", used)
        print("\nНа данный момент слово выглядит так:\n", so_far)
        guess = input("\n\nВведите свое предположение: ")

        while guess in used:
            print("Вы уже вводили букву", guess)
            guess = input("Введите свое предположение: ")
        
        used.append(guess)

        if guess in word:
            print("\nДа!", guess, "есть в слове!")
            new = ""

            for i in range(len(word)):
                if guess == word[i]:
                    new += guess
                else:
                    new += so_far[i]

            so_far = new

        else:
            print("\nИзвините, буквы \"" + guess + "\" нет в слове.")
            wrong += 1


    if wrong == max_wrong:
        print(HANGMAN[wrong])
        print("\nТебя повесили!")

    else:
        print("\nВы угадали слово!")

    print("\nЗагаданное слово было \"" + word + '\"')


    print("Игра окончена!")
    input("Нажмите Enter, чтобы выйти...")
    clear_screen()

if __name__ == "__main__":
    main()