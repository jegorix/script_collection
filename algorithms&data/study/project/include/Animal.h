#ifndef ANIMAL_H
#define ANIMAL_H

using namespace std;

#include <string>

class Animal
{
    private:
        std::string name;
        int age;
        double weight;
        static int animalCount;
    
    public: // Constructors
    Animal();
    Animal(const string& name, int age, double weight);

    // Destructors
    ~Animal();

    // getters
    string getName() const;
    int getAge() const;
    double getWeight() const;

    // setters
    void setName(const string& name);
    void setAge(int age);
    void setWeight(double weight);

    // public methods
    void printInfo() const;
    void eat(double foodAmount);
    void sleep(int hours);
    void makeSound() const;

    // static method
    static int getAnimalCount();

};

#endif