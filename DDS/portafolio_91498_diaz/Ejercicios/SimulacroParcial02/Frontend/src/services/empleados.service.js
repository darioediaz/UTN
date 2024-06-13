import httpService from "./http.service";
import { config } from "../config";

const urlResource = config.urlResourceEmpleados;

async function Buscar(ApellidoYNombre, Activo, Pagina) {
  const resp = await httpService.get(urlResource, {
    params: { ApellidoYNombre, Activo, Pagina },
  });
  return resp.data;
}

async function BuscarPorId(id) {
  const resp = await httpService.get(`${urlResource}/${id}`);
  return resp.data;
}

async function ActivarDesactivar(id) {
  await httpService.delete(`${urlResource}/${id}`);
}

async function Grabar(item) {
  if (item.IdEmpleado === 0) {
    await httpService.post(urlResource, item);
  } else {
    await httpService.put(`${urlResource}/${item.IdEmpleado}`, item);
  }
}

export const empleadosService = {
  Buscar,
  BuscarPorId,
  ActivarDesactivar,
  Grabar,
};
