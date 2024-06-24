import React, { useState } from "react";
import './styles.css';
import { useForm } from 'react-hook-form';
import { registrarIngreso } from "../services/ingresos-service";
import Consulta from "./Consulta";
import { useNavigate } from "react-router-dom";

function Registro() {
    const [action, setAction] = useState('R');
    const { register, handleSubmit, formState:{errors}}=useForm();
    const navigate = useNavigate();

    async function onSubmit(data) {
        await registrarIngreso(data); 
        setAction('C');       
    }

    return(
        <>
        {action === 'R' && (

        <div className="container">
            <div className="container_app">
                <form onSubmit={handleSubmit(onSubmit)}>
                    <h2>Seguridad. Registro de ingresos</h2>
                    <div className="row form-group p-2">
                        <label for="Dni">DNI Ingreso:</label>
                        <input type="number" id="Dni" className="form-control" placeholder="DNI del ingresante..." {...register(
                            "Dni",{
                                required:{value:true, message:'Dni del ingresante no definido.'}
                            }
                        )}/>
                        {errors.Dni ? <span className="bg-danger text-white my-2" style={{borderRadius:"5px"}}>{errors.Dni.message}</span> : <></>}
                    </div>
                    <div className="row p-2">
                        <label for="HoraIngreso">Hora Ingreso [hh:mm]</label>
                        <input type="time" id="HoraIngreso" className="form-control" {...register(
                            "HoraIngreso",{
                                required:{value:true, message:'Hora de ingreso no establecida.'}
                            }
                        )}/>
                        {errors.HoraIngreso ? <span className="bg-danger text-white my-2" style={{borderRadius:"5px"}}>{errors.HoraIngreso.message}</span> : <></>}
                    </div>
                    <div className="row p-2">
                        <label for="Proveedor">Proveedor (Empresa externa):</label>
                        <input type="text" id="Proveedor" className="form-control" placeholder="Proovedor ingresante..." {...register(
                            "Proveedor",{
                                required:{value:true, message:'Proovedor ingresante no definido.'}
                            }
                        )}/>
                        {errors.Proveedor ? <span className="bg-danger text-white my-2" style={{borderRadius:"5px"}}>{errors.Proveedor.message}</span> : <></>}
                    </div>
                    <div className="row p-2">
                        <div className="col">
                            <input type="checkbox" id="ConNotebook" className="form-check-input mx-1" {...register(
                                "ConNotebook"
                            )}/>
                            <label for="ConNotebook">Ingresa con notebook</label>
                        </div>
                    </div>
                    <div className="row justify-content-center p-2">
                        <div className="col text-center">
                            <button type="submit" className="btn btn-success" onClick={()=>navigate("/consulta")}>Registrar</button>
                        </div>
                        <div className="col text-center">
                          <button type="button" className="btn btn-secondary" onClick={()=>navigate("/")}>Volver</button>
                        </div>
                        <div className="col text-center">
                            <button type="reset" className="btn btn-danger">Limpiar</button>
                        </div>
                    </div>
                </form>
            </div>
        </div>

        )}

        {action === 'C' && (

            <Consulta />

        )}
        </>
    );
}

export default Registro;
