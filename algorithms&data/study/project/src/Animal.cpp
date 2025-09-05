#include "Animal.h"
#include <iostream>
#include <cassert>

using namespace std;

int Animal::animalCount = 0;

Animal::Animal() : name("Unknown"), age(0), weight(0.0)
{
    animalCount++;
    cout << "Default constructor called" << endl;
}

Animal::Animal(const string& name, int age, double weight) : name(name), age(age), weight(weight)
{
    animalCount++;
    cout << "Parameterized constructor called for " << name << endl;
}

Animal::~Animal()
{
    animalCount--;
    cout << "Animal " << name << " destroyed" << endl;
}


// GETTERS
string Animal::getName() const
{
    return name;
}

int Animal::getAge() const
{
    return age;
}

double Animal::getWeight() const
{
    return weight;
}

// setters

void Animal::setName(const string& name)
{
    this->name = name;
}

void Animal::setAge(int age)
{
    if(age > 0) this->age = age;
    else cout << "Error: Age cannot be negative!" << endl;
}

void Animal::setWeight(double weight)
{
    if(weight > 0) this->weight = weight;
    else cout << "Error: Weight cannot be negative!" << endl;
    // assert(weight > 0 && "Weight cannot be negative");
    // this->weight = weight;

}

// public methods

void Animal::printInfo() const
{
    cout << "\n" << "Name: " << name
    << "\n" << "Age: " << age
    << "\n" << "Weight: " << weight
    << endl;

}

void Animal::eat(double foodAmount)
{
    if(foodAmount > 0)
    {
        weight += foodAmount * 0.1;
        cout << name << " ate " << foodAmount << " kg of food. ";
        cout << "New weight: " << weight << " kg" << endl;
    }
    else cout << "Error: Food amount must be positive!" << endl;
}

void Animal::sleep(int hours)
{
    if(hours > 0) cout << name << " is sleeping for " << hours << " hours" << endl;
    else cout << "Error: Sleep time must be positive!" << endl;
}

void Animal::makeSound() const
{
    cout << name << " says: Some animal sound!" << endl;
}

int Animal::getAnimalCount()
{
    return animalCount;
}