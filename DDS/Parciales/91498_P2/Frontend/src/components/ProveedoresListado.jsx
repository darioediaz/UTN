import React from "react";
import moment from "moment";

export default function ProveedoresListado({
  Items,
  Pagina,
  RegistrosTotal,
  Paginas,
  Buscar,
}) {
  return (
    <div className="table-responsive">
      <table className="table table-hover table-sm table-bordered table-striped">
        <thead>
          <tr>
            <th className="text-start">Razon Social</th>
            <th className="text-center">Telefono</th>
            <th className="text-center">Fecha de Alta</th>
          </tr>
        </thead>

        <tbody>
          {Items &&
            Items.map((Item) => (
              <tr key={Item.IdProveedor}>
                <td className="text-start">{Item.RazonSocial}</td>
                <td className="text-center">{Item.Telefono}</td>
                <td className="text-center">{moment(Item.FechaAlta).format("DD/MM/YYYY")}</td>
              </tr>
            ))}
        </tbody>
      </table>

      {/* Paginador*/}
      <div className="paginador text-start">
        <div className="row">
          <div className="col">
            <span className="pyBadge">Registros: {RegistrosTotal}</span>
          </div>
          
          <div className="col text-start">
            Pagina: &nbsp;
            <select
              value={Pagina}
              onChange={(e) => {
                Buscar(e.target.value);
              }}
            >
              {Paginas?.map((x) => (
                <option value={x} key={x}>
                  {x}
                </option>
              ))}
            </select>
            &nbsp; de {Paginas?.length}
          </div>

        </div>
      </div>
    </div>
  );
}
