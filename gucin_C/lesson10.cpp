#include "pair.h"
#include <iostream>
using namespace std;

Pair::Pair(int int_numb, double double_number): int_numb(int_numb), double_number(double_number) {
    cout << "Start class with int number: " << int_numb << " and double numb: " << double_number << "\n";
}

Pair::~Pair() {
    cout << "End class with int number: " << int_numb << " and double numb: " << double_number << "\n";
}

void Pair::subtractionNumber(int num_int, double num_double) {
    cout << "Subtraction: " << num_int - num_double << "\n";
}

int main() {
    int int_num;
    double double_num;
    cout << "Enter int num: ";
    cin >> int_num;
    cout << "Enter double num: ";
    cin >> double_num;
    Pair pair(int_num, double_num);
    pair.subtractionNumber(int_num, double_num);

    int flag;
    cout << "If you want to enter double enter 0 else 1" << "\n";
    cin >> flag;

    if (flag == 0) {
        double numb;
        cout << "Enter number: ";
        cin >> numb;
        cout << "\n";
        pair.addNumber(numb, int_num, double_num);
    } else {
        int numb;
        cout << "Enter number: ";
        cin >> numb;
        cout << "\n";
        pair.addNumber(numb, int_num, double_num);
    }

    return 0;
}