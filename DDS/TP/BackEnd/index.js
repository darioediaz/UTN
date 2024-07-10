const express = require("express");

// crear servidor
const app = express();

require("./base-orm/sqlite-init");  // crear base si no existe

app.use(express.json()); // para poder leer json en el body

const cors = require("cors");
app.use(
  cors({
    origin: "*", // origin: 'https://dds-frontend.azurewebsites.net'
  })
);

// controlar ruta
app.get("/", (req, res) => {
  res.send("dds-backend iniciado!");
});


const juegosRouter = require("./routes/juegos");
app.use(juegosRouter);

const cancionesRouter = require("./routes/canciones");
app.use(cancionesRouter);

const peliculasRouter = require("./routes/peliculas");
app.use(peliculasRouter);

const librosRouter = require("./routes/libros");
app.use(librosRouter);

const seriesRouter = require("./routes/series");
app.use(seriesRouter);

const artistasRouter = require("./routes/artistas");
app.use(artistasRouter);

const deportesRouter = require("./routes/deportes");
app.use(deportesRouter);

const redesSocialesRouter = require("./routes/redesSociales");
app.use(redesSocialesRouter);

// levantar servidor
if (!module.parent) {   // si no es llamado por otro módulo, es decir, si es el módulo principal -> levantamos el servidor
    const port = process.env.PORT || 4000;   // en producción se usa el puerto de la variable de entorno PORT
    app.locals.fechaInicio = new Date();
    app.listen(port, () => {
      console.log(`sitio escuchando en el puerto ${port}`);
    });
  }
  module.exports = app; // para testing