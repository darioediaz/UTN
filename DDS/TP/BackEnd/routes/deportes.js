const express = require('express');
const { Op, ValidationError } = require("sequelize");
const router = express.Router();
const db = require("../base-orm/sequelize-init");

// Obtener todos los deportes
router.get('/api/deportes', async (req, res) => {
    try {
        let where = {};
        if (req.query.Nombre != undefined && req.query.Nombre !== "") {
            where.Nombre = {
                [Op.like]: "%" + req.query.Nombre + "%",
            };
        }
        const Pagina = req.query.Pagina ?? 1;
        const TamañoPagina = 10;
        const { count, rows } = await db.deportes.findAndCountAll({
            attributes: [
                "IdDeporte",
                "Nombre",
                "CantidadJugadores",
                "FechaFundacion",
                "PaisOrigen",
            ],
            order: [["Nombre", "ASC"]],
            where,
            offset: (Pagina - 1) * TamañoPagina,
            limit: TamañoPagina,
        });

        return res.json({ Items: rows, RegistrosTotal: count });
    } catch (error) {
        res.status(500).json({ error: 'Error al obtener los deportes' });
    }
});

// Obtener un deporte por su Id
router.get('/api/deportes/:id', async (req, res) => {
    try {
        const deporte = await db.deportes.findByPk(req.params.id);
        if (deporte) {
            res.json(deporte);
        } else {
            res.status(404).json({ error: 'Deporte no encontrado' });
        }
    } catch (error) {
        res.status(500).json({ error: 'Error al obtener el deporte' });
    }
});

// Crear un nuevo deporte
router.post('/api/deportes', async (req, res) => {
    const { IdDeporte, ...datosDeporte} = req.body;
    try {
        const nuevoDeporte = await db.deportes.create(datosDeporte);
        res.status(200).json(nuevoDeporte);
    } catch (error) {
        res.status(400).json({ error: error.message });
    }
});

// Actualizar un deporte existente
router.put('/api/deportes/:id', async (req, res) => {
    try {
        const [numFilasActualizadas, deportesActualizados] = await db.deportes.update(req.body, {
            where: { IdDeporte: req.params.id },
            returning: true,
        });
        if (deportesActualizados === 1) {
            res.sendStatus(204);
        } else {
            res.status(404).json({ error: 'Deporte no encontrado' });
        }
    } catch (error) {
        res.status(400).json({ error: error.message });
    }
});

// Eliminar un deporte existente
router.delete('/api/deportes/:id', async (req, res) => {
    try {
        const numFilasEliminadas = await db.deportes.destroy({
            where: { IdDeporte: req.params.id },
        });
        if (numFilasEliminadas === 1) {
            res.json({ message: 'Deporte eliminado correctamente' });
        } else {
            res.status(404).json({ error: 'Deporte no encontrado' });
        }
    } catch (error) {
        res.status(500).json({ error: 'Error al eliminar el deporte' });
    }
});

module.exports = router;
