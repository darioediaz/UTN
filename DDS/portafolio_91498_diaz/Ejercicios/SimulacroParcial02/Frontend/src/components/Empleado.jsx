import React from 'react';

const Empleado = ({ empleado }) => {
  return (
    <div className="empleado">
      <h3>{empleado.nombre}</h3>
      <p>Posición: {empleado.posicion}</p>
      <p>Salario: {empleado.salario}</p>
    </div>
  );
}

export default Empleado;
