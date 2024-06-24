import React from 'react';

const ListadoSocio = ({ lista }) => {
  
  return (
    <div className="container mt-3">
      <table className="table table-striped">
        <thead>
          <tr>
            <th>ID Socio</th>
            <th>Apellido y Nombre</th>
            <th>Numero de Socio</th>
          </tr>
        </thead>
        <tbody>
          {lista.map((item) => (
             <tr key={item.IdSocio}>
              <td>{item.IdSocio}</td>
              <td>{item.ApeNomSocio}</td>
              <td>{item.NroSocio}</td>
            </tr>
          ))}
        </tbody>
      </table>
    </div>
  );
};

export default ListadoSocio;
