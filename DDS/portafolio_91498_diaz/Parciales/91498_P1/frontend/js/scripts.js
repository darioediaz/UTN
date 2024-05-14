const apiURL = "http://localhost:3000/eventos";

// Funcion para obtener eventos
const cargarEventos = async () => {
  try {
    const response = await fetch(apiURL);
    const eventos = await response.json();
    const grillaEventos = document.getElementById("grilla-eventos");
    grillaEventos.innerHTML = ""; // limpia la grilla
    eventos.forEach((evento) => {
      const row = `
        <tr>
          <td>${evento.nombre}</td>
          <td>${evento.descripcion}</td>
          <td>${evento.ubicacion}</td>
          <td>${evento.fechaInicio}</td>
          <td>${evento.fechaFin}</td>
          <td>${evento.tipoAsistencia}</td>
          <td><a href="${evento.enlace}" class="enlace">${evento.enlace}</a></td>
        </tr>
      `;
      grillaEventos.innerHTML += row;
    });
    // Agregar evento de clic a los enlaces
    const enlaces = document.getElementsByClassName("enlace");
    for (let i = 0; i < enlaces.length; i++) {
      enlaces[i].addEventListener("click", (event) => {
        event.preventDefault(); // Evitar comportamiento predeterminado del enlace
        const enlace = event.target.href;
        window.location.href = enlace; // Redireccionar al enlace
      });
    }
  } catch (error) {
    console.log("Error al cargar los eventos: ", error);
  }
};

cargarEventos();
