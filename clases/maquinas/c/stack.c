/*
Programa que emula una máquina de stack, para lo cual genera listas dinámicas para la
representación de las instrucciones y la pila en sí.
Entrada: Se necesita un archivo de texto, llamado Stack.in, que debe estar ubicado en 
	la misma carpeta que este archivo.
Salida: Por la salida standar sale la ejecución, paso a paso, de la máquina de de stack,
	al estilo de una traza.
Fecha de creación: 2-2017
Fecha de actualización: 2-2018
Autor: Alejandro Cisterna Villalobos
*/

/*Se incluyen las librerías necesarias*/
#include <stdio.h>
#include "stack.h"

/*Se predefinen las funciones, explícitamente en este código no es necesario, pero se 
muestran con el fin de saber como se realiza.
Estas son solo las firmas de las funciones, deben ser exacactamente como están definidas
posteriormente, en estos momentos solo le decimos al programa que conoce estas funciones,
pero el qué realizan, lo haremos posteriormente en el cuerpo de la función*/
int lectura(char *** programa, int * push);
char ** crearStackInstrucciones(char ** programa,int instrucciones);
void escritura(int n);
void mostrarStack(char ** stack,int instrucciones,char *  mensaje);
void ejecutar(char ** programa, char ** stack, int instrucciones,  int push);

/*Función lectura que lee el rachivo Stack.in, y vacía su contenido en la variable programa.
Entrada:
	- programa: Puntero a la dirección de memoria en donde se almacenarán las instrucciones,
	este es un arreglo de string, y el string es un arreglo de caracteres.
		Primer puntero, apunta a la dirección de memoria de este arreglo de string
		Segundo puntero, apunta a la dirección de memoria de cada elemento del arreglo de string
		tercer puntero, apunta a la dirección de memoria del string en sí, es decir, la cadena de
			caracteres
	- push: puntero a entero que almacena la cantidad de instrucciones PUSH existentes en la máquina
Salida:
	- instrucciones: corresponde a la cantidad total de instrucciones existentes en la máquina.*/
int lectura(char *** programa, int* push){
	printf("\n******** LECTURA ********\n");
	/*Se definen las variables para la cantidad de instrucciones y el puntero a la dirección de memoria
	donde se encuentre el archivo cuando se abra*/
	int instrucciones;
	FILE *archivoEntrada;
	//Se abre el archivo, es decir se genera la conección entre el archivo y el programa
	archivoEntrada = fopen("Stack.in","r");
	//Se lee la primera linea del archivo, correspondiente a la cantidad de instrucciones de la máquina
	fscanf(archivoEntrada,"%d",&instrucciones);
	//Variable auxiliar para obtener lo que está en el archivo
	char variable1[20];
	//Se recorren las instrucciones del archivo para saber cuántas instrucciones PUSH existen
	for (int i=0;i<instrucciones;i++){
		//Se lee el primer string que se encuentra en la linea i +1 (ya se leyó la primera línea)
		fscanf(archivoEntrada,"%s",variable1);
		if (strcmp(variable1,"PUSH") == 0){
			/*Si lo leído es un PUSH, se debe identificar que es lo que se debe agregar*/
			instrucciones=instrucciones+1;//Se aumenta la cantidad de elementos en las instrucciones
			*push = *push + 1;//Se indica que hay una instrucción PUSH más
		}
	}
	fclose(archivoEntrada);//Se cierra el archivo
	//Se abre nuevamente el archivo, ahora para capturar en si las instrucciones de la máquina
	archivoEntrada = fopen("stack.in","r");
	int variable2;
	fscanf(archivoEntrada,"%d",&variable2);//Se lee la primera línea, la cual ya no es necesaria
	/*Se genera un puntero a un arreglo de string (cadena de char), el cual tiene el tamaño 
	instrucciones, recuerde que en el ciclo anterior la variable instrucciones aumento, y ahora
	posee la cantidad de palabras que hay en la máquina.*/
	*programa = (char **) malloc(sizeof(char *)*instrucciones);
	//Se recorre el archivo completo
	for (int i=0;i<instrucciones;i++){
		//Se reserva memoria para el string
		(*programa)[i] = (char *) malloc(sizeof(char )*10);
		//Se almacena el string
		fscanf(archivoEntrada,"%s",(*programa)[i]);
	}	
	fclose(archivoEntrada);
	return instrucciones;
}

/*Función que crea el stack de instrucciones a realizar
Entrada:
	- programa: Puntero a un string (cadena de caracteres) que representa las instrucciones de la
	máquina de stack
	- instrucciones: Indica la cantidad de instrucciones como número entero
Salida:
	- programaOrdenado: La máquina posee las instrucciones al revés, ahora se nvierten para que la
	máquina funcione correctamente*/
char ** crearStackInstrucciones(char ** programa,int instrucciones){
	char ** programaOrdenado;
	programaOrdenado = (char **) malloc(sizeof(char *)*instrucciones);
	for (int i=0;i<instrucciones;i++){
		if (strcmp(programa[i],"PUSH") == 0){
			programaOrdenado[instrucciones-(i+2)] = programa[i];	
			programaOrdenado[instrucciones-(i+1)] = programa[i+1];
			i++;
		}	
		else{
			programaOrdenado[instrucciones-(i+1)] = programa[i];
		}
		
	}

	free(programa);
	
	return programaOrdenado;

}
	
void escritura(int n){
	
	FILE *archivoSalida;
	archivoSalida = fopen("Salida.out","w");
	fprintf(archivoSalida,"%d",n);
	fclose(archivoSalida);
	
}

void mostrarStack(char ** stack,int instrucciones,char *  mensaje){
	
	printf("\n******** %s ********\n",mensaje);
	
	int i;
	for (i=instrucciones-1;i >= 0;i--){
		if(i<9)
			printf("Registro 0%d: %s\n",i+1,stack[i]);
		else		
			printf("Registro %d: %s\n",i+1,stack[i]);

	}	
}

void ejecutar(char ** programa, char ** stack, int instrucciones,int push){
	int i;
	printf("\n************************************\n");
	printf("******** EJECUCION PROGRAMA ********\n");
	printf("************************************\n\n");
	
	int primero = 0;
	
	for(i = 0; i<instrucciones;i++){
		
		printf("\n_______________________________________________________________\n");
		
		if (strcmp(programa[i],"PUSH") == 0){
			printf("\nInstruccion: %s %s\n",programa[i],programa[i+1]);
		
			i++;
			PUSH(&primero,&stack, programa[i]);			
		}
		else if(strcmp(programa[i],"POP") == 0){
			printf("\nInstruccion: %s \n",programa[i]);
		
			POP(&primero, &stack);
		}
		else if(strcmp(programa[i],"SUM") == 0){
			printf("\nInstruccion: %s \n",programa[i]);	
			SUM(&primero, &stack);
		}
		else if(strcmp(programa[i],"RES") == 0){
			printf("\nInstruccion: %s \n",programa[i]);	
			RES(&primero, &stack);
		}
		else if(strcmp(programa[i],"MUL") == 0){
			printf("\nInstruccion: %s \n",programa[i]);	
			MUL(&primero, &stack);
		}
		else if(strcmp(programa[i],"DIV") == 0){
			printf("\nInstruccion: %s \n",programa[i]);	
			DIV(&primero, &stack);
		}
		else if(strcmp(programa[i],"MOD") == 0){
			printf("\nInstruccion: %s \n",programa[i]);	
			MOD(&primero, &stack);
		}
		else if(strcmp(programa[i],"POT") == 0){
			printf("\nInstruccion: %s \n",programa[i]);	
			POT(&primero, &stack);
		}
		else if(strcmp(programa[i],"EXP") == 0){
			printf("\nInstruccion: %s \n",programa[i]);	
			EXP(&primero, &stack);
		}
		else if(strcmp(programa[i],"RAI") == 0){
			printf("\nInstruccion: %s \n",programa[i]);	
			RAI(&primero, &stack);
		}
		else{
			printf("\nInstruccion: %s (No se reconoce)\n",programa[i]);
		}	
		mostrarStack(stack,push,"STACK RESULTANTE");
	}
}

int main (){
	system("cls");
	printf("\n\n********************** INICIO DEL PROGRAMA **********************\n");

	
	int instrucciones;
	char ** programa; 
	int push =0;
	
	instrucciones = lectura(&programa,&push);


	printf("\n******** CREACION DEL STACK ********\n");
	
	char ** stack = (char **) malloc(sizeof(char *)*push);
	int i;
	for (i=0;i<push;i++){
		stack[i] = "";
	}
	
	printf("\nExisten %d instrucciones PUSH en el programa...\n",push);
	printf("por lo que se creo un estack de %d espacios...\n",push);

	printf("\n******** PROGRAMA LEIDO ********\n");
	int j;
	for (i=0,j=1;i<instrucciones;i++,j++){
		if (strcmp(programa[i],"PUSH") == 0){
			printf("instruccion %d: %s %s\n",j,programa[i],programa[i+1]);
			i++;
		}
		else 
			printf("instruccion %d: %s\n",j,programa[i]);

	}

	mostrarStack(stack,push,"STACK INICIAL");
	
	//Se ordenan las instrucciones del modo que seran ejecutadas
	programa = crearStackInstrucciones(programa,instrucciones);

	ejecutar(programa, stack, instrucciones,push);
	
	for(i=0;i<instrucciones;i++){
		free(programa[i]);
	
	}
	for(i=0;i<push;i++){
		if(strcmp(stack[i],"")!=0)
			free(stack[i]);	
	}
	free(programa);
	free(stack);
	
	printf("\n\n********************** FIN DEL PROGRAMA **********************\n");
	
	return 0;

}