import axios from 'axios';

const URL = 'http://localhost:3001/ingresos';

export const registrarIngreso = async(data)=>{
    await axios.post(URL, data);
}

export const consultarIngresos = async(data)=>{
    const res = await axios.get(URL);
    return (res).data;
}
