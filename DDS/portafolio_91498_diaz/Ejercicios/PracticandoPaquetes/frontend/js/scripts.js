const apiUrl = "http://localhost:3000/paquetes"; // Reemplaza con la URL de tu API

// Función para cargar la grilla de paquetes
const cargarPaquetes = async () => {
  try {
    const response = await fetch(apiUrl);
    const paquetes = await response.json();
    const listaPaquetes = document.getElementById("lista-paquetes");
    listaPaquetes.innerHTML = "";
    paquetes.forEach((paquete) => {
      const row = `
        <tr>
          <td>${paquete.destino}</td>
          <td>${paquete.duracion}</td>
          <td>${paquete.precio}</td>
          <td>${paquete.descripcion}</td>
          <td><button type="button" class="btn btn-primary" onClick="eliminarPaquete(${paquete.id})">Eliminar</button></td>  
        </tr>
      `;
      listaPaquetes.innerHTML += row;
    });
  } catch (error) {
    console.log("Error al cargar los paquetes: ", error);
  }
};

// Referencia a la lista del HTML
const listaPaquetes = document.getElementById("lista-paquetes");

// Función para buscar paquetes por DESCRIPCION
function buscarPaquetes() {
  const query = document.getElementById("buscar-input").value;
  let url = apiUrl;
  if (query) {
    url += `/consulta?q=${query}`;
  }
  fetch(url)
    .then((respuesta) => {
      return respuesta.json();
    })
    .then((paquetes) => {
      // Actualiza la grilla con los resultados
      const listaPaquetes = document.getElementById("lista-paquetes");
      listaPaquetes.innerHTML = ""; // Limpiar la lista

      paquetes.forEach((paquete) => {
        const row = document.createElement("tr");
        row.innerHTML = `
              <td>${paquete.destino}</td>
              <td>${paquete.duracion}</td>
              <td>${paquete.precio}</td>
              <td>${paquete.descripcion}</td>
              <td><button type="button" class="btn btn-primary" onClick="eliminarPaquete(${paquete.id})">Eliminar</button></td>
        `;
        listaPaquetes.appendChild(row);
      });
    });
}

// Función para AGREGAR un nuevo paquete
const agregarPaquete = async (paquete) => {
  const destino = document.getElementById("destino").value;
  const duracion = document.getElementById("duracion").value;
  const precio = document.getElementById("precio").value;
  const descripcion = document.getElementById("descripcion").value;

  if (!destino || !duracion || !precio || !descripcion) {
    alert("Por favor, ingresa todos los datos para realizar la carga");
    return;
  }

  try {
    const response = await fetch(apiUrl, {
      method: "POST",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify(paquete),
    });
    const data = await response.json();
    cargarPaquetes();
  } catch (error) {
    console.log("Error al agregar el paquete: ", error);
  }
};

// Referencia al boton AGREGAR PAQUETE del HTML
const botonAgregarPaquete = document.getElementById("botonAgregarPaquete");

// Evento CLICK para AGREGAR paquetes
botonAgregarPaquete.addEventListener("click", function () {
  const destino = document.getElementById("destino").value;
  const duracion = document.getElementById("duracion").value;
  const precio = document.getElementById("precio").value;
  const descripcion = document.getElementById("descripcion").value;

  //Crear OBJETO PAQUETE
  const paquete = {
    destino: destino,
    duracion: duracion,
    precio: precio,
    descripcion: descripcion,
  };

  //Agregar paquete a la lista
  agregarPaquete(paquete);

  // LIMPIAR los campos de entrada
  document.getElementById("destino").value = "";
  document.getElementById("duracion").value = "";
  document.getElementById("precio").value = "";
  document.getElementById("descripcion").value = "";
});

// Función para ELIMINAR un paquete
const eliminarPaquete = async (id) => {
  try {
    await fetch(`${apiUrl}/${id}`, {
      method: "DELETE",
    });
    cargarPaquetes();
  } catch (error) {
    console.log("Error al eliminar el paquete: ", error);
  }
};

// Cargar la lista de paquetes al cargar o refrescar la página
cargarPaquetes();
