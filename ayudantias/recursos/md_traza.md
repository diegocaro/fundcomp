# Ayudantía: Métodos de trazas para códigos

### Universidad de Santiago de Chile

##### Fundamentos de Computación 2021-1

##### Profesor: Diego Caro (diego.caro.a@usach.cl)

##### Ayudante: Clemente Aguilar (clemente.aguilar@usach.cl)

---

**OJO!** El siguiente desarrollo detalla **dos formas** simples, versátiles y comprensibles de realizar trazas. El aspecto más importante de una traza es que **logre describir el código de la forma más clara posible**. Si tu método de escribir trazas es distinto a los entregadas a continuación, pero explica con **claridad** lo que hace el código, entonces **<u>tu método es correcto</u>**.

Dado el siguiente pseudocódigo:

~~~
read x, y, z
if x < y:
	for i = 1 to 3:
		x = x * i
		print "x fue ponderado por", i

if x > z:
	k = 1
	while k <= 4:
		z = z + k
		print "esta es la iteración n° ", k
		k = k + 1

print x + y + z
~~~

Escribiremos la traza correspondiente para los valores  $x=3,\ y=7,\ z=2$:

## Método 1:

|       -        |  x   |  y   |  z   | x<y  |  i   | x>z  |  k   | k<=4 |
| :------------: | :--: | :--: | :--: | :--: | :--: | :--: | :--: | :--: |
|                |  3   |  7   |  2   |  -   |  -   |  -   |  -   |  -   |
|    if x < y    |  3   |  7   |  2   |  V   |  -   |  -   |  -   |  -   |
| for i = 1 to 3 |  3   |  7   |  2   |  V   |  1   |  -   |  -   |  -   |
| for i = 1 to 3 |  3   |  7   |  2   |  V   |  2   |  -   |  -   |  -   |
| for i = 1 to 3 |  6   |  7   |  2   |  V   |  3   |  -   |  -   |  -   |
|    if x > z    |  6   |  7   |  2   |  -   |  3   |  V   |  -   |  -   |
|  while k <= 4  |  6   |  7   |  2   |  -   |  3   |  V   |  1   |  V   |
|  while k <= 4  |  6   |  7   |  3   |  -   |  3   |  V   |  2   |  V   |
|  while k <= 4  |  6   |  7   |  5   |  -   |  3   |  V   |  3   |  V   |
|  while k <= 4  |  6   |  7   |  8   |  -   |  3   |  F   |  4   |  V   |
|  while k <= 4  |  6   |  7   |  12  |  -   |  3   |  F   |  5   |  F   |



#### Explicación traza:

Este método se centra en mantener un registro de las **variables y operaciones de comparación** presentes en el código. Se actualizan los valores de cada variable al ser modificados, al igual que los valores booleanos de las comparaciones. 

Al ir constantemente registrando el estado de las variables utilizadas, este método nos asegurará obtener en la última fila de nuestra traza el valor con el que las variables llegan al término de la ejecución del código.


## Método 2:

|  x   |  y   |  z   |  i   |  k   |         imprimir          |
| :--: | :--: | :--: | :--: | :--: | :-----------------------: |
|  3   |  7   |  2   |      |      |                           |
|      |      |      |  1   |      |                           |
|  3   |      |      |      |      |                           |
|      |      |      |      |      |   x fue ponderado por 1   |
|      |      |      |  2   |      |                           |
|  6   |      |      |      |      |                           |
|      |      |      |      |      |   x fue ponderado por 2   |
|      |      |      |  3   |      |                           |
|      |      |      |      |  1   |                           |
|      |      |  3   |      |      |                           |
|      |      |      |      |      | esta es la iteración n° 1 |
|      |      |      |      |  2   |                           |
|      |      |  5   |      |      |                           |
|      |      |      |      |      | esta es la iteración n° 2 |
|      |      |      |      |  3   |                           |
|      |      |  8   |      |      |                           |
|      |      |      |      |      | esta es la iteración n° 3 |
|      |      |      |      |  4   |                           |
|      |      |  12  |      |      |                           |
|      |      |      |      |      | esta es la iteración n° 4 |
|      |      |      |      |  5   |                           |
|      |      |      |      |      |            25             |



