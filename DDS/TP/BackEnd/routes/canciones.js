const express = require('express');
const { Op, ValidationError } = require("sequelize");
const router = express.Router();
const db = require("../base-orm/sequelize-init");

// Obtener todos los canciones
router.get('/api/canciones', async (req, res) => {
  try {
    let where = {};
    if (req.query.Titulo != undefined && req.query.Titulo !== "") {
      where.Titulo = {
        [Op.like]: "%" + req.query.Titulo + "%",
      };
    }    
    const Pagina = req.query.Pagina ?? 1;
    const TamañoPagina = 10;    
    const { count, rows } = await db.canciones.findAndCountAll({
        attributes: [
          "IdCancion",
          "Titulo",
          "DuracionSegundos",
          "FechaLanzamiento",
        ],
        order: [["Titulo", "ASC"]],
        where,
        offset: (Pagina - 1) * TamañoPagina,
        limit: TamañoPagina,
      });
    
      return res.json({ Items: rows, RegistrosTotal: count });  } catch (error) {
    res.status(500).json({ error: 'Error al obtener las canciones' });
  }
});

// Obtener un cancion por su Id
router.get('/api/canciones/:id', async (req, res) => {
  try {
    const cancion = await db.canciones.findByPk(req.params.id);
    if (cancion) {
      res.json(cancion);
    } else {
      res.status(404).json({ error: 'Cancion no encontrada' });
    }
  } catch (error) {
    res.status(500).json({ error: 'Error al obtener la cancion' });
  }
});

// Crear un nuevo cancion
router.post('/api/canciones', async (req, res) => {
  const { IdCancion, ...datosCancion} = req.body;
  try {
    const nuevaCancion = await db.canciones.create(datosCancion);
    res.status(200).json(nuevaCancion);
  } catch (error) {
    res.status(400).json({ error: error.message });
  }
});

// Actualizar un cancion existente
router.put('/api/canciones/:id', async (req, res) => {
  try {
    const [numFilasActualizadas, cancionActualizado] = await db.canciones.update(req.body, {
      where: { IdCancion: req.params.id },
      returning: true,
    });
    if (cancionActualizado === 1) {
      res.sendStatus(204);
    } else {
      res.status(404).json({ error: 'Cancion no encontrada' });
    }
  } catch (error) {
    res.status(400).json({ error: error.message });
  }
});

// Eliminar un cancion existente
router.delete('/api/canciones/:id', async (req, res) => {
  try {
    const numFilasEliminadas = await db.canciones.destroy({
      where: { IdCancion: req.params.id },
    });
    if (numFilasEliminadas === 1) {
      res.json({ message: 'Cancion eliminada correctamente' });
    } else {
      res.status(404).json({ error: 'Cancion no encontrada' });
    }
  } catch (error) {
    res.status(500).json({ error: 'Error al eliminar la cancion' });
  }
});

module.exports = router;