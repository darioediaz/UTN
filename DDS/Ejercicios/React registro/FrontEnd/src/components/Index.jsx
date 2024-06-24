import React from 'react'
import { Link } from 'react-router-dom';
import './styles.css'

export default function Index() {
    return (
        <div className="container_app">
            <h4>Desarrollo de Software</h4>
            <h6>Parcial 18/06/2024</h6>
            <nav className='btn mt-3 pb-1'>
                <div>
                    <Link className='btn btn-primary' to='/registro'>Registrar Ingreso</Link>
                </div>
                <br></br>
                <div>
                    <Link className='btn btn-primary' to='/consulta'>Consultar Ingresos</Link>
                </div>
            </nav>
        </div>
    );
}

