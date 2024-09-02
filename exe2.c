#include <stdio.h>

int main(void){
    //armazena as variaveis
    int temp1 = 1;
    int temp2 = 1;
    int aux = 0;

    int busca;

    //pergunta ao usuario o numero que deseja buscar na sequencia
    printf("digite um numero que deseje saber se pertence a sequencia fibonacci: ");
    scanf("%d",&busca);


    //roda a sequencia verificando se o numero se encontra
    while(1){
        aux = temp1 + temp2;
        temp1 = temp2;
        temp2 = aux;


        //retorna se o numero foi encontrado
        if(busca == 1 || busca == temp2){
            printf("elemento %d encontrado", busca);
            break;
        }
        //retorna se o numero nao foi encontrado
        if(temp2 > busca){
            printf("elemento nao %d encontrado!",busca);
            break;
        }
    }  

    return 0;
}
