const express = require('express');
const { Op, ValidationError } = require("sequelize");
const router = express.Router();
const db = require("../base-orm/sequelize-init");

// Obtener todos los juegos
router.get('/api/juegos', async (req, res) => {
  try {
    let where = {};
    if (req.query.Titulo != undefined && req.query.Titulo !== "") {
      where.Titulo = {
        [Op.like]: "%" + req.query.Titulo + "%",
      };
    }    
    const Pagina = req.query.Pagina ?? 1;
    const TamañoPagina = 10;    
    const { count, rows } = await db.juegos.findAndCountAll({
        attributes: [
          "IdJuego",
          "Titulo",
          "Puntuacion",
          "FechaLanzamiento",
        ],
        order: [["Titulo", "ASC"]],
        where,
        offset: (Pagina - 1) * TamañoPagina,
        limit: TamañoPagina,
      });
    
      return res.json({ Items: rows, RegistrosTotal: count });  } catch (error) {
    res.status(500).json({ error: 'Error al obtener los juegos' });
  }
});

// Obtener un juego por su Id
router.get('/api/juegos/:id', async (req, res) => {
  try {
    const juego = await db.juegos.findByPk(req.params.id);
    if (juego) {
      res.json(juego);
    } else {
      res.status(404).json({ error: 'Juego no encontrado' });
    }
  } catch (error) {
    res.status(500).json({ error: 'Error al obtener el juego' });
  }
});

// Crear un nuevo juego
router.post('/api/juegos', async (req, res) => {
  const { IdJuego, ...datosJuego} = req.body;
  try {
    const nuevoJuego = await db.juegos.create(datosJuego);
    res.status(200).json(nuevoJuego);
  } catch (error) {
    res.status(400).json({ error: error.message });
  }
});

// Actualizar un juego existente
router.put('/api/juegos/:id', async (req, res) => {
  try {
    const [numFilasActualizadas, juegoActualizado] = await db.juegos.update(req.body, {
      where: { IdJuego: req.params.id },
      returning: true,
    });
    if (juegoActualizado === 1) {
      res.sendStatus(204);
    } else {
      res.status(404).json({ error: 'Juego no encontrado' });
    }
  } catch (error) {
    res.status(400).json({ error: error.message });
  }
});

// Eliminar un juego existente
router.delete('/api/juegos/:id', async (req, res) => {
  try {
    const numFilasEliminadas = await db.juegos.destroy({
      where: { IdJuego: req.params.id },
    });
    if (numFilasEliminadas === 1) {
      res.json({ message: 'Juego eliminado correctamente' });
    } else {
      res.status(404).json({ error: 'Juego no encontrado' });
    }
  } catch (error) {
    res.status(500).json({ error: 'Error al eliminar el juego' });
  }
});

module.exports = router;