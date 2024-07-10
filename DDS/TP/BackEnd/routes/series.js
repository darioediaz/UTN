const express = require('express');
const { Op, ValidationError } = require("sequelize");
const router = express.Router();
const db = require("../base-orm/sequelize-init");

// Obtener todas las series
router.get('/api/series', async (req, res) => {
    try {
        let where = {};
        if (req.query.Titulo != undefined && req.query.Titulo !== "") {
            where.Titulo = {
                [Op.like]: "%" + req.query.Titulo + "%",
            };
        }
        const Pagina = req.query.Pagina ?? 1;
        const TamañoPagina = 10;
        const { count, rows } = await db.series.findAndCountAll({
            attributes: [
                "IdSerie",
                "Titulo",
                "NumTemporadas",
                "FechaEstreno",
            ],
            order: [["Titulo", "ASC"]],
            where,
            offset: (Pagina - 1) * TamañoPagina,
            limit: TamañoPagina,
        });

        return res.json({ Items: rows, RegistrosTotal: count });
    } catch (error) {
        res.status(500).json({ error: 'Error al obtener las series' });
    }
});

// Obtener una serie por su Id
router.get('/api/series/:id', async (req, res) => {
    try {
        const serie = await db.series.findByPk(req.params.id);
        if (serie) {
            res.json(serie);
        } else {
            res.status(404).json({ error: 'Serie no encontrada' });
        }
    } catch (error) {
        res.status(500).json({ error: 'Error al obtener la serie' });
    }
});

// Crear una nueva serie
router.post('/api/series', async (req, res) => {
    const { IdSerie, ...datosSeries } = req.body;
    try {
        const nuevaSerie = await db.series.create(datosSeries);
        res.status(200).json(nuevaSerie);
    } catch (error) {
        res.status(400).json({ error: error.message });
    }
});

// Actualizar una serie existente
router.put('/api/series/:id', async (req, res) => {
    try {
        const [numFilasActualizadas, serieActualizada] = await db.series.update(req.body, {
            where: { IdSerie: req.params.id },
            returning: true,
        });
        if (serieActualizada === 1) {
            res.sendStatus(204);
        } else {
            res.status(404).json({ error: 'Serie no encontrada' });
        }
    } catch (error) {
        res.status(400).json({ error: error.message });
    }
});

// Eliminar una serie existente
router.delete('/api/series/:id', async (req, res) => {
    try {
        const numFilasEliminadas = await db.series.destroy({
            where: { IdSerie: req.params.id },
        });
        if (numFilasEliminadas === 1) {
            res.json({ message: 'Serie eliminada correctamente' });
        } else {
            res.status(404).json({ error: 'Serie no encontrada' });
        }
    } catch (error) {
        res.status(500).json({ error: 'Error al eliminar la serie' });
    }
});

module.exports = router;
