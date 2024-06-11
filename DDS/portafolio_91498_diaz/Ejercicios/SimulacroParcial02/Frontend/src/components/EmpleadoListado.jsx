import React, { useState, useEffect } from 'react';
import axios from 'axios';
import { useForm } from 'react-hook-form';
import { useNavigate } from 'react-router-dom';
import Empleado from './Empleado';

const EmpleadoListado = () => {
  const [empleados, setEmpleados] = useState([]);
  const { register, handleSubmit } = useForm();
  const navigate = useNavigate();

  const onSubmit = async (data) => {
    try {
      const response = await axios.get(`/api/empleados?ApellidoYNombre=${data.ApellidoYNombre}`);
      setEmpleados(response.data);
    } catch (error) {
      console.error('Error al buscar empleados:', error);
    }
  };

  const handleDelete = async (id) => {
    try {
      await axios.delete(`/api/empleados/${id}`);
      setEmpleados(empleados.filter(empleado => empleado.id !== id));
    } catch (error) {
      console.error('Error al eliminar el empleado:', error);
    }
  };

  return (
    <div>
      <form onSubmit={handleSubmit(onSubmit)}>
        <input {...register('ApellidoYNombre')} placeholder="Buscar por nombre" />
        <button type="submit">Buscar</button>
      </form>
      <button onClick={() => navigate('/empleadoregistro')}>Nuevo Empleado</button>
      <table>
        <thead>
          <tr>
            <th>Nombre</th>
            <th>DNI</th>
            <th>Fecha Nacimiento</th>
            <th>Suspendido</th>
            <th>Acciones</th>
          </tr>
        </thead>
        <tbody>
          {empleados.map(empleado => (
            <tr key={empleado.id}>
              <td>{empleado.ApellidoYNombre}</td>
              <td>{empleado.Dni}</td>
              <td>{empleado.FechaNacimiento}</td>
              <td>{empleado.Suspendido ? 'Sí' : 'No'}</td>
              <td>
                <button onClick={() => navigate(`/empleadoregistro/${empleado.id}`)}>Editar</button>
                <button onClick={() => handleDelete(empleado.id)}>Eliminar</button>
              </td>
            </tr>
          ))}
        </tbody>
      </table>
    </div>
  );
};

export default EmpleadoListado;
