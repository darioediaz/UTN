import React from 'react';
import { useForm } from 'react-hook-form';
import axios from 'axios';
import { useNavigate, useParams } from 'react-router-dom';

const EmpleadoRegistro = () => {
  const { register, handleSubmit, setValue } = useForm();
  const navigate = useNavigate();
  const { id } = useParams();

  const onSubmit = async (data) => {
    try {
      if (id) {
        await axios.put(`/api/empleados/${id}`, data);
      } else {
        await axios.post('/api/empleados', data);
      }
      navigate('/empleados');
    } catch (error) {
      console.error('Error al guardar el empleado:', error);
    }
  };

  const fetchEmpleado = async (id) => {
    try {
      const response = await axios.get(`/api/empleados/${id}`);
      const empleado = response.data;
      setValue('ApellidoYNombre', empleado.ApellidoYNombre);
      setValue('Dni', empleado.Dni);
      setValue('FechaNacimiento', empleado.FechaNacimiento);
      setValue('Suspendido', empleado.Suspendido);
    } catch (error) {
      console.error('Error al obtener el empleado:', error);
    }
  };

  React.useEffect(() => {
    if (id) {
      fetchEmpleado(id);
    }
  }, [id]);

  return (
    <form onSubmit={handleSubmit(onSubmit)}>
      <div>
        <label>Nombre</label>
        <input {...register('ApellidoYNombre', { required: true })} />
      </div>
      <div>
        <label>DNI</label>
        <input type="number" {...register('Dni', { required: true })} />
      </div>
      <div>
        <label>Fecha de Nacimiento</label>
        <input type="date" {...register('FechaNacimiento', { required: true })} />
      </div>
      <div>
        <label>Suspendido</label>
        <input type="checkbox" {...register('Suspendido')} />
      </div>
      <button type="submit">Guardar</button>
    </form>
  );
};

export default EmpleadoRegistro;
