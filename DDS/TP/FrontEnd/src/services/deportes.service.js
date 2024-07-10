import httpService from "./http.service";
//const urlResource = "https://labsys.frc.utn.edu.ar/dds-express/api/articulos";

 import {config} from "../config";
 const urlResource = config.urlResourceDeportes;

async function Buscar(Nombre, Pagina) {
  const resp = await httpService.get(urlResource, {
    params: { Nombre, Pagina },
  });
  return resp.data;
}

async function BuscarPorId(item) {
  const resp = await httpService.get(urlResource + "/" + item.IdDeporte);
  return resp.data;
}

async function EliminarDeporte(item) {
  await httpService.delete(urlResource + "/" + item.IdDeporte);
}

async function Grabar(item) {
  try {
    if (item.IdDeporte === 0 || !item.IdDeporte) {
      // Si el ID del Deporte es 0 o no está definido, es un nuevo Deporte
      await httpService.post(urlResource, item);
    } else {
      // Si el ID del Deporte está definido, es una actualización
      // Eliminamos el campo IdDeporte para que el backend lo genere automáticamente
      const { IdDeporte, ...data } = item;
      await httpService.put(`${urlResource}/${item.IdDeporte}`, data);
    }
    console.log("Deporte grabado correctamente.");
  } catch (error) {
    console.error("Error al grabar Deporte:", error);
    throw error;
  }
}

export const deportesService = {
  Buscar,BuscarPorId,EliminarDeporte,Grabar
};
