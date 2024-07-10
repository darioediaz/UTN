import httpService from "./http.service";
//const urlResource = "https://labsys.frc.utn.edu.ar/dds-express/api/articulos";

 import {config} from "../config";
 const urlResource = config.urlResourceRedesSociales;

async function Buscar(Nombre, Pagina) {
  const resp = await httpService.get(urlResource, {
    params: { Nombre, Pagina },
  });
  return resp.data;
}

async function BuscarPorId(item) {
  const resp = await httpService.get(urlResource + "/" + item.IdRedSocial);
  return resp.data;
}

async function EliminarRedSocial(item) {
  await httpService.delete(urlResource + "/" + item.IdRedSocial);
}

async function Grabar(item) {
  try {
    if (item.IdRedSocial === 0 || !item.IdRedSocial) {

      // Si el ID del RedesSociales es 0 o no está definido, es un nuevo RedesSociales
      await httpService.post(urlResource, item);
    } else {
      // Si el ID del RedesSociales está definido, es una actualización
      // Eliminamos el campo IdRedesSociales para que el backend lo genere automáticamente
      const { IdRedesSociales, ...data } = item;
      await httpService.put(`${urlResource}/${item.IdRedSocial}`, data);
    }
    console.log("RedesSociales grabado correctamente.");
  } catch (error) {
    console.log(item)
    console.error("Error al grabar RedesSociales:", error);
    throw error;
  }
}

export const redesSocialesService = {
  Buscar,BuscarPorId,EliminarRedSocial,Grabar
};