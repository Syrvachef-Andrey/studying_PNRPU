#ifndef PAIR_H
#define PAIR_H

#include <typeinfo>
#include <iostream>
#include <type_traits> // Для std::is_same
using namespace std;

class Pair {
    private:
        int int_numb;
        double double_number;
    public:
        Pair(int int_numb, double double_number);
        ~Pair();

        void subtractionNumber(int int_numb, double double_number);

        template <typename T>
        void addNumber(T number, int int_numb, double double_number);
};

// Определение шаблонной функции вне класса
template <typename T>
void Pair::addNumber(T number, int int_numb, double double_number) {
    cout << "Type of data: " << typeid(number).name() << endl;
    cout << "Number: " << number << endl;

    if (std::is_same<T, double>::value) {
        cout << "Sum with double_number: " << number + double_number << endl;
    } else if (std::is_same<T, int>::value) {
        cout << "Sum with int_numb: " << number + int_numb << endl;
    }
}

#endif