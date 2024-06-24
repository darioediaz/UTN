import { useEffect, useState } from "react";
import { consultarIngresos } from "../services/ingresos-service";
import { useNavigate } from "react-router-dom";

function Consulta() {
    const navigate = useNavigate();
    const [rows, setRows] = useState([]);

    useEffect(() => {
        const fetchData = async () => {
            try {
                const ingresos = await consultarIngresos();
                console.table(ingresos)
                setRows(ingresos);
            } catch (error) {
                console.error('Error al consultar ingresos:', error);
            }
        };
        fetchData();
    }, []);

    return(
        <div className="container-fluid">
            <h2>Listado de Ingresos</h2>
            <table className="table">
                <thead>
                    <tr>
                        <th style={{border:"1px solid lightgray"}}>id</th>
                        <th style={{border:"1px solid lightgray"}}>DNI</th>
                        <th style={{border:"1px solid lightgray"}}>Hora de Ingreso</th>
                        <th style={{border:"1px solid lightgray"}}>Proveedor</th>
                        <th style={{border:"1px solid lightgray"}}>Ingresa con notebook?</th>
                    </tr>
                </thead>
                <tbody>
                    {rows.map(row => 
                        <tr>
                            <td>{row.Id}</td>
                            <td>{row.Dni}</td>
                            <td>{row.HoraIngreso}</td>
                            <td>{row.Proveedor}</td>
                            <td>{row.ConNotebook === true ? "Si" : "No"}</td>
                        </tr>
                    )}
                </tbody>
            </table>
            <button className="btn btn-secondary m-2" onClick={()=>navigate("/registro")}>Volver</button>
        </div>
    );
}

export default Consulta;
