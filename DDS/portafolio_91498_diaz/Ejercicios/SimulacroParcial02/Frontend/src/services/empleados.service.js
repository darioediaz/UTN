import axios from 'axios';

const API_URL = './api/empleados';

const Buscar = async (ApellidoYNombre) => {
  try {
    const response = await axios.get(API_URL, { params: { ApellidoYNombre } });
    return response.data;
  } catch (error) {
    throw new Error(error.response?.data?.message || error.message);
  }
};

const BuscarPorId = async (IdEmpleado) => {
  try {
    const response = await axios.get(`${API_URL}/${IdEmpleado}`);
    return response.data;
  } catch (error) {
    throw new Error(error.response?.data?.message || error.message);
  }
};

const Grabar = async (data) => {
  try {
    if (data.IdEmpleado === 0) {
      const response = await axios.post(API_URL, data);
      return response.data;
    } else {
      const response = await axios.put(`${API_URL}/${data.IdEmpleado}`, data);
      return response.data;
    }
  } catch (error) {
    throw new Error(error.response?.data?.message || error.message);
  }
};

const Eliminar = async (IdEmpleado) => {
  try {
    const response = await axios.delete(`${API_URL}/${IdEmpleado}`);
    return response.data;
  } catch (error) {
    throw new Error(error.response?.data?.message || error.message);
  }
};

export const empleadosService = {
  Buscar,
  BuscarPorId,
  Grabar,
  Eliminar,
};