#### Explicación traza:

Este método registra cada **actualización de variable y output** dentro del código. Cada fila de la traza corresponde a una línea de código donde se inicializa o modifica una variable, o se genera un output por pantalla (print).

Este método asegura que el último valor de cada columna corresponde al estado de cada variable, o el último output al finalizar la ejecución del código.

\pagebreak

La traza debe describir el proceso del pseudocódigo para los valores dados ($x=2,\ y=7,\ z=3$).

Este formato de traza se preocupa de **llevar un seguimiento de cada variable y output** (imprimir y/o retornar) dentro del código.

Antes de iniciar el análisis línea por línea, recomiendo escribir cada variable presente en el código en su columna correspondiente. Para nuestro caso, estas variables serán `x, z, i, j`. También dedicamos una columna para los mensajes que serán impresos por pantalla.

* La primera línea del código nos pide leer `x, y ` y `z`, por lo que anotaremos sus valores en la tabla. Como estos valores son registrados en una misma operación, los escribimos en la misma fila.

* Luego se pregunta en el condicional por `x < y`. Como esto se cumple, entramos al `Si`. _**¡Recuerda!**, este método de traza solo registra outputs, creación y cambio de variables. Como esta línea no imprime nada, ni modifica ni crea variables, no hay necesidad de anotar el condicional en la tabla_.

* Una vez dentro, encontramos un ciclo `Para`. Este ciclo itera en base a una variable `i` inicializada en `i = 1`, por lo que se registra en la tabla. El ciclo `Para` funciona aumentando nuestra variable `i` en 1 **al final de cada iteración**. Por último, en esta línea se especifica el límite de iteración del ciclo. Para este caso, cuando `i` sea igual a 3, el ciclo dejará de iterar.

* La primera línea dentro del ciclo modifica nuestro `x`, por lo que nuestra variable `x` tendrá un nuevo valor en nuestra tabla. Para esta iteración, ese valor será -2.

* La siguiente línea imprime un mensaje por pantalla, el cual será anotado en la tabla.

* Como llegamos al fin de nuestra iteración, nuestra variable `i` va a aumentar en 1, modificando su valor en la tabla.

* Nuestro ciclo `Para` vuelve a iniciar, pero esta vez con la variable `i = 2`. Como `i` aún no es igual a 3, el ciclo vuelve a ejecutarse.

* El valor de `x` vuelve a cambiar, siendo registrado en la tabla.

* La siguiente línea imprime un mensaje por pantalla, el cual será anotado en la tabla.

* Llegamos de nuevo al fin del ciclo, por lo que `i` aumenta en 1.

* Volvemos al ciclo `Para`, pero como nuestra variable `i` es 3, llegamos al tope de la condición del ciclo (`hasta i = 3`), por lo que no se volverá a iterar. Pasamos a la siguiente línea (`línea 6`).

* En esta línea encontramos otro condicional: `Si y < z:`. Notemos que esto no se cumple para los valores con los que estamos escribiendo la traza (`y = 7, z = 3`). 

  _**¿Qué implica esto?** Significa que toda las operaciones dentro del condicional **no serán ejecutadas**. Es así que cualquier modificación de variable o mensaje impreso **no ocurrirá**, por lo que no debemos anotarla en nuestra traza._

* Es así que llegamos a la última línea de nuestro pseudocódigo, donde se imprime por pantalla el valor de `x + y + z`, anotándolo en nuestra tabla.



¡Y así se pueden hacer trazas de pseudocódigo! Para seguir practicando, te recomiendo realizar la traza utilizando el método que más te para los siguientes valores:

* $x=4,\ y=4,\ z=9$
* $x=1,\ y=1,\ z=1$

**¡Éxito!**