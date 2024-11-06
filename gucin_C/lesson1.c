// Лабораторная работа № 1

// Задача 1.4

#include <stdio.h>
#include <math.h>

int main(){
    double x = 0;
    printf("x?");
    scanf("%lf", &x);
    double r1;
    r1 = 1 + x * pow(cos(x), 2) + pow(sin(x), 3);
    printf("Responce = %f", r1);
}

// Задача 2

// #include <stdio.h>
// #include <math.h>

// int main(){
//     double x = 0;
//     double y = 0;
//     printf("x?");
//     scanf("%lf", &x);
//     printf("y?");
//     scanf("%lf", &y);
//     int r2 = ((pow(x, 2) + pow(y, 2)) <= 1) && !(x > 0 && y > 0);
//     printf("Response = %d", r2);
// }
