// Задача 1

// #include <stdio.h>

// int main(){
//     int n = 0;
//     int the_first = 0;
//     int k = 0;
//     int j = 0;
//     printf("Enter quantity of numbers?");
//     scanf("%d", &n);
//     for (int i = 0; i < n; i++)
//     {
//         printf("Enter number: ");
//         scanf("%d", &k);
//         if (i == 0){
//             the_first = k;
//             printf("This is the first number - %d\n", k);
//         }
//         else{
//             if (the_first % k == 0){
//                 printf("Number %d is multiple to %d\n", the_first, k);
//                 j++;
//             }
//             else
//             {
//                 printf("Number %d is not multiple to %d\n", the_first, k);
//             }
//         }
//     }
//     printf("quantity = %d", j);
// }

// Задача 2

#include <stdio.h>

int main(){
    int summ = 0;
    int n;
    int i = 1;
    do {
        printf("Enter n: ");
        scanf("%d", &n);
        if (i % 2 == 0){
            summ = summ + n;
        }
        i++;
    } while (n != 0);
    printf("Total summ = %d", summ);
} 

// Задача 3

// #include <stdio.h>

// int main(){
//     int a1 = 1;
//     int a2 = 1;
//     int i = 1;
//     int a3 = 0;
//     int n = 0;
//     printf("Enter n: ");
//     scanf("%d", &n);
//     while (i < n){
//         a3 = a1 + a2;
//         a1 = a2;
//         a2 = a3;
//         printf("%d, %d\n", a1, a2);
//         i++;
//     }
//     return 0;
// }
