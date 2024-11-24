#include <stdio.h>
#include <stdlib.h>
#include <time.h>
#include <string.h>

typedef struct {
    char brand[20];
    int year;
    int cost;
    char color[20];
} cars;

void write_cars_to_file(cars *massive, int size, const char *filename) {
    FILE *file = fopen(filename, "w");
    if (file == NULL) {
        fprintf(stderr, "Error\n");
        return;
    }

    for (int i = 0; i < size; i++) {
        fprintf(file, "Car %d:\n", i + 1);
        fprintf(file, "brand: %s\n", massive[i].brand);
        fprintf(file, "year: %d\n", massive[i].year);
        fprintf(file, "cost: %d\n", massive[i].cost);
        fprintf(file, "color: %s\n", massive[i].color);
        fprintf(file, "\n");
    }

    fclose(file);
}

int main() {
    srand(time(NULL));
    const char *cars_brand[] = {"lada", "skoda", "renault"};
    const char *cars_color[] = {"black", "white", "yellow", "red"};
    cars massive[100];

    // Заполнение массива случайными данными
    for (int i = 0; i < 100; i++) {
        massive[i].year = rand() % 21 + 1980;
        massive[i].cost = rand() % 4000 + 2000;

        int random_brand_index = rand() % 3;
        int random_color_index = rand() % 4;

        strcpy(massive[i].brand, cars_brand[random_brand_index]);
        strcpy(massive[i].color, cars_color[random_color_index]);
    }

    // Запись данных в файл
    FILE *file = fopen("cars.txt", "w");
    if (file == NULL) {
        fprintf(stderr, "Error\n");
        return 1;
    }

    for (int i = 0; i < 100; i++) {
        fprintf(file, "Car %d:\n", i + 1);
        fprintf(file, "brand: %s\n", massive[i].brand);
        fprintf(file, "year: %d\n", massive[i].year);
        fprintf(file, "cost: %d\n", massive[i].cost);
        fprintf(file, "color: %s\n", massive[i].color);
        fprintf(file, "\n");
    }

    fclose(file);

    printf("Data was written in cars.txt\n");

    // Ввод года для удаления
    int need_year;
    printf("Enter number fo year beetween 1985 and 2000: ");
    scanf("%d", &need_year);

    // Удаление структур с годом меньше введенного
    int new_len = 100;
    for (int i = 0; i < new_len; i++) {
        if (massive[i].year < need_year) {
            for (int j = i; j < new_len - 1; j++) {
                massive[j] = massive[j + 1];
            }
            new_len--;
            i--; // Уменьшаем индекс, чтобы не пропустить элементы
        }
    }

    // Вывод обновленных данных
    printf("New Data:\n");
    for (int i = 0; i < new_len; i++) {
        printf("Car %d:\n", i + 1);
        printf("brand: %s\n", massive[i].brand);
        printf("year: %d\n", massive[i].year);
        printf("cost: %d\n", massive[i].cost);
        printf("color: %s\n", massive[i].color);
        printf("\n");
    }

    // Запись обновленных данных в файл
    write_cars_to_file(massive, new_len, "cars.txt");

    printf("New data was written in cars.txt\n");

    printf("Do you need to delete K number: \n");
    int yes_or_no;
    scanf("%d", &yes_or_no);
    if (yes_or_no){
        int k_ind;
        printf("Enter k ind: ");
        scanf("%d", &k_ind);
        k_ind++;
        printf("\n");
        int new_len = 100;
        for (int j = k_ind; j < new_len - 1; j++) {
            massive[j] = massive[j + 1];
        }
        new_len--;
        printf("New Data:\n");
        for (int i = 0; i < new_len; i++) {
            printf("Car %d:\n", i + 1);
            printf("brand: %s\n", massive[i].brand);
            printf("year: %d\n", massive[i].year);
            printf("cost: %d\n", massive[i].cost);
            printf("color: %s\n", massive[i].color);
            printf("\n");
        }

        // Запись обновленных данных в файл
        write_cars_to_file(massive, new_len, "cars.txt");

        printf("New data was written in cars.txt\n");
        }
    else
    {
    return 0;
    }
}