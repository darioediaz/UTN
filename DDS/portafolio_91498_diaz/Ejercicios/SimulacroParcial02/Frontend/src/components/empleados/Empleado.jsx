import React, { useState } from "react";
import axios from "axios";
import EmpleadoListado from "./components/empleados/EmpleadoListado";
import EmpleadoRegistro from "./components/empleados/EmpleadoRegistro";

const Empleado = () => {
  const [mostrarRegistro, setMostrarRegistro] = useState(false);
  const [empleados, setEmpleados] = useState([]);

  const obtenerEmpleados = async () => {
    try {
      const response = await axios.get("/api/empleados");
      setEmpleados(response.data);
    } catch (error) {
      console.error("Error al obtener empleados:", error);
    }
  };

  const handleMostrarRegistro = () => {
    setMostrarRegistro(true);
  };

  const handleCerrarRegistro = () => {
    setMostrarRegistro(false);
    // Actualizar la lista de empleados después de agregar uno nuevo
    obtenerEmpleados();
  };

  return (
    <div>
      <button onClick={handleMostrarRegistro}>Agregar Nuevo Empleado</button>
      {mostrarRegistro && <EmpleadoRegistro onClose={handleCerrarRegistro} />}
      <EmpleadoListado empleados={empleados} />
    </div>
  );
};

export { Empleado };
