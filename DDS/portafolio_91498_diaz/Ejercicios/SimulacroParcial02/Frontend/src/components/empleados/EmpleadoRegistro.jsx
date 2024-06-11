import React, { useState } from 'react';
import axios from 'axios';

const EmpleadoRegistro = ({ onClose }) => {
  const [nuevoEmpleado, setNuevoEmpleado] = useState({
    nombre: '',
    apellido: '',
    correo: ''
    // Agrega aquí más campos según la definición de la base de datos
  });

  const handleChange = (e) => {
    const { name, value } = e.target;
    setNuevoEmpleado((prevState) => ({
      ...prevState,
      [name]: value
    }));
  };

  const handleSubmit = async (e) => {
    e.preventDefault();
    try {
      await axios.post('/api/empleados', nuevoEmpleado);
      // Cerrar el componente después de agregar el nuevo empleado
      onClose();
    } catch (error) {
      console.error('Error al agregar empleado:', error);
    }
  };

  return (
    <div>
      <h2>Ingresar Nuevo Empleado</h2>
      <form onSubmit={handleSubmit}>
        <div>
          <label htmlFor="nombre">Nombre:</label>
          <input
            type="text"
            id="nombre"
            name="nombre"
            value={nuevoEmpleado.nombre}
            onChange={handleChange}
            required
          />
        </div>
        <div>
          <label htmlFor="apellido">Apellido:</label>
          <input
            type="text"
            id="apellido"
            name="apellido"
            value={nuevoEmpleado.apellido}
            onChange={handleChange}
            required
          />
        </div>
        <div>
          <label htmlFor="correo">Correo:</label>
          <input
            type="email"
            id="correo"
            name="correo"
            value={nuevoEmpleado.correo}
            onChange={handleChange}
            required
          />
        </div>
        {/* Agrega más campos según la definición de la base de datos */}
        <button type="submit">Guardar</button>
      </form>
    </div>
  );
};

export default EmpleadoRegistro;
