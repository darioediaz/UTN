const express = require('express');
const { Op, ValidationError } = require("sequelize");
const router = express.Router();
const db = require("../base-orm/sequelize-init");

// Obtener todos los artistas
router.get('/api/artistas', async (req, res) => {
    try {
        let where = {};
        if (req.query.Nombre != undefined && req.query.Nombre !== "") {
            where.Nombre = {
                [Op.like]: "%" + req.query.Nombre + "%",
            };
        }
        const Pagina = req.query.Pagina ?? 1;
        const TamañoPagina = 10;
        const { count, rows } = await db.artistas.findAndCountAll({
            attributes: [
                "IdArtista",
                "Nombre",
                "FechaNacimiento",
                "Nacionalidad",
                "Descripcion",
            ],
            order: [["Nombre", "ASC"]],
            where,
            offset: (Pagina - 1) * TamañoPagina,
            limit: TamañoPagina,
        });

        return res.json({ Items: rows, RegistrosTotal: count });
    } catch (error) {
        res.status(500).json({ error: 'Error al obtener los artistas' });
    }
});

// Obtener un artista por su Id
router.get('/api/artistas/:id', async (req, res) => {
    try {
        const artista = await db.artistas.findByPk(req.params.id);
        if (artista) {
            res.json(artista);
        } else {
            res.status(404).json({ error: 'Artista no encontrado' });
        }
    } catch (error) {
        res.status(500).json({ error: 'Error al obtener el artista' });
    }
});

// Crear un nuevo artista
router.post('/api/artistas', async (req, res) => {
    const { IdArtista, ...datosArtista} = req.body;
    try {
        const nuevoArtista = await db.artistas.create(datosArtista);
        res.status(200).json(nuevoArtista);
    } catch (error) {
        res.status(400).json({ error: error.message });
    }
});

// Actualizar un artista existente
router.put('/api/artistas/:id', async (req, res) => {
    try {
        const [numFilasActualizadas, artistasActualizados] = await db.artistas.update(req.body, {
            where: { IdArtista: req.params.id },
            returning: true,
        });
        if (artistasActualizados === 1) {
            res.sendStatus(204);
        } else {
            res.status(404).json({ error: 'Artista no encontrado' });
        }
    } catch (error) {
        res.status(400).json({ error: error.message });
    }
});

// Eliminar un artista existente
router.delete('/api/artistas/:id', async (req, res) => {
    try {
        const numFilasEliminadas = await db.artistas.destroy({
            where: { IdArtista: req.params.id },
        });
        if (numFilasEliminadas === 1) {
            res.json({ message: 'Artista eliminado correctamente' });
        } else {
            res.status(404).json({ error: 'Artista no encontrado' });
        }
    } catch (error) {
        res.status(500).json({ error: 'Error al eliminar el artista' });
    }
});

module.exports = router;
