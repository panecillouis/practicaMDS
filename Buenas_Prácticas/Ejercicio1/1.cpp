#include <stdio.h>

void calculate_area(int width, int height) {
    int area = width * height;
    printf("Area: %d\n", area);
}

int main() {

    int ancho=0,alto=0;  // A large number
    printf("Calculadora del area de un rectangulo.\n");
    printf("Introduce el ancho.\n");
    scanf("%d",&ancho); // CWE-20 (Improper Input Validation)
    printf("Introduce el alto.\n");
    scanf("%d",&alto); // CWE-20 (Improper Input Validation)
    calculate_area(ancho, alto);
    return 0;
}
