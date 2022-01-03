#include <stdio.h>
#include <string.h>
void PrintList(char *lista);

int main(void) {
  char numero[25];
  fgets(numero, 25, stdin);
  PrintList(numero);
}

void PrintList(char *lista){
  int tam = strlen(lista);
  for(int i = 0;i < tam-1 ;i++){
    printf("valor: %c\n",lista[i]);
  }
}
