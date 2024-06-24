// Lectura del archivo JSON
const fs = require("fs");

fs.readFile("./personas.json", "utf-8", (error, data) => {
  if (error) {
    console.error("Error al leer el archivo:", error);
  } else {
    const json = JSON.parse(data);
    // Aca se podrian manipular los datos JSON
    const coleccion = [];

    for (let i = 0; i < json.length; i++) {
      const objeto = json[i];
      coleccion.push(objeto);
    }

    // console.log(coleccion);

    console.log(
      "--------------------------------------------------------------------------------------------------------------------------------"
    );
    console.log(
      "--------------------------------------------------------------------------------------------------------------------------------"
    );
    console.log("Resultados");

    // 1. Calcular el promedio entero de las edades de todas las personas del archivo
    let cantidadPersonas = 0;
    let sumaEdades = 0;

    for (elem of coleccion) {
      cantidadPersonas++;
      sumaEdades += elem.edad;
    }
    if (cantidadPersonas > 0) {
      let promedioEdades = sumaEdades / cantidadPersonas;
      console.log("El promedio de edades es de: ", Math.round(promedioEdades));
    }

    // 2. Informar el Nombre y Apellido de la persona más joven del conjunto (si hubiere más de una persona con
    // esa misma edad debe informar la primera que aparezca en el archivo).
    let menorEdad = null;
    let menorEdadNombre = null;
    let menorEdadApellido = null;

    for (elem of coleccion) {
      if (menorEdad == null) {
        menorEdad = elem.edad;
        menorEdadNombre = elem.nombre;
        menorEdadApellido = elem.apellido;
      } else {
        if (elem.edad < menorEdad) {
          menorEdad = elem.edad;
          menorEdadNombre = elem.nombre;
          menorEdadApellido = elem.apellido;
        }
      }
    }
    console.log(
      "La persona de menor edad es: ",
      menorEdadNombre,
      menorEdadApellido
    );

    // 3. Informar los Nombres separados por coma ", " de todas las personas con apellido GOMEZ, ordenados alfabéticamente.
    let coleccionGomez = [];

    for (elem of coleccion) {
      if (elem.apellido == "GOMEZ") {
        coleccionGomez.push(elem.nombre);
      }
    }
    if (coleccionGomez.length == 0) {
      console.log("No hay personas con apellido GOMEZ en esta lista");
    } else {
      console.log(
        "Cantidad de personas con appellido GOMEZ en esta lista: ",
        coleccionGomez.length
      );
      console.log(coleccionGomez.sort());
    }

    // 3. Suma de las edades de aquellas personas cuyo nombre tenga una longitud par y el  apellido una longitud impar.
    let sumaEdadesNombreParApellidoImpar = 0;

    for (elem of coleccion) {
      if (elem.nombre.length % 2 == 0 && elem.apellido.length % 2 != 0) {
        sumaEdadesNombreParApellidoImpar += elem.edad;
      }
    }

    console.log(
      "La edad total de personas con cantidad de letras par en sus nombres y cantidad de letras impar en sus apellidos es de :",
      sumaEdadesNombreParApellidoImpar
    );

    // 4. Construir una funcionalidad que genere un objeto en su notación JSON que contenga los siguientes atributos o propiedades:
    // - mayores: cantidad de personas con edad > 18
    // - menores: cantidad de personas con edad <= 18
    // - primeraMitad: cantidad de personas cuyo apellido comienza con A-L
    // - segundaMitad: cantidad de personas cuyo apellido comienza con M-Z

    function generarJsonPersonas(coleccion) {
      let mayores = 0;
      let menores = 0;
      let primeraMitad = 0;
      let segundaMitad = 0;

      for (elem of coleccion) {
        if (elem.edad > 18) {
          mayores++;
        } else {
          menores++;
        }
      }

      for (elem of coleccion) {
        if (elem.apellido >= "A" && elem.apellido < "M") {
          primeraMitad++;
        } else {
          segundaMitad++;
        }
      }

      const estadisticasJSON = {
        mayores: mayores,
        menores: menores,
        primeraMitad: primeraMitad,
        segundaMitad: segundaMitad,
      };
      return JSON.stringify(estadisticasJSON);
    }
    let resultadoFuncionGenerarJsonPersonas = generarJsonPersonas(coleccion);

    console.log(
      "Los resultados del punto 4 son los siguientes: ",
      resultadoFuncionGenerarJsonPersonas
    );

    // 5. Construir una funcionalidad que genere un objeto en su notación JSON que contenga los siguientes atributos, cuyos valores
    // deben ser la cantidad de personas correspondientes a cada apellido:
    // - CASTILLO
    // - DIAZ
    // - FERRER
    // - PINO
    // - ROMERO

    function generarJSONPorApellidos(coleccion) {
      let castillo = 0;
      let diaz = 0;
      let ferrer = 0;
      let pino = 0;
      let romero = 0;

      for (elem of coleccion) {
        if (elem.apellido == "CASTILLO") {
          castillo++;
        } else if (elem.apellido == "DIAZ") {
          diaz++;
        } else if (elem.apellido == "FERRER") {
          ferrer++;
        } else if (elem.apellido == "PINO") {
          pino++;
        } else if (elem.apellido == "ROMERO") {
          romero++;
        }
      }

      const estadisticasJSON = {
        castillo: castillo,
        diaz: diaz,
        ferrer: ferrer,
        pino: pino,
        romero: romero,
      };

      return JSON.stringify(estadisticasJSON);
    }
    let resultadoFuncionGenerarJSONPorApellidos =
      generarJSONPorApellidos(coleccion);

    console.log(
      "Los resultados del punto 5 son los siguientes: ",
      resultadoFuncionGenerarJSONPorApellidos
    );
    console.log(
      "--------------------------------------------------------------------------------------------------------------------------------"
    );
    console.log(
      "--------------------------------------------------------------------------------------------------------------------------------"
    );
  }
});
