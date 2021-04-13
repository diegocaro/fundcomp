#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <math.h>

void mostrarRegistros(int numRegistros,int * registros,int i);
void lectura(char **** programa,int * instrucciones, int * numRegistros, int ** registros);
void mostrarInstruccion(char *** programa, int i);
void ejecutar(int numRegistros,int * registros, int instrucciones, char *** programa);
char * eliminarL(char * L);


void lectura(char **** programa,int * instrucciones, int * numRegistros, int ** registros){
	printf("\n******** LECTURA ********\n");
	
	FILE *archivoEntrada;
	
	int i,j;
		
	archivoEntrada = fopen("Registros.in","r");	
	fscanf(archivoEntrada,"%d",numRegistros);
	
	(* registros) = (int *) malloc(sizeof(int)* ((*numRegistros) + 1)); 
	
	for (i = 0 ; i< (*numRegistros)+1;i++){
		fscanf(archivoEntrada,"%d",&(*registros)[i]);	
	}
	
	
	fscanf(archivoEntrada,"%d",instrucciones);
	
	(*programa) = (char ***)  malloc(sizeof (char **) * (*instrucciones));
	
	for (i = 0 ; i < (*instrucciones); i++){
		(*programa)[i] = malloc(sizeof(char *)*5);
		for(j=0;j<5;j++){
			(*programa)[i][j] = malloc(sizeof(char *)*10);
		}
	}
	
	for (i=0;i<(*instrucciones);i++){
		
		fscanf(archivoEntrada,"%s",(*programa)[i][0]);		
		fscanf(archivoEntrada,"%s",(*programa)[i][1]);
		if (strcmp((*programa)[i][1],"HALT") != 0){
			fscanf(archivoEntrada,"%s",(*programa)[i][2]);
		
			fscanf(archivoEntrada,"%s",(*programa)[i][3]);
			fscanf(archivoEntrada,"%s",(*programa)[i][3]);
			
			if (strcmp((*programa)[i][1],"R-") == 0){
				fscanf(archivoEntrada,"%s",(*programa)[i][4]);
			}
			else{
				(*programa)[i][4] = "-";
				
			}
		}
	}

	fclose(archivoEntrada);
}

void mostrarRegistros(int numRegistros,int * registros, int L){
	
	
	
	int i;

	printf("Etiqueta actual: L%d\n\n",L);
	
	for(i=1;i<numRegistros+1;i++){
		if (i<9)
			printf("Registro 0%d: %d\n",i-1,registros[i]);
		else
			printf("Registro %d: %d\n",i-1,registros[i]);
	} 
	printf("\n\n");
	return;
}

void mostrarInstruccion(char *** programa, int i){
	
	int j;
	printf("Instruccion ejecutada: ");
	
	for (j=0;j<4;j++){
		if(j==3)
		printf("-> ");
			
		printf("%s ",programa[i][j]);
	}	
	if (strcmp((programa)[i][1],"R-") == 0)
		printf("%s ",programa[i][4]);
	printf("\n\n");
	
}

char * eliminarL(char * L){
	int i;
	char  * L2 = malloc(sizeof(char)*10);
	for (i=0;i<10;i++){
		L2[i]=L[i+1];
	}
	return L2;
}

void ejecutar(int numRegistros,int * registros, int instrucciones, char *** programa){

	printf("\n\n**************************************\n");
	printf("********* EJECUTAR PROGRAMA **********\n");
	printf("**************************************\n");

	int i = 0;
	
	
	int j;	
	char * x;
	while (strcmp(programa[i][1],"HALT") != 0){
		
		int reg = atoi(programa[i][2]);
			
		if(strcmp((programa)[i][1],"R-") == 0){
			if(registros[reg+1] > 0){
				registros[reg+1] = registros[reg+1] - 1;
				x = eliminarL(programa[i][3]);
			}
			else{
				x = eliminarL(programa[i][4]);
			}
		}
		else if(strcmp((programa)[i][1],"R+") == 0){
				registros[reg+1] = registros[reg+1] + 1;
				x = eliminarL(programa[i][3]);
			
		}

		printf("\n****** REGISTROS ACTUALES ******\n");

		mostrarInstruccion(programa, i);

		i= atoi(x);
		free(x);

		mostrarRegistros(numRegistros,registros,i);
	}
	printf("************* FIN DE LA EJECUCION ***************\n");
	
	printf("************* REGISTROS FINALES ***************\n");

	mostrarRegistros(numRegistros,registros,i);

	
}

int main (){
	system("cls");

	printf("\n******** INICIO DEL PROGRAMA ********\n");

	
	char *** programa;
	int  instrucciones;
	int  numRegistros;
	int * registros;
	
	lectura(&programa, &instrucciones,&numRegistros,&registros);

	printf("Hay %d instrucciones\n",instrucciones);
	printf("Hay %d registros\n",numRegistros);
	

	printf("\n******** INSTRUCCIONES ********\n");
	
	int i,j;	
	
	for(i=0;i<instrucciones;i++){
		for(j=0;j<5;j++){
			printf("%s ",programa[i][j]);
		}
		printf("\n");
	}
	
	mostrarRegistros(numRegistros,registros,registros[0]);

	ejecutar(numRegistros,registros, instrucciones, programa);

	printf("************* FIN DEL PROGRAMA ***************\n");
		
	return 0;
}