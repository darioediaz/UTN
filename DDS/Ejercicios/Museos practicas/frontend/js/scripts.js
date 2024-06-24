const apiURL = "http://localhost:3000/api/museos";

const cargarMuseos = async () => {
  try {
    const response = await fetch(apiURL);
    const museos = await response.json();
    const listaMuseos = document.getElementById("lista-museos");
    listaMuseos.innerHTML = "";
    museos.forEach((museo) => {
      const row = `
        <tr>
          <td>${museo.nombre}</td>
          <td>${museo.ubicacion}</td>
          <td>${museo.exposiciones}</td>
          <td>${museo.horarios}</td>
          <td>${museo.precioEntrada}</td>
          <td><button type="button" class="btn btn-primary" onClick="eliminarMuseo(${museo.id})">Eliminar</td>
        </tr>
      `;
      listaMuseos.innerHTML += row;
    });
  } catch (error) {
    console.log("Error al cargar los museos: ", error);
  }
};

// Referencia al HTML
const listaMuseos = document.getElementById("lista-museos");

// Funcion para eliminar museo
const eliminarMuseo = async (id) => {
  try {
    await fetch(`${apiURL}/${id}`, {
      method: "DELETE",
    });
    cargarMuseos();
  } catch (error) {
    console.log("Error al eliminar museo: ", error);
  }
};

// Funcion para agregar museo
const agregarMuseo = async () => {
  const nuevoMuseo = {
    nombre: document.getElementById("nombre").value,
    ubicacion: document.getElementById("ubicacion").value,
    exposiciones: document.getElementById("exposiciones").value,
    horarios: document.getElementById("horarios").value,
    precioEntrada: document.getElementById("precio").value,
  };

  try {
    await fetch(apiURL, {
      method: "POST",
      headers: {
        "Content-Type": "application/json",
      },
      body: JSON.stringify(nuevoMuseo),
    });
    // Museo creado correctamente, limpiar los campos y recargar la lista
    document.getElementById("nombre").value = "";
    document.getElementById("ubicacion").value = "";
    document.getElementById("exposiciones").value = "";
    document.getElementById("horarios").value = "";
    document.getElementById("precio").value = "";

    cargarMuseos();
  } catch (error) {
    console.log("Error al crear museo:", error);
  }
};

// Funcion para buscar museos por nombre
const buscarMuseos = async () => {
  const query = document.getElementById("buscar-input").value;
  let url = apiURL;
  if (query) {
    url += `/consulta?q=${query}`;
  }

  try {
    const response = await fetch(url);
    const museos = await response.json();
    const listaMuseos = document.getElementById("lista-museos");
    listaMuseos.innerHTML = "";
    museos.forEach((museo) => {
      const row = document.createElement("tr");
      row.innerHTML = `
        <td>${museo.nombre}</td>
        <td>${museo.ubicacion}</td>
        <td>${museo.exposiciones}</td>
        <td>${museo.horarios}</td>
        <td>${museo.precioEntrada}</td>
        <td><button type="button" class="btn btn-primary" onClick="eliminarMuseo(${museo.id})">Eliminar</td>
      `;
      listaMuseos.appendChild(row);
    });
  } catch (error) {
    console.log("Error al buscar museo:", error);
  }
};

cargarMuseos();
