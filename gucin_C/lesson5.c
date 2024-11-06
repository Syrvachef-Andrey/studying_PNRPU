#include <stdio.h>
#include <stdlib.h>
#include <time.h>

void rand_massive(int* arr, int len){
    for (int i = 0; i < len; i++){
        arr[i] = rand() % 100 + 1;
    }
}

void show_massive(int* arr, int len){
    for (int i = 0; i < len; i++){
        printf("%d ", arr[i]);
    }
}

void add_elements(int* arr, int length, int quant, int ind){
    int new_length = length + quant;
    for (int i = length + quant - 1; i >= ind + quant; i--){
        arr[i] = arr[i - quant];
    }
    for (int i = 0; i < quant; i++){
        arr[ind + i] = rand() % 100 + 1;
    }
    for (int i = 0; i < new_length; i++){
        printf("%d ", arr[i]);
    }
}

void two_dimensional_array(int **arr, int rows, int cols){
    for (int i = 0; i < rows; i++){
        for (int j = 0; j < cols; j++){
            arr[i][j] = rand() % 100 + 1;
        }
    }
    for (int i = 0; i < rows; i++){
        for (int j = 0; j < cols; j++){
            printf("%2d ", arr[i][j]);
        }
        printf("\n");
    }
}

void delete_even_strings(int ***arr, int *rows, int cols){
    int new_rows = 0;
    for (int i = 0; i < *rows; i++){
        if ((i + 1) % 2 == 0){  // Удаляем строки с четными индексами (индексация с 1)
            free((*arr)[i]);
        } else {
            (*arr)[new_rows++] = (*arr)[i];
        }
    }
    *rows = new_rows;
    *arr = (int **)realloc(*arr, new_rows * sizeof(int *));
}

int main() {
    srand(time(NULL));
    int length, kolvo, ind, rows, columns;

    // Работа с одномерным массивом
    printf("Work with ONE dimensional massive: \n");
    printf("Enter length of massive: ");
    scanf("%d", &length);
    int *massive = (int *)malloc(length * sizeof(int));
    printf("start massive: \n");
    rand_massive(massive, length);
    show_massive(massive, length);
    printf("\n");
    printf("Enter index where we need to add elements: ");
    scanf("%d", &ind);
    printf("Enter quantity of new elements: ");
    scanf("%d", &kolvo);
    printf("Final massive: \n");
    add_elements(massive, length, kolvo, ind);
    printf("\n");
    free(massive);  // Освобождаем память после использования массива
    
    // Работа с двумерным массивом
    printf("Work with TWO dimensional massive: \n");
    printf("Enter quantity of rows: ");
    scanf("%d", &rows);
    printf("Enter quantity of columns: ");
    scanf("%d", &columns);
    int **two_massive = (int **)malloc(rows * sizeof(int *));
    for (int i = 0; i < rows; i++){
        two_massive[i] = (int *)malloc(columns * sizeof(int));
    }
    printf("Start two_dimensional_array: \n");
    two_dimensional_array(two_massive, rows, columns);
    
    printf("Final two_dimensional_array: \n");
    delete_even_strings(&two_massive, &rows, columns);
    two_dimensional_array(two_massive, rows, columns);
    
    for (int i = 0; i < rows; i++) {
        free(two_massive[i]);
    }
    free(two_massive);

    return 0;
}