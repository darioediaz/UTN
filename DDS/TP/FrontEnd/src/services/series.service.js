
import httpService from "./http.service";
//const urlResource = "https://labsys.frc.utn.edu.ar/dds-express/api/articulos";

// mas adelante podemos usar un archivo de configuracion para el urlResource
 import {config} from "../config";
 const urlResource = config.urlResourceseries;

async function Buscar(Titulo, Pagina) {
  const resp = await httpService.get(urlResource, {
    params: { Titulo, Pagina },
  });
  return resp.data;
}

async function BuscarPorId(item) {
  const resp = await httpService.get(urlResource + "/" + item.IdSerie);
  return resp.data;
}

async function EliminarSerie(item) {
  await httpService.delete(urlResource + "/" + item.IdSerie);
}

async function Grabar(item) {
  try {
    if (item.IdSerie === 0 || !item.IdSerie) {
      // Si el ID del Serie es 0 o no está definido, es un nuevo Serie
      await httpService.post(urlResource, item);
    } else {
      // Si el ID del Serie está definido, es una actualización
      // Eliminamos el campo IdSerie para que el backend lo genere automáticamente
      const { IdSerie, ...data } = item;
      await httpService.put(`${urlResource}/${item.IdSerie}`, data);
    }
    console.log("Serie grabado correctamente.");
  } catch (error) {
    console.error("Error al grabar serie:", error);
    throw error;
  }
}

export const seriesService = {
  Buscar,BuscarPorId,EliminarSerie,Grabar
};
