#ifndef ROW_H
#define ROW_H

#include <iostream>
using namespace std;

class Row {
private:
    double first;
    int r;
public:
    Row(double first, int r);  // Добавлена точка с запятой
    ~Row();  // Добавлена точка с запятой

    void Element(int j);  // Добавлена точка с запятой
};

#endif // ROW_H