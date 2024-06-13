import React, { useState, useEffect } from "react";
import { useForm } from "react-hook-form";
import moment from "moment";
import EmpleadoListado from "./EmpleadoListado";
import EmpleadoRegistro from "./EmpleadoRegistro";
import { empleadosService } from "../../services/empleados.service";
import modalDialogService from "../../services/modalDialog.service";

function Empleados() {
  const TituloAccionABMC = {
    A: "(Agregar)",
    B: "(Eliminar)",
    M: "(Modificar)",
    C: "(Consultar)",
    L: "(Listado)",
  };
  const [AccionABMC, setAccionABMC] = useState("L");

  const { register, handleSubmit, setValue } = useForm();
  const [ApellidoYNombre, setApellidoYNombre] = useState("");

  const [Items, setItems] = useState(null);
  const [Item, setItem] = useState(null);

  useEffect(() => {
    Buscar();
  }, []);

  async function Buscar(data) {
    modalDialogService.BloquearPantalla(true);
    try {
      const empleados = await empleadosService.Buscar(data?.ApellidoYNombre || "", true, 1);
      setItems(empleados.Items);
    } catch (error) {
      modalDialogService.Alert("Error al buscar empleados");
    } finally {
      modalDialogService.BloquearPantalla(false);
    }
  }

  async function BuscarPorId(id, accionABMC) {
    try {
      const empleado = await empleadosService.BuscarPorId(id);
      setItem(empleado);
      setAccionABMC(accionABMC);
    } catch (error) {
      modalDialogService.Alert("Error al buscar el empleado");
    }
  }

  function Consultar(item) {
    BuscarPorId(item.IdEmpleado, "C");
  }

  function Modificar(item) {
    if (item.Suspendido) {
      modalDialogService.Alert("No puede modificarse un registro suspendido.");
      return;
    }
    BuscarPorId(item.IdEmpleado, "M");
  }

  function Agregar() {
    setAccionABMC("A");
    setItem({
      IdEmpleado: 0,
      ApellidoYNombre: '',
      Dni: '',
      FechaNacimiento: moment(new Date()).format("YYYY-MM-DD"),
      Suspendido: false,
    });
  }

  async function Eliminar(item) {
    modalDialogService.Confirm(
      "Está seguro que quiere eliminar el registro?",
      undefined,
      undefined,
      undefined,
      async () => {
        try {
          await empleadosService.ActivarDesactivar(item.IdEmpleado);
          await Buscar();
        } catch (error) {
          modalDialogService.Alert(error.message);
        }
      }
    );
  }

  async function Grabar(data) {
    try {
      await empleadosService.Grabar(data);
      modalDialogService.Alert(
        `Registro ${AccionABMC === "A" ? "agregado" : "modificado"} correctamente.`
      );
      await Buscar();
      Volver();
    } catch (error) {
      modalDialogService.Alert("Error al guardar el empleado");
    }
  }

  function Volver() {
    setAccionABMC("L");
  }

  return (
    <div>
      <div className="tituloPagina">
        Empleados <small>{TituloAccionABMC[AccionABMC]}</small>
      </div>

      {AccionABMC === "L" && (
        <form onSubmit={handleSubmit(Buscar)}>
          <div className="row">
            <div className="col-sm-3">
              <label>Apellido y Nombre:</label>
              <input
                type="text"
                {...register("ApellidoYNombre")}
                className="form-control"
                onChange={(e) => setApellidoYNombre(e.target.value)}
              />
            </div>
            <div className="col-sm-3">
              <button type="submit" className="btn btn-primary">
                Buscar
              </button>
              <button type="button" className="btn btn-success" onClick={Agregar}>
                Agregar
              </button>
            </div>
          </div>
        </form>
      )}

      {AccionABMC === "L" && Items?.length > 0 && (
        <EmpleadoListado
          {...{
            Items,
            Consultar,
            Modificar,
            Eliminar,
          }}
        />
      )}

      {AccionABMC === "L" && Items?.length === 0 && (
        <div className="alert alert-info mensajesAlert">
          <i className="fa fa-exclamation-sign"></i>
          No se encontraron registros...
        </div>
      )}

      {AccionABMC !== "L" && (
        <EmpleadoRegistro
          {...{ AccionABMC, Item, Grabar, Volver }}
        />
      )}
    </div>
  );
}

export { Empleados };
