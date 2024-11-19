
#include <stdio.h>
#include <stdlib.h>

int main() {
    // Genera 10 números aleatorios entre 0 y 10 y los muestra
    for (int i = 0; i < 10; i++) {
        printf("%d ..", rand() % 11);  // rand() % 11 genera números entre 0 y 10
    }

    return 0;
}
