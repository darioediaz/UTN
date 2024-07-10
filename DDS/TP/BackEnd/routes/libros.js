const express = require('express');
const { Op, ValidationError } = require("sequelize");
const router = express.Router();
const db = require("../base-orm/sequelize-init");

// Obtener todos los libros
router.get('/api/libros', async (req, res) => {
  try {
    let where = {};
    if (req.query.Titulo != undefined && req.query.Titulo !== "") {
      where.Titulo = {
        [Op.like]: "%" + req.query.Titulo + "%",
      };
    }    
    const Pagina = req.query.Pagina ?? 1;
    const TamañoPagina = 10;    
    const { count, rows } = await db.libros.findAndCountAll({
        attributes: [
          "IdLibro",
          "Titulo",
          "Precio",
          "FechaPublicacion",
        ],
        order: [["Titulo", "ASC"]],
        where,
        offset: (Pagina - 1) * TamañoPagina,
        limit: TamañoPagina,
      });
    
      return res.json({ Items: rows, RegistrosTotal: count });  } catch (error) {
    res.status(500).json({ error: 'Error al obtener los libros' });
  }
});

// Obtener un libro por su Id
router.get('/api/libros/:id', async (req, res) => {
  try {
    const libro = await db.libros.findByPk(req.params.id);
    if (libro) {
      res.json(libro);
    } else {
      res.status(404).json({ error: 'Libro no encontrado' });
    }
  } catch (error) {
    res.status(500).json({ error: 'Error al obtener el libro' });
  }
});

// Crear un nuevo libro
router.post('/api/libros', async (req, res) => {
  const { IdLibro, ...datosLibro} = req.body;
  try {
    const nuevoLibro = await db.libros.create(datosLibro);
    res.status(200).json(nuevoLibro);
  } catch (error) {
    res.status(400).json({ error: error.message });
  }
});

// Actualizar un libro existente
router.put('/api/libros/:id', async (req, res) => {
  try {
    const [numFilasActualizadas, libroActualizado] = await db.libros.update(req.body, {
      where: { IdLibro: req.params.id },
      returning: true,
    });
    if (libroActualizado === 1) {
      res.sendStatus(204);
    } else {
      res.status(404).json({ error: 'Libro no encontrado' });
    }
  } catch (error) {
    res.status(400).json({ error: error.message });
  }
});

// Eliminar un libro existente
router.delete('/api/libros/:id', async (req, res) => {
  try {
    const numFilasEliminadas = await db.libros.destroy({
      where: { IdLibro: req.params.id },
    });
    if (numFilasEliminadas === 1) {
      res.json({ message: 'Libro eliminado correctamente' });
    } else {
      res.status(404).json({ error: 'Libro no encontrado' });
    }
  } catch (error) {
    res.status(500).json({ error: 'Error al eliminar el libro' });
  }
});

module.exports = router;