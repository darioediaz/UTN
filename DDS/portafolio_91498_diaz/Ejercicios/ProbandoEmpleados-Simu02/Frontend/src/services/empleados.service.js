
import httpService from "./http.service";
//const urlResource = "https://labsys.frc.utn.edu.ar/dds-express/api/articulos";

// mas adelante podemos usar un archivo de configuracion para el urlResource
 import {config} from "../config";
 const urlResource = config.urlResourceEmpleados;


async function Buscar(ApellidoYNombre, Suspendido, Pagina) {
  const resp = await httpService.get(urlResource, {
    params: { ApellidoYNombre, Suspendido, Pagina },
  });
  return resp.data;
}


async function BuscarPorId(item) {
  const resp = await httpService.get(urlResource + "/" + item.IdEmpleado);
  return resp.data;
}

// revisar, porque borra al empleado y no lo suspende
async function ActivarDesactivar(item) {
  await httpService.delete(urlResource + "/" + item.IdEmpleado);
}


async function Grabar(item) {
  if (item.IdEmpleado === 0) {
    await httpService.post(urlResource, item);
  } else {
    await httpService.put(urlResource + "/" + item.IdEmpleado, item);
  }
}


export const empleadosService = {
  Buscar,BuscarPorId,ActivarDesactivar,Grabar
};
