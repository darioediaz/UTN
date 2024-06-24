const express = require('express');
const cors = require('cors');
const app = express();

// Leer archivo de configuración
require('dotenv').config();

// Crear base si no existe
require("./base-orm/sqlite-init"); 

// Para poder leer JSON en el body
app.use(express.json()); 

// Configuración de CORS
app.use(cors());

// Configuración de rutas
const routeArticulos = require('./routes/articulos');
const routeSocios = require('./routes/socios'); // Nueva ruta de socios

app.use('/', routeArticulos);
app.use('/', routeSocios); // Usar la nueva ruta

// Inicio del servidor
const port = 4000;
app.listen(port, () => {
  console.log(`Servidor iniciado en el puerto ${port}`);
});

module.exports = app;

