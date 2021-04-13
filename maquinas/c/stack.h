/*
Cabecera que sirve de apoyo al programa que emula una máquina de stack, para lo cual genera 
listas dinámicas para la representación de las instrucciones y la pila en sí.
Entrada: Se necesita un archivo de texto, llamado Stack.in, que debe estar ubicado en 
	la misma carpeta que este archivo.
Salida: Por la salida standar sale la ejecución, paso a paso, de la máquina de de stack,
	al estilo de una traza.
Fecha de creación: 2-2017
Fecha de actualización: 2-2018
Autor: Alejandro Cisterna Villalobos
*/
/*Se incluyen las librerias necesarias
OBS: No se incluye stdio, dado que no se utiliza en ninguna parte de éste código elementos
correspondientes a esa librería*/
#include <stdlib.h>
#include <string.h>//http://c.conclase.net/librerias/?ansilib=string#inicio
#include <math.h>//http://c.conclase.net/librerias/?ansilib=math#inicio

/*Función PUSH, que ingresa un dato a la pila
Entrada:
	- primero: Puntero a un valor entero que representa la posición del primer elemento
	de la pila
	- stack: Puntero a la matriz de caracteres que almacena las instrucciones de la máquina
	de stack creada (es la que se encuentra en el archivo de texto a leer)
	- dato: Puntero al char que se desea ingresar dentro de la pila de elementos*/
void PUSH(int * primero, char *** stack, char * dato){	

	(*stack)[(*primero)] = dato; 
	*primero = * primero + 1;
}

/*Función POP, que elimina el elemento que esté en el tope del stack
Entrada:
	- primero: Puntero a un valor entero que representa la posición del primer elemento
	de la pila
	- stack: Puntero a la matriz de caracteres que almacena las instrucciones de la máquina
	de stack creada (es la que se encuentra en el archivo de texto a leer)
Salida:
	- dato: Cadena de caracteres que posee el elemento que se encontraba en el tope del stack*/
char * POP(int *primero, char *** stack){
	int n = *primero;
	*primero = *primero - 1;
	char * dato = (*stack)[n-1];
	(*stack)[n-1] = "";
	return dato;
}
/*Función SUM, que realiza la suma de los dos elementos que estén al tope del stack.
Entrada: 
	- primero: puntero a la posición donde se encuentra el primer elemento.
	- stack: puntero a la matriz de los elementos almacenados en el stack
No retorna nada*/
void SUM (int *primero, char *** stack){
	char * n1 = POP(primero, stack);
	char * n2 = POP(primero, stack);
	//Función atoi de la librería stdlib, que transforma la cadena de caracteres en su representación en int
	int num1 = atoi(n1);
	int num2 = atoi(n2);
	//Reservo memoria para que la suma se almacene como una cadena de caracteres (string)
	char * suma = (char *) malloc(sizeof(char)*20); 
	/*Función sprintf almacena en la primera variable la transformación a string del valor de la tercera
	variable. La segunda variable indica el tipo de dato que posee la tercera variable*/ 
	sprintf ( suma, "%d" , num1 +  num2 );
	PUSH(primero,stack,suma);
	return;
}

/*Función RES, que realiza la resta de los dos elmentos que están al tope del stack
La estructura de la función es similar a la de la función SUM
La resta es lo que está más al tope del stack menos el que viene*/
void RES (int *primero, char *** stack){
	char * n1 = POP(primero, stack);
	char * n2 = POP(primero, stack);
	int num1 = atoi(n1);
	int num2 = atoi(n2);
	char * suma = (char *) malloc(sizeof(char)*20); 
	sprintf ( suma, "%d" , num1 -  num2 );
	PUSH(primero,stack,suma);
	return;	
}

/*Función MUL, que realiza la multiplicacióna de los dos elmentos que están al tope del stack
La estructura de la función es similar a la de la función SUM*/
void MUL (int *primero, char *** stack){
	char * n1 = POP(primero, stack);
	char * n2 = POP(primero, stack);	
	int num1 = atoi(n1);
	int num2 = atoi(n2);
	char * suma = (char *) malloc(sizeof(char)*20); 
	sprintf ( suma, "%d" , num1 *  num2 );
	PUSH(primero,stack,suma);
	return;
}

/*Función DIV, que realiza la división entera de los dos elmentos que están al tope del stack
La estructura de la función es similar a la de la función SUM
La división es lo que está más al tope del stack dividido el que viene*/
void DIV (int *primero, char *** stack){
	char * n1 = POP(primero, stack);
	char * n2 = POP(primero, stack);
	int num1 = atoi(n1);
	int num2 = atoi(n2);
	char * suma = (char *) malloc(sizeof(char)*20); 
	sprintf ( suma, "%d" , num1 /  num2 );
	PUSH(primero,stack,suma);
	return;
}

/*Función MOD, que realiza el resto de la división entera de los dos elmentos que están al tope del stack
La estructura de la función es similar a la de la función SUM
Entrega el resto de la división es lo que está más al tope del stack dividido el que viene*/
void MOD (int *primero, char *** stack){
	char * n1 = POP(primero, stack);
	char * n2 = POP(primero, stack);
	int num1 = atoi(n1);
	int num2 = atoi(n2);
	char * suma = (char *) malloc(sizeof(char)*20); 
	sprintf ( suma, "%d" , num1 %  num2 );
	PUSH(primero,stack,suma);
	return;
}

/*Función RAI, que realiza la raiz cuadrada del elmento que esta al tope del stack
La estructura de la función es similar a la de la función SUM*/
void RAI (int *primero, char *** stack){
	char * n1 = POP(primero, stack);
	int num1 = atoi(n1);
	char * suma = (char *) malloc(sizeof(char)*20); 
	sprintf (suma, "%d" , (int)sqrt(num1));
	PUSH(primero,stack,suma);
	return;
}

/*Función EXP, que realiza la operación de e^x elmento que esta al tope del stack
La estructura de la función es similar a la de la función SUM*/
void EXP (int *primero, char *** stack){
	char * n1 = POP(primero, stack);
	int num1 = atoi(n1);
	char * suma = (char *) malloc(sizeof(char)*20); 
	sprintf ( suma, "%d" , (int)exp(num1));
	PUSH(primero,stack,suma);
	return;
}

/*Función POT, que realiza potencia de los dos elmentos que están al tope del stack
La estructura de la función es similar a la de la función SUM
Entrega la potencia del elemento está más al tope del stack elevado el que viene*/
void POT (int *primero, char *** stack){	
	char * n1 = POP(primero, stack);
	char * n2 = POP(primero, stack);
	int num1 = atoi(n1);
	int num2 = atoi(n2);
	char * suma = (char *) malloc(sizeof(char)*20); 
	sprintf ( suma, "%d" , (int)pow(num1,  num2) ) ;
	PUSH(primero,stack,suma);
	return;
}