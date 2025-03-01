#include <cstdio>
#include <limits>
#include <iostream>
int obtenerValorValido() {
    int valor;
    bool entradaValida = false;
    do {
       
        // Verificar si la entrada es un número
        if (!(std::cin >> valor)) {
            printf("Error: Debe ingresar un numero de longitud válida.\n");
            std::cin.clear();
            std::cin.ignore(std::numeric_limits<std::streamsize>::max(), '\n');
            continue;
        }
        // Verificar si el número es positivo
        if (valor <= 0) {
            printf("Error: El numero debe ser mayor a 0.\n");
            continue;
        }
        else {
            entradaValida = true;
        }  
    } while (!entradaValida);
    return valor;
}

void calculate_area(int width, int height) {
    // Verificar overflow en la multiplicación
    if (width > std::numeric_limits<int>::max() / height) {
        printf("Error: El resultado excederia el limite permitido.\n");}
    else
    {
        int area = width * height;
        printf("%d\n", area);
    }
}

int main() {
    int ancho = 0, alto = 0;  // A large number
    printf("Calculadora del area de un rectangulo.\n");
    printf("Introduce el ancho.\n");
    ancho = obtenerValorValido();
    printf("Introduce el alto.\n");
    alto = obtenerValorValido();
    calculate_area(ancho, alto);
    return 0;
}