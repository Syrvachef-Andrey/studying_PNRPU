#include <stdio.h>
#include <stdlib.h>
#include <time.h>
#include <string.h>

typedef struct {
    char name[50];
    int age;
    double rating;
} pupil;

int main(){
    srand(time(0));
    int new_len = 0;
    pupil massive[100];

    for (int i = 0; i < 100; i++){
        char random_name[50];

        sprintf(random_name, "Pupil%d", i + 1);
        strcpy(massive[i].name, random_name);

        massive[i].age = rand() % 13 + 6;
        massive[i].rating = (double)(rand() % 31 + 20) / 10.0;
    }

    for (int i = 0; i < 100; i++) {
        printf("Pupil %d:\n", i + 1);
        printf("Name: %s\n", massive[i].name);
        printf("Age: %d\n", massive[i].age);
        printf("Rating: %.2f\n", massive[i].rating);
        printf("\n");
        if (massive[i].rating == 4.50){
            new_len++;
        }
    }
    printf("%d", new_len);
}