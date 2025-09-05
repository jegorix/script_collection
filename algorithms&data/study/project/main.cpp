
#include <iostream>
#include "Animal.h"
using namespace std;

int main()
{

 cout << "=== ДЕМОНСТРАЦИЯ КЛАССА ANIMAL ===\n" << endl;
 Animal animal1;
 Animal animal2("Барсик", 3, 4.5);
 Animal animal3("Шарик", 5, 12.3);

 cout << "\nВсего животных: " << Animal::getAnimalCount() << endl;

    cout << "\n2. ГЕТТЕРЫ:" << endl;
    cout << "Имя animal2: " << animal2.getName() << endl;
    cout << "Возраст animal3: " << animal3.getAge() << " лет" << endl;
    cout << "Вес animal2: " << animal2.getWeight() << " кг" << endl;

 cout << "\n3. СЕТТЕРЫ:" << endl;
 animal1.setName("Murka");
 animal1.setAge(2);
 animal1.setWeight(3.8);
 animal1.printInfo();

cout << "\n4. ПРОВЕРКА ВАЛИДАЦИИ:" << endl;
animal1.setAge(-5);
animal1.setWeight(-3.14);

cout << "\n5. МЕТОДЫ ПОВЕДЕНИЯ:" << endl;

animal2.printInfo();
animal2.eat(13);
animal2.sleep(6);
animal2.makeSound();

cout << endl;

cout << "\n7. ДИНАМИЧЕСКОЕ СОЗДАНИЕ:" << endl;

Animal* newAnimal = new Animal("Dino", 10, 23.73);
newAnimal->printInfo();
newAnimal->makeSound();

 cout << "\n8. СТАТИСТИКА:" << endl;
cout << "Всего создано животных: " << Animal::getAnimalCount() << endl;


cout << "\n9. УДАЛЕНИЕ ДИНАМИЧЕСКОГО ОБЪЕКТА:" << endl;
 delete newAnimal;

cout << "\n10. ЗАВЕРШЕНИЕ ПРОГРАММЫ:" << endl;
cout << "Оставшееся количество животных: " << Animal::getAnimalCount() << endl;



}