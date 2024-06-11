import React from 'react';
import EmpleadoRegistro from './EmpleadoRegistro';

const EmpleadoListado = ({ empleados, onEliminarEmpleado }) => {
  return (
    <table>
      <thead>
        <tr>
          <th>Nombre</th>
          <th>Apellido</th>
          <th>Correo</th>
          <th>Acciones</th>
        </tr>
      </thead>
      <tbody>
        {empleados.map((empleado) => (
          <tr key={empleado.id}>
            <td>{empleado.nombre}</td>
            <td>{empleado.apellido}</td>
            <td>{empleado.correo}</td>
            <td>
              <button onClick={() => onEliminarEmpleado(empleado)}>Eliminar</button>
            </td>
          </tr>
        ))}
      </tbody>
    </table>
  );
};

export default EmpleadoListado;
