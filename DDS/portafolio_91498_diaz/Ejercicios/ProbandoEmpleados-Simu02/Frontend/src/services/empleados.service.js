
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
  try {
    if (item.IdEmpleado === 0 || !item.IdEmpleado) {
      // Si el ID del empleado es 0 o no está definido, es un nuevo empleado
      await httpService.post(urlResource, item);
    } else {
      // Si el ID del empleado está definido, es una actualización
      // Eliminamos el campo IdEmpleado para que el backend lo genere automáticamente
      const { IdEmpleado, ...data } = item;
      await httpService.put(`${urlResource}/${item.IdEmpleado}`, data);
    }
    console.log("Empleado grabado correctamente.");
  } catch (error) {
    console.error("Error al grabar empleado:", error);
    throw error;
  }
}



export const empleadosService = {
  Buscar,BuscarPorId,ActivarDesactivar,Grabar
};
