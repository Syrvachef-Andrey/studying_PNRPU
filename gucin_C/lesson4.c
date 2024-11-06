// Задача 1

// #include <stdio.h>
// #include <stdlib.h>
// #include <time.h>

// void rand_arr(int massive[], int n){
//     for (int i = 0; i < n; i++) massive[i] = rand()%100 + 1;
// }

// void output_massive(int massive[], int n)
// {
//     for (int i = 0; i < n; i++) printf("%d ", massive[i]);
// }

// void prime_numbers(int massive[], int n, int state_of_simple)
// {
//     printf("\nPrime quantity:\n");
//     for (int i = 0; i < n; i++)
//     {
//         state_of_simple = 1;
//         for (int j = 2; j < ((massive[i] / 2) + 1); j++){
//             if (!(massive[i] % j != 0)){
//                 state_of_simple = 0;
//                 break;
//             }
//         }
//         if (state_of_simple){
//             printf("%d ", massive[i]);
//         }
//     }
// }

// int main()
// {
//     int n, summ_of_min_elem, state_of_simple;
//     printf("Enter start quantity of massive: \n");
//     scanf("%d", &n);
//     int massive[n];
//     srand(time(NULL));
//     rand_arr(massive, n);
//     printf("Start massive: \n");
//     output_massive(massive, n);
//     prime_numbers(massive, n, state_of_simple);
//     return 0;
// }

// Задача 2

// #include <stdio.h>
// #include <stdlib.h>
// #include <time.h>

// int height, weight;

// void arr_rand(int arr[][weight], int h, int w)
// {
//     for (int i = 0; i < h; i++){
//         for (int j = 0; j < w; j++)
//         {
//             arr[i][j] = rand()%100 + 1;
//         }
//     } 
// }

// void output_arr(int arr[][weight], int h, int w)
// {
//     for (int i = 0; i < h; i++){
//         for (int j = 0; j < w; j++){
//             printf("%03d ", arr[i][j]);
//         }
//         printf("\n");
//     }
// }

// void sort_string(int arr[][weight], int h, int w)
// {
//     for (int i = 0; i < h; i++){
//         for (int pass = 0; pass < w - 1; pass++)
//         { 
//             for (int j = 0; j < w - 1 - pass; j++)
//             { 
//                 if (arr[i][j] < arr[i][j + 1])
//                 {
//                     int t = arr[i][j];
//                     arr[i][j] = arr[i][j + 1];
//                     arr[i][j + 1] = t;
//                 }
//             }
//         }
//     }
// }

// int main()
// {
//     printf("Enter start height of massive:\n");
//     scanf("%d", &height);
//     printf("Enter start weight of massive:\n");
//     scanf("%d", &weight);
//     int massive[height][weight];
//     srand(time(0));
//     arr_rand(massive, height, weight);
//     printf("Start massive: \n");
//     output_arr(massive, height, weight);
//     sort_string(massive, height, weight);
//     printf("Final massive: \n");
//     output_arr(massive, height, weight);
// }

// Задача 3

#include <stdio.h>
#include <stdlib.h>
#include <string.h>

void enter_str(char** str) {
    size_t len = 0;
    size_t read; 
    printf("Enter the string: \n");
    read = getline(str, &len, stdin);

    if (read == -1) {
        printf("Ошибка при чтении строки.\n");
        free(*str);
        *str = NULL;
    }
}

char* delete_glas(char* str) {
    char vowels[] = "AEIOUaeiou";
    size_t len = strlen(str);
    char* new_string = (char*)malloc((len + 1) * sizeof(char)); 
    size_t j = 0;

    for (size_t i = 0; i < len; i++) {
        int glas_flag = 1;
        for (size_t k = 0; k < strlen(vowels); k++) {
            if (str[i] == vowels[k]) {
                glas_flag = 0;
                break;
            }
        }
        if (glas_flag) {
            new_string[j++] = str[i];
        }
    }
    new_string[j] = '\0';
    return new_string;
}

int main() {
    char* string = NULL;
    enter_str(&string);

    if (string != NULL) {
        printf("Entred string: %s", string);

        char* result = delete_glas(string);
        printf("String without vowels: %s", result);

        free(result); 
        free(string); 
    }

    return 0;
}