#include <stdio.h>

int main(void){
    //pedindo ao usuario para armazenar uma palavra
    char palavra[20];

    printf("digite uma palavra para ser invertida: ");
    scanf("%s", palavra);
    
    //descobrindo o tamanho da palavra
    int tamanho = 0;
    while(palavra[tamanho] != '\0'){
        tamanho++;
    }

    //declarando algumas variaveis que vamos utilizar para inverter
    int inicio = 0;
    int fim = tamanho-1;
    char temp;

    //invertendo a palavra
    while(inicio < fim){
        temp = palavra[inicio];
        palavra[inicio] = palavra[fim];
        palavra[fim] = temp;
        
        inicio++;
        fim--;
    }   

    //printando o resultado
    printf("%s",palavra);
    return 0;
}
