import React, { useState, useEffect } from "react";
import moment from "moment";
import EmpleadosBuscar from "./EmpleadosBuscar"; // Asumiendo que este es el nombre correcto del componente
import EmpleadosListado from "./EmpleadosListado"; // Asumiendo que este es el nombre correcto del componente
import EmpleadosRegistro from "./EmpleadosRegistro"; // Asumiendo que este es el nombre correcto del componente
import { empleadosService } from "../../services/empleados.service";
import modalDialogService from "../../services/modalDialog.service";

function Empleado() {
  const TituloAccionABMC = {
    A: "(Agregar)",
    B: "(Eliminar)",
    M: "(Modificar)",
    C: "(Consultar)",
    L: "(Listado)",
  };
  const [AccionABMC, setAccionABMC] = useState("L");
  const [ApellidoYNombre, setApellidoYNombre] = useState("");
  const [Suspendido, setSuspendido] = useState("");
  const [Items, setItems] = useState(null);
  const [Item, setItem] = useState(null);
  const [RegistrosTotal, setRegistrosTotal] = useState(0);
  const [Pagina, setPagina] = useState(1);
  const [Paginas, setPaginas] = useState([]);

  useEffect(() => {
    async function fetchData() {
      try {
        modalDialogService.BloquearPantalla(true);
        const data = await empleadosService.Buscar(ApellidoYNombre, Suspendido, Pagina);
        setItems(data.Items);
        setRegistrosTotal(data.RegistrosTotal);
        const arrPaginas = [];
        for (let i = 1; i <= Math.ceil(data.RegistrosTotal / 10); i++) {
          arrPaginas.push(i);
        }
        setPaginas(arrPaginas);
      } catch (error) {
        console.error("Error al cargar datos:", error);
      } finally {
        modalDialogService.BloquearPantalla(false);
      }
    }

    fetchData();
  }, [ApellidoYNombre, Suspendido, Pagina]);

  async function Buscar(_pagina) {
    if (_pagina && _pagina !== Pagina) {
      setPagina(_pagina);
    } else {
      _pagina = Pagina;
    }
    modalDialogService.BloquearPantalla(true);
    const data = await empleadosService.Buscar(ApellidoYNombre, Suspendido, _pagina);
    modalDialogService.BloquearPantalla(false);
    setItems(data.Items);
    setRegistrosTotal(data.RegistrosTotal);
    const arrPaginas = [];
    for (let i = 1; i <= Math.ceil(data.RegistrosTotal / 10); i++) {
      arrPaginas.push(i);
    }
    setPaginas(arrPaginas);
  }

  async function BuscarPorId(item, accionABMC) {
    const data = await empleadosService.BuscarPorId(item);
    setItem(data);
    setAccionABMC(accionABMC);
  }

  function Consultar(item) {
    BuscarPorId(item, "C");
  }

  function Modificar(item) {
    if (!item.Suspendido) {
      modalDialogService.Alert("No puede modificarse un empleado suspendido.");
      return;
    }
    BuscarPorId(item, "M");
  }

  async function Agregar() {
    setAccionABMC("A");
    setItem({
      IdArticulo: 0,
      ApellidoYNombre: "",
      Dni: "",
      FechaNacimiento: "",
      Suspendido: false,
    });
  }

  function Imprimir() {
    modalDialogService.Alert("En desarrollo...");
  }

  async function ActivarDesactivar(item) {
    modalDialogService.Confirm(
      `¿Está seguro que quiere ${item.Suspendido ? "suspender" : "reincorporar"} el registro?`,
      undefined,
      undefined,
      undefined,
      async () => {
        await empleadosService.ActivarDesactivar(item);
        await Buscar();
      }
    );
  }

  async function Grabar(item) {
    try {
      await empleadosService.Grabar(item);
    } catch (error) {
      modalDialogService.Alert(error?.response?.data?.message ?? error.toString());
      return;
    }
    await Buscar();
    Volver();
    modalDialogService.Alert(
      `Registro ${AccionABMC === "A" ? "agregado" : "modificado"} correctamente.`
    );
  }

  function Volver() {
    setAccionABMC("L");
  }

  return (
    <div>
      <div className="tituloPagina">
        Empleado <small>{TituloAccionABMC[AccionABMC]}</small>
      </div>

      {AccionABMC === "L" && (
        <EmpleadosBuscar
          ApellidoYNombre={ApellidoYNombre}
          setApellidoYNombre={setApellidoYNombre}
          Suspendido={Suspendido}
          setSuspendido={setSuspendido}
          Buscar={Buscar}
          Agregar={Agregar}
        />
      )}

      {AccionABMC === "L" && Items?.length > 0 && (
        <EmpleadosListado
          Items={Items}
          Consultar={Consultar}
          Modificar={Modificar}
          ActivarDesactivar={ActivarDesactivar}
          Imprimir={Imprimir}
          Pagina={Pagina}
          RegistrosTotal={RegistrosTotal}
          Paginas={Paginas}
          Buscar={Buscar}
        />
      )}

      {AccionABMC === "L" && Items?.length === 0 && (
        <div className="alert alert-info mensajesAlert">
          <i className="fa fa-exclamation-sign"></i>
          No se encontraron registros...
        </div>
      )}

      {AccionABMC !== "L" && (
        <EmpleadosRegistro
          AccionABMC={AccionABMC}
          Item={Item}
          Grabar={Grabar}
          Volver={Volver}
        />
      )}
    </div>
  );
}

export { Empleado };
