import React from "react";
import { useForm } from "react-hook-form";

export default function DeportesRegistro({
  AccionABMC,
  Item,
  Grabar,
  Volver,
}) {
  const {
    register,
    handleSubmit,
    formState: { errors, touchedFields, isValid, isSubmitted },
  } = useForm({ values: Item });

  const onSubmit = (data) => {
    Grabar(data);
  };

  return (
    <form onSubmit={handleSubmit(onSubmit)}>
      <div className="container-fluid">

        <fieldset disabled={AccionABMC === "C"}>

          {/* campo Nombre */}
          <div className="row">
            <div className="col-sm-4 col-md-3 offset-md-1">
              <label className="col-form-label" htmlFor="Nombre">
                Nombre<span className="text-danger">*</span>:
              </label>
            </div>
            <div className="col-sm-8 col-md-6">
              <input
                type="text"
                {...register("Nombre", {
                  required: { value: true, message: "Nombre es requerido" },
                  minLength: {
                    value: 4,
                    message: "Nombre debe tener al menos 4 caracteres",
                  },
                  maxLength: {
                    value: 55,
                    message: "Nombre debe tener como máximo 55 caracteres",
                  },
                })}
                autoFocus
                className={
                  "form-control " + (errors?.Nombre ? "is-invalid" : "")
                }
              />
              {errors?.Nombre && touchedFields.Nombre && (
                <div className="invalid-feedback">
                  {errors?.Nombre?.message}
                </div>
              )}
            </div>
          </div>

          {/* campo CantidadJugadores */}
          <div className="row">
            <div className="col-sm-4 col-md-3 offset-md-1">
              <label className="col-form-label" htmlFor="CantidadJugadores">
                Cantidad de Jugadores<span className="text-danger">*</span>:
              </label>
            </div>
            <div className="col-sm-8 col-md-6">
              <input
                type="number"
                {...register("CantidadJugadores", {
                  required: { value: true, message: "CantidadJugadores es requerido" },
                  min: {
                    value: 0,
                    message: "CantidadJugadores debe ser mayor a 0",
                  },
                  max: {
                    value: 99999999,
                    message: "CantidadJugadores debe ser menor o igual a 99999999",
                  },
                })}
                className={
                  "form-control " + (errors?.CantidadJugadores ? "is-invalid" : "")
                }
              />
              <div className="invalid-feedback">{errors?.CantidadJugadores?.message}</div>
            </div>
          </div>


         {/* campo PaisOrigen */}
          <div className="row">
            <div className="col-sm-4 col-md-3 offset-md-1">
              <label className="col-form-label" htmlFor="PaisOrigen">
              Pais de Origen<span className="text-danger">*</span>:
              </label>
            </div>
            <div className="col-sm-8 col-md-6">
              <input
                type="text"
                {...register("PaisOrigen", {
                    required: { value: true, message: "Pais de Origen es requerido" },
                    minLength: {
                      value: 4,
                      message: "Pais de Origen debe tener al menos 4 caracteres",
                    },
                    maxLength: {
                      value: 55,
                      message: "Pais de Origen debe tener como máximo 55 caracteres",
                  },
                })}
                className={
                  "form-control " + (errors?.PaisOrigen ? "is-invalid" : "")
                }
              />
              <div className="invalid-feedback">{errors?.PaisOrigen?.message}</div>
            </div>
          </div>


          {/* campo FechaFundacion */}
          <div className="row">
            <div className="col-sm-4 col-md-3 offset-md-1">
              <label className="col-form-label" htmlFor="FechaFundacion">
                Fecha de Fundacion<span className="text-danger">*</span>:
              </label>
            </div>
            <div className="col-sm-8 col-md-6">
              <input
                type="date"
                {...register("FechaFundacion", {
                  required: { value: true, message: "Fecha de Fundacion es requerido" }
                })}
                className={
                  "form-control " + (errors?.FechaFundacion ? "is-invalid" : "")
                }
              />
              <div className="invalid-feedback">
                {errors?.FechaFundacion?.message}
              </div>
            </div>
          </div>

        </fieldset>

        {/* Botones Grabar, Cancelar/Volver' */}
        <hr />
        <div className="row justify-content-center">
          <div className="col text-center botones">
            {AccionABMC !== "C" && (
              <button type="submit" className="btn btn-primary">
                <i className="fa fa-check"></i> Grabar
              </button>
            )}
            <button
              type="button"
              className="btn btn-warning"
              onClick={() => Volver()}
            >
              <i className="fa fa-undo"></i>
              {AccionABMC === "C" ? " Volver" : " Cancelar"}
            </button>
          </div>
        </div>

        {/* texto: Revisar los datos ingresados... */}
        {!isValid && isSubmitted && (
          <div className="row alert alert-danger mensajesAlert">
            <i className="fa fa-exclamation-sign"></i>
            Revisar los datos ingresados...
          </div>
        )}

      </div>
    </form>
  );
}

