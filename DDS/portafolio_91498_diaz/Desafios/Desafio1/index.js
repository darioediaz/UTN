// Importacion de libreria
const seedrandom = require("seedrandom");

// Creacion de semilla
let semilla = seedrandom(1763519);

// Generar 1000000 de numeros aleatorios enteros
let cantidadNumeros = 1000000;

// Variables necesarias
let vectorNumeros = [];
let contPositivos = 0;
let contNegativos = 0;
let contNumerosResto0356 = 0;
let numerosAnteultimoDigito = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0];
let menorNumero = 0;
let menorNumeroIndice = 0;
let numeroActual = null;
let numeroAnterior = true;
let contSignoIgualAlAnterior = 0;
let sumNumero6Digitos = 0;
let contNumero6Digitos = 0;
let promedio = null;

// Crear el arreglo de numeros aleatorios usando el metodo int32
for (let i = 0; i < cantidadNumeros; i++) {
  const numeroAleatorio = semilla.int32();
  vectorNumeros.push(numeroAleatorio);
}

// Mostrar vector creado
console.log(vectorNumeros);

// Punto 1.
// Cantidad de números positivos y cantidad de números negativos.
for (elem of vectorNumeros) {
  if (elem > 0) {
    contPositivos++;
  } else {
    contNegativos++;
  }
}

// Punto 2.
// Cantidad de números cuyo resto al dividirlos en 7 sea exactamente 0, 3, 5 o 6.
for (elem of vectorNumeros) {
  if (elem % 7 == 0 || elem % 7 == 3 || elem % 7 == 5 || elem % 7 == 6) {
    contNumerosResto0356++;
  }
}

// Punto 3.
// Un arreglo de contadores que indique la cantidad de números según su anteúltimo dígito (el de las decenas)
// coincida con el índice. De esta manera el número 2134 debe contarse en la posición 3 del arreglo, el número
// 32405 en la posición 0 del arreglo y así sucesivamente.
// Evidentemente el arreglo va a ser de 10 contadores con índices del 0 al 9 y deberá ser cargado usando
// llaves y valores separados por comas.
// Obtener el anteultimo digito del numero
for (elem of vectorNumeros) {
  let anteultimoDigito = Math.floor(Math.abs(elem / 10) % 10);

  // Incrementar el contador correspondiente al anteultimo digito
  numerosAnteultimoDigito[anteultimoDigito]++;
}

// Punto 4.
// Valor y posición del menor de todos. La posición del primer número generado debe considerarse como 1,
// es decir no se pide el índice del valor en el arreglo sino el número de orden del mismo.
for (let i = 1; i < vectorNumeros.length; i++) {
  if (vectorNumeros[i] < menorNumero) {
    menorNumero = vectorNumeros[i];
    menorNumeroIndice = i + 1;
  }
}

// Punto 5.
// Cantidad de números cuyo signo sea igual al del anterior, evidentemente el primer elemento del conjunto
// no puede ser contabilizado porque no tiene anterior, es decir el máximo posible es la cantidad de elementos
// generados menos 1.
// Verificar si el número actual tiene el mismo signo que el número anterior con funcion Math
for (elem of vectorNumeros) {
  if (
    numeroAnterior !== null &&
    Math.sign(elem) === Math.sign(numeroAnterior)
  ) {
    contSignoIgualAlAnterior++;
  }
  // Almacenar el numero actual como el numero anterior para la proxima iteracion
  numeroAnterior = elem;
}

// Punto 6.
// Promedio entero (redondeado con Math.round) de todos los números que contengan exactamente 6 dígitos.
for (elem of vectorNumeros) {
  let elemTexto = elem.toString();
  if (elem > 0 && elemTexto.length === 6) {
    sumNumero6Digitos += elem;
    contNumero6Digitos++;
  }
  if (elem < 0 && elemTexto.length === 7) {
    sumNumero6Digitos += elem;
    contNumero6Digitos++;
  }
}

if (contNumero6Digitos > 0) {
  promedio = Math.round(sumNumero6Digitos / contNumero6Digitos);
}

// Resultados
console.log(
  "----------------------------------------------------------------------------------------------"
);
console.log(
  "----------------------------------------------------------------------------------------------"
);
console.log("Resultados:");

// Punto 1.
console.log("Cantidad de numeros positivos: ", contPositivos);
console.log("Cantidad de numeros negativos: ", contNegativos);

// Punto 2.
console.log(
  "Cantidad de numeros con resto 0, 3, 5 o 6: ",
  contNumerosResto0356
);

// Punto 3.
console.log("El arreglo de contadores es: " + numerosAnteultimoDigito);

// Punto 4.
console.log("El menor numero del arreglo es: ", menorNumero);
console.log("El indice del menor numero del arreglo es: ", menorNumeroIndice);

// Punto 5.
console.log(
  "La cantidad de numeros con signo igual a su anterior es de: ",
  contSignoIgualAlAnterior
);

// Punto 6.
console.log("El promedio de todos los numeros con 6 digitos es de: ", promedio);

console.log(
  "----------------------------------------------------------------------------------------------"
);
console.log(
  "----------------------------------------------------------------------------------------------"
);
