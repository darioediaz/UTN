const cargarMuseos = () => {
  const museos = fetch("http://localhost:3000/api/museos");
  museos
    .then((respuesta) => {
      return respuesta.json();
    })
    .then((museos) => {
      const listaMuseos = document.getElementById("lista-museos");
      listaMuseos.innerHTML = ""; // Limpiar lista existente antes de agregar nuevas entradas
      for (let museo of museos) {
        const row = `
          <tr>
            <td>${museo.nombre}</td>
            <td>${museo.ubicacion}</td>
            <td>${museo.exposiciones}</td>
            <td>${museo.horarios}</td>
            <td>${museo.precioEntrada}</td>
            <td><button onclick="eliminarMuseo('${museo.id}')" type="button" class="btn btn-danger">Eliminar</button></td>
          </tr>
        `;
        listaMuseos.innerHTML += row; // Agregar fila a la tabla
      }
    })
    .catch((error) => console.log("Error al cargar los museos: ", error));
};

// Obtener una referencia al elemento de la tabla donde se mostraran los museos
const listaMuseos = document.getElementById("lista-museos");

// Funcion para agregar un museo a la lista
const agregarMuseo = (museo) => {
  // Validar que se carguen todos los datos
  const nombre = document.getElementById("nombre").value;
  const ubicacion = document.getElementById("ubicacion").value;
  const exposiciones = document.getElementById("exposiciones").value;
  const horarios = document.getElementById("horarios").value;
  const precioEntrada = document.getElementById("precio").value;

  if (!nombre || !ubicacion || !exposiciones || !horarios || !precioEntrada) {
    alert("Por favor, ingresa todos los datos para realizar la carga");
    return;
  }

  fetch("http://localhost:3000/api/museos", {
    method: "POST",
    headers: {
      "Content-Type": "application/json",
    },
    body: JSON.stringify(museo),
  })
    .then((response) => response.json())
    .then((data) => {
      cargarMuseos();
    })
    .catch((error) => {
      console.log("Error al agregar el museo:", error);
    });
};

// Funcion para eliminar un museo de la lista
const eliminarMuseo = (id) => {
  fetch(`http://localhost:3000/api/museos/${id}`, {
    method: "DELETE",
  })
    .then((response) => {
      cargarMuseos();
    })
    .catch((error) => {
      console.log("Error al eliminar el museo:", error);
    });
};

// Obtener una referencia al boton de agregar museo
const agregarMuseoBtn = document.getElementById("agregar-museo-btn");

// Evento click para agregar un museo a la lista
agregarMuseoBtn.addEventListener("click", function () {
  const nombre = document.getElementById("nombre").value;
  const ubicacion = document.getElementById("ubicacion").value;
  const exposiciones = document.getElementById("exposiciones").value;
  const horarios = document.getElementById("horarios").value;
  const precioEntrada = document.getElementById("precio").value;

  // Crear un objeto museo con los valores ingresados
  const museo = {
    nombre: nombre,
    ubicacion: ubicacion,
    exposiciones: exposiciones,
    horarios: horarios,
    precioEntrada: precioEntrada,
  };

  // Agregar el museo a la tabla
  agregarMuseo(museo);

  // Limpiar los campos de entrada
  document.getElementById("nombre").value = "";
  document.getElementById("ubicacion").value = "";
  document.getElementById("exposiciones").value = "";
  document.getElementById("horarios").value = "";
  document.getElementById("precio").value = "";
});
cargarMuseos();
