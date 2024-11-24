#ifndef SALARY_H
#define SALARY_H

#include <iostream>
#include <string>
using namespace std;

class Salary {
private:
    string FIO;
    int salary;
public:
    Salary(string FIO, int salary);  // Исправлено объявление параметров
    ~Salary();

    void PremiumCalculation(int proc);  // Добавлена точка с запятой
};

#endif // SALARY_H