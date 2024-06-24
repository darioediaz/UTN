const cargarPaquetes = () => {
  const paquetes = fetch("http://localhost:3000/paquetes");
  paquetes
    .then((respuesta) => {
      return respuesta.json();
    })
    .then((paquetes) => {
      const listaPaquetes = document.getElementById("lista-paquetes");
      listaPaquetes.innerHTML = ""; // Limpiar lista existente antes de agregar nuevas entradas
      for (let paquete of paquetes) {
        const row = `
          <tr>
            <td>${paquete.destino}</td>
            <td>${paquete.duracion}</td>
            <td>${paquete.precio}</td>
            <td>${paquete.descripcion}</td>
            <td><button onclick="eliminarPaquete('${paquete.id}')" type="button" class="btn btn-danger">Eliminar</button></td>
          </tr>
        `;
        listaPaquetes.innerHTML += row; // Agregar fila a la tabla
      }
    })
    .catch((error) => console.log("Error al cargar los paquete: ", error));
};

// Obtener una referencia al elemento de la tabla donde se mostraran los paquetes
const listaPaquetes = document.getElementById("lista-paquetes");

// Funcion para agregar un paquete a la lista
const agregarPaquete = (paquete) => {
  // Validar que se carguen todos los datos
  const destino = document.getElementById("destino").value;
  const duracion = document.getElementById("duracion").value;
  const precio = document.getElementById("precio").value;
  const descripcion = document.getElementById("descripcion").value;

  if (!destino || !duracion || !precio || !descripcion) {
    alert("Por favor, ingresa todos los datos para realizar la carga");
    return;
  }

  fetch("http://localhost:3000/paquetes", {
    method: "POST",
    headers: {
      "Content-Type": "application/json",
    },
    body: JSON.stringify(paquete),
  })
    .then((response) => response.json())
    .then((data) => {
      cargarPaquetes();
    })
    .catch((error) => {
      console.log("Error al agregar el paquete:", error);
    });
};

// Funcion para eliminar un paquete de la lista
const eliminarPaquete = (id) => {
  fetch(`http://localhost:3000/paquetes/${id}`, {
    method: "DELETE",
  })
    .then((response) => {
      cargarPaquetes();
    })
    .catch((error) => {
      console.log("Error al eliminar el paquete:", error);
    });
};

// Obtener una referencia al boton de agregar paquete
const agregarPaqueteBtn = document.getElementById("agregar-paquete-btn");

// Evento click para agregar un paquete a la lista
agregarPaqueteBtn.addEventListener("click", function () {
  const destino = document.getElementById("destino").value;
  const duracion = document.getElementById("duracion").value;
  const precio = document.getElementById("precio").value;
  const descripcion = document.getElementById("descripcion").value;

  // Crear un objeto paquete con los valores ingresados
  const paquete = {
    destino: destino,
    duracion: duracion,
    precio: precio,
    descripcion: descripcion,
  };

  // Agregar el paquete a la tabla
  agregarPaquete(paquete);

  // Limpiar los campos de entrada
  document.getElementById("destino").value = "";
  document.getElementById("duracion").value = "";
  document.getElementById("precio").value = "";
  document.getElementById("descripcion").value = "";
});
cargarPaquetes();

// Funcion para filtrar paquetes
