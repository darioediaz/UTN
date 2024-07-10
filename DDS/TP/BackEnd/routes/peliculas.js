const express = require('express');
const { Op, ValidationError } = require("sequelize");
const router = express.Router();
const db = require("../base-orm/sequelize-init");

// Obtener todos los peliculas
router.get('/api/peliculas', async (req, res) => {
  try {
    let where = {};
    if (req.query.Titulo != undefined && req.query.Titulo !== "") {
      where.Titulo = {
        [Op.like]: "%" + req.query.Titulo + "%",
      };
    }    
    const Pagina = req.query.Pagina ?? 1;
    const TamañoPagina = 10;    
    const { count, rows } = await db.peliculas.findAndCountAll({
        attributes: [
          "IdPelicula",
          "Titulo",
          "Precio",
          "FechaEstreno",
        ],
        order: [["Titulo", "ASC"]],
        where,
        offset: (Pagina - 1) * TamañoPagina,
        limit: TamañoPagina,
      });
    
      return res.json({ Items: rows, RegistrosTotal: count });  } catch (error) {
    res.status(500).json({ error: 'Error al obtener las peliculas' });
  }
});

// Obtener un pelicula por su Id
router.get('/api/peliculas/:id', async (req, res) => {
  try {
    const pelicula = await db.peliculas.findByPk(req.params.id);
    if (pelicula) {
      res.json(pelicula);
    } else {
      res.status(404).json({ error: 'Pelicula no encontrada' });
    }
  } catch (error) {
    res.status(500).json({ error: 'Error al obtener la pelicula' });
  }
});

// Crear un nuevo pelicula
router.post('/api/peliculas', async (req, res) => {
  const { IdPelicula, ...datosPelicula} = req.body;
  try {
    const nuevaPelicula = await db.peliculas.create(datosPelicula);
    res.status(200).json(nuevaPelicula);
  } catch (error) {
    res.status(400).json({ error: error.message });
  }
});

// Actualizar un pelicula existente
router.put('/api/peliculas/:id', async (req, res) => {
  try {
    const [numFilasActualizadas, peliculaActualizado] = await db.peliculas.update(req.body, {
      where: { IdPelicula: req.params.id },
      returning: true,
    });
    if (peliculaActualizado === 1) {
      res.sendStatus(204);
    } else {
      res.status(404).json({ error: 'Pelicula no encontrada' });
    }
  } catch (error) {
    res.status(400).json({ error: error.message });
  }
});

// Eliminar un pelicula existente
router.delete('/api/peliculas/:id', async (req, res) => {
  try {
    const numFilasEliminadas = await db.peliculas.destroy({
      where: { IdPelicula: req.params.id },
    });
    if (numFilasEliminadas === 1) {
      res.json({ message: 'Pelicula eliminada correctamente' });
    } else {
      res.status(404).json({ error: 'Pelicula no encontrada' });
    }
  } catch (error) {
    res.status(500).json({ error: 'Error al eliminar la pelicula' });
  }
});

module.exports = router;