#include <iostream>
#include <math.h>
#include <string>
#include "salary.h"

    Salary::Salary(string FIO, int salary): FIO(FIO), salary(salary){
        cout<<"Person: "<<FIO<<"\n"<<"Salary: "<<salary<<"\n";
    }

    Salary::~Salary(){
        cout<<"dismissed"<<"\n";
    }

    void Salary::PremiumCalculation(int procent){
        int prem = procent * salary / 100;
        cout<<"Premium: "<<prem<<"\n";
    }

int main(){
    int proc, sal;
    double wage;
    string FIO;
    cout<<"FIO of worker: ";
    getline(cin, FIO);
    cout<<"Salary of worker: ";
    cin>>sal;
    cout<<"Enter the procent premium from salary: ";
    cin>>proc;
    Salary salar(FIO, sal);
    salar.PremiumCalculation(proc);
    return 0;
}