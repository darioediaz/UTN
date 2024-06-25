import React from "react";
export default function ProveedoresBuscar({
  Buscar,
  Agregar,
}) {
  return (
    <form>
      {/* Botones */}
      <div className="row">
        <div className="col text-center botones">

          <button
            type="button"
            className="btn btn-primary"
            onClick={() => Agregar()}
          >
            <i className="fa fa-plus"> </i> Agregar Proveedor</button>
        </div>
      </div>
    </form>
  );
}
