#include <stdio.h>
#include <stdlib.h>
#include <time.h>

int qualMaior(int tamanhoVetor, int vetor[tamanhoVetor])
{
    int maior = 0;
    for(int i = 0; i < tamanhoVetor; i++)
    {
        if(vetor[i] > vetor[maior])
        {
            maior = i;
        }
    }
    return maior;
}

int rolarDado(void)
{
    return rand() % 6 + 1;
}

int main(void)
{
    int v[6] = {0, 0, 0, 0, 0, 0};
    srand(time(NULL));

    for(int i = 0; i < 150000; i++)
    {
        switch(rolarDado())
        {
            case 1:
                v[0]++; 
                break;
            case 2:
                v[1]++; 
                break;
            case 3:
                v[2]++; 
                break;
            case 4:
                v[3]++; 
                break;
            case 5:
                v[4]++; 
                break;
            case 6:
                v[5]++; 
                break;
        }
    }
    for(int i = 0; i < 6; i++)
    {
        printf("Número de dados \"%d\": %d\n", i+1, v[i]);
    }
    printf("O dado mais repetido foi %d\n", qualMaior(6, v) + 1);
    return 0;
}
