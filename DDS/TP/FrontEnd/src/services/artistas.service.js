import httpService from "./http.service";

// mas adelante podemos usar un archivo de configuracion para el urlResource
import { config } from "../config";
const urlResource = config.urlResourceArtistas;

async function Buscar(Nombre, Pagina) {
  const resp = await httpService.get(urlResource, {
    params: { Nombre, Pagina },
  });
  return resp.data;
}

async function BuscarPorId(item) {
  const resp = await httpService.get(urlResource + "/" + item.IdArtista);
  return resp.data;
}

async function EliminarArtista(item) {
  await httpService.delete(urlResource + "/" + item.IdArtista);
}

async function Grabar(item) {
  try {
    if (item.IdArtista === 0 || !item.IdArtista) {
      // Si el ID del Artista es 0 o no está definido, es un nuevo Artista
      await httpService.post(urlResource, item);
    } else {
      // Si el ID del Artista está definido, es una actualización
      // Eliminamos el campo IdArtista para que el backend lo genere automáticamente
      const { IdArtista, ...data } = item;
      await httpService.put(`${urlResource}/${item.IdArtista}`, data);
    }
    console.log("Artista grabada correctamente.");
  } catch (error) {
    console.error("Error al grabar Artista:", error);
    throw error;
  }
}

export const artistasService = {
  Buscar,
  BuscarPorId,
  EliminarArtista,
  Grabar,
};
