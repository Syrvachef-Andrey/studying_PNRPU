// Задача 1

// #include <stdio.h>
// #include <time.h>
// #include <stdlib.h>

// int main()
// {
//    srand(time(0));
//    int n;
//    printf("Enter quantity of numbers \n");
//    scanf("%d", &n);
//    int massive[n];
//    for (int i = 0; i < n; i++) massive[i] = rand()%10 + 1;
//    printf("Start massive \n");
//    for (int i = 0; i < n; i++) printf("%d ", massive[i]);
//    printf("\n");
//    int new_i = 0;
//    for (int i = 1; i < n; i = i + 2){
//        massive[new_i] = massive[i];
//        new_i++;
//    }
//    n = new_i;
//    printf("Final massive \n");
//    for (int i = 0; i < n; i++) printf("%d ", massive[i]);
// }

// Задача 2

#include <stdio.h>
#include <stdlib.h>
#include <time.h>

int main(){
   srand(time(0));
   int length, n, k;
   printf("Enter quantity of numbers \n");
   scanf("%d", &length);
   int massive[length];
   for (int i = 0; i < length; i++) massive[i] = rand()%10 + 1;
   printf("Start massive \n");
   for (int i = 0; i < length; i++) printf("%d ", massive[i]);
   printf("\n");
   printf("Enter quantity to add in massive:\n");
   scanf("%d", &n);
   printf("Enter index where we need to add numbers:\n");
   scanf("%d", &k);
   for (int i = length + n; i >= k + n; i--){
      massive[i] = massive[i - n];
   }
   k = k + 1;
   for (int i = 0; i < n - 1; i++, k++){
       massive[k + i] = rand()%10 + 1;
   }
   length = length + n;
   printf("Final massive \n");
   for (int i = 0; i < length; i++) printf("%d ", massive[i]);
}

// Задача 3

// #include <stdio.h>
// #include <stdlib.h>
// #include <time.h>

// int main(){
//    srand(time(0));
//    int length;
//    printf("Enter quantity of numbers \n");
//    scanf("%d", &length);
//    int massive[length];
//    for (int i = 0; i < length; i++) massive[i] = rand()%10 + 1;
//    printf("Start massive \n");
//    for (int i = 0; i < length; i++) printf("%d ", massive[i]);
//    printf("\n");
//    int el;
//    for (int i = 0; i < length / 2; i++){
//        el = massive[i];
//        massive[i] = massive[length - 1 - i];
//        massive[length - 1 - i] = el;
//    }
//    printf("Final massive \n");
//    for (int i = 0; i < length; i++) printf("%d ", massive[i]);
// }

// Задача 4

// #include <stdio.h>
// #include <stdlib.h>
// #include <time.h>

// int main(){
//     srand(time(0));
//     int length;
//     printf("Enter quantity of numbers \n");
//     scanf("%d", &length);
//     int massive[length];
//     for (int i = 0; i < length; i++) massive[i] = rand()%10 + 1;
//     printf("Start massive \n");
//     for (int i = 0; i < length; i++) printf("%d ", massive[i]);
//     printf("\n");
//     int k;
//     int flag = 0;
//     printf("Enter number we need: \n");
//     scanf("%d", &k);
//     for (int i = 0; i < length; i++){
//         if (massive[i] == k){
//             printf("This number index is %d\n", i);
//             flag = 1;
//         }
//     }
//     if (!flag){
//         printf("There is not this number %d in massive\n", k);
//     }
// }

// Задача 5

// #include <stdio.h>
// #include <stdlib.h>
// #include <time.h>

// int main(){
//     srand(time(0));
//     int length;
//     printf("Enter quantity of numbers \n");
//     scanf("%d", &length);
//     int massive[length];
//     for (int i = 0; i < length; i++) massive[i] = rand()%10 + 1;
//     printf("Start massive \n");
//     for (int i = 0; i < length; i++) printf("%d ", massive[i]);
//     printf("\n");
//     int i, key, j;
//     for (i = 1; i < length; i++){
//         key = massive[i];
//         j = i - 1;
//         while (j >= 0 && massive[j] > key){
//             massive[j + 1] = massive[j];
//             j = j - 1;
//         }
//         massive[j + 1] = key;
//     }
//     printf("Final massive \n");
//     for (int i = 0; i < length; i++) printf("%d ", massive[i]);
//     return 0;
// }


    