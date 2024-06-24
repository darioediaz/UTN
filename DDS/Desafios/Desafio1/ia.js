// Importar la librería seedrandom
const seedrandom = require('seedrandom');

// Semilla para generar los números aleatorios
const seed = '1763519';

// Generar una instancia de la función de generación de números aleatorios
const rng = seedrandom(seed);

// Función para generar números aleatorios enteros utilizando int32
function getRandomInt32() {
  return rng.int32();
}

// Generar 1,000,000 de números aleatorios enteros
const numbers = Array.from({ length: 1000000 }, getRandomInt32);

// Cantidad de números positivos y negativos
let positiveCount = 0;
let negativeCount = 0;

// Cantidad de números con resto 0, 3, 5 o 6 al dividir por 7
let countMod7_0 = 0;
let countMod7_3 = 0;
let countMod7_5 = 0;
let countMod7_6 = 0;

// Arreglo de contadores según el anteúltimo dígito
const digitCounters = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0];

// Valor y posición del menor número
let minNumber = numbers[0];
let minNumberPosition = 1;

// Cantidad de números con el mismo signo que el anterior
let sameSignCount = 0;

// Suma de números con exactamente 6 dígitos
let sumSixDigitNumbers = 0;
let sixDigitCount = 0;

// Recorrer los números generados
for (let i = 0; i < numbers.length; i++) {
  const number = numbers[i];

  // Contar números positivos y negativos
  if (number > 0) {
    positiveCount++;
  } else if (number < 0) {
    negativeCount++;
  }

  // Contar números según el resto al dividir por 7
  const mod7 = Math.abs(number % 7);
  if (mod7 === 0) {
    countMod7_0++;
  } else if (mod7 === 3) {
    countMod7_3++;
  } else if (mod7 === 5) {
    countMod7_5++;
  } else if (mod7 === 6) {
    countMod7_6++;
  }

  // Contar números según el anteúltimo dígito
  const secondToLastDigit = Math.floor(Math.abs(number) / 10) % 10;
  digitCounters[secondToLastDigit]++;

  // Encontrar el menor número y su posición
  if (number < minNumber) {
    minNumber = number;
    minNumberPosition = i + 1;
  }

  // Contar números con el mismo signo que el anterior
  if (i > 0 && Math.sign(number) === Math.sign(numbers[i - 1])) {
    sameSignCount++;
  }

  // Sumar números con exactamente 6 dígitos
  if (Math.abs(number) >= 100000 && Math.abs(number) < 1000000) {
    sumSixDigitNumbers += number;
    sixDigitCount++;
  }
}

// Promedio entero de los números con 6 dígitos
const avgSixDigitNumbers = Math.round(sumSixDigitNumbers / sixDigitCount);

// Imprimir los resultados
console.log('Cantidad de números positivos:', positiveCount);
console.log('Cantidad de números negativos:', negativeCount);
console.log('Cantidad de números con resto 0:', countMod7_0);
console.log('Cantidad de números con resto 3:', countMod7_3);
console.log('Cantidad de números con resto 5:', countMod7_5);
console.log('Cantidad de números con resto 6:', countMod7_6);
console.log('Cantidad de números totales:', (countMod7_0+countMod7_3+countMod7_5+countMod7_6));
console.log('Arreglo de contadores:'+ digitCounters);
console.log('Valor del menor número:', minNumber);
console.log('Posición del menor número:', minNumberPosition);
console.log('Cantidad de números con el mismo signo que el anterior:', sameSignCount);
console.log('Promedio entero de números con 6 dígitos:', avgSixDigitNumbers);