/* 
Resultados:
1) 499606
2) 500394
3) 571411
4) {100174, 99809, 99650, 100141, 99897, 99920, 99850, 99651, 100421, 100487}
5) -2147480057:406724
6) 500379
7) -21810
*/

"use strict";

import seedrandom from "seedrandom";

// Establecer la semilla
var random = seedrandom(1763519);

// Generar 1M numeros aleatorios
let numerosAleatorios = Array.from({ length: 1000000 }, () => random.int32());

// Demostracion de forEach para iterar sobre los elementos del array
// console.log("Demostracion de join: {" + numerosAleatorios.join(", ") + "}");

// Punto 1...
// Demostracion de filter para buscar los numeros positicos
console.log(
  "1. Cantidad de numeros positivos: ",
  numerosAleatorios.filter((value) => value > 0).length
);

// Demostracion de filter para mostrar los numeros negativos
console.log(
  "2. Cantidad de numeros negativos: ",
  numerosAleatorios.filter((value) => value < 0).length
);

// Punto 3.
let numDivisiblePor7Resto0_3_5_6 = 0;

// Por cada valor del array verificar si el resto al dividirlo por 7 es 0, 3, 5 o 6
numerosAleatorios.forEach((value) => {
  if (value % 7 == 0 || value % 7 == 3 || value % 7 == 5 || value % 7 == 6) {
    numDivisiblePor7Resto0_3_5_6++;
  }
});

console.log(
  "3. Cantidad de numeros divisibles por 7 con resto 0, 3, 5 o 6: ",
  numDivisiblePor7Resto0_3_5_6
);

// Punto 4...
let numAnteultimoDigito = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0];

numerosAleatorios.forEach((value) => {
  let anteultimoDigito = Math.floor(Math.abs((value / 10) % 10));
  numAnteultimoDigito[anteultimoDigito]++;
});

console.log("4. Conteo de anteúltimos dígitos: " + numAnteultimoDigito);

//Punto 5...
let menorNumero = null;
let menorIndice = null;

for (let i = 0; i < numerosAleatorios.length; i++) {
  if (numerosAleatorios[i] < menorNumero) {
    menorNumero = numerosAleatorios[i];
    menorIndice = i + 1;
  }
}

console.log(
  "5. El menor numero es: ",
  menorNumero,
  " y su indice es: ",
  menorIndice
);

// Punto 6...
let anterior = null;
let numerosDeIgualSignoASuAnterior = 0;

numerosAleatorios.forEach((value) => {
  if (anterior !== null && Math.sign(anterior) === Math.sign(value)) {
    numerosDeIgualSignoASuAnterior++;
  } else {
    anterior = value;
  }
});

console.log(
  "6. Cantidad de numeros de signo igual a su anterior: ",
  numerosDeIgualSignoASuAnterior
);

// Punto 7...
let sumadorNumeros6Digitos = 0;
let contadorNumeros6Digitos = 0;

numerosAleatorios.forEach((value) => {
  let valueTexto = value.toString();
  if (
    (value < 0 && valueTexto.length == 7) ||
    (value > 0 && valueTexto.length == 6)
  ) {
    sumadorNumeros6Digitos += value;
    contadorNumeros6Digitos++;
  }
});

if (contadorNumeros6Digitos > 0) {
  let promedio = Math.round(sumadorNumeros6Digitos / contadorNumeros6Digitos);
  console.log("7. El promedio es de: ", promedio);
}
