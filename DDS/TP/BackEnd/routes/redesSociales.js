const express = require('express');
const { Op, ValidationError } = require("sequelize");
const router = express.Router();
const db = require("../base-orm/sequelize-init");


// Obtener todas las redes sociales
router.get('/api/redes-sociales', async (req, res) => {
    try {
        let where = {};
        if (req.query.Nombre && req.query.Nombre !== "") {
            where.Nombre = {
                [Op.like]: "%" + req.query.Nombre + "%",
            };
        }

        const pagina = req.query.pagina ? parseInt(req.query.pagina) : 1;
        const tamañoPagina = 10;

        const { count, rows } = await db.redesSociales.findAndCountAll({
            attributes: [
                "IdRedSocial",
                "Nombre",
                "UsuariosActivos",
                "FechaCreacion",
            ],
            order: [["nombre", "ASC"]],
            where,
            offset: (pagina - 1) * tamañoPagina,
            limit: tamañoPagina,
        });

        return res.json({ Items: rows, registrosTotal: count });
    } catch (error) {
        console.error("Error al obtener las redes sociales:", error);
        res.status(500).json({ error: 'Error al obtener las redes sociales' });
    }
});

// Obtener una red social por su ID
router.get('/api/redes-sociales/:id', async (req, res) => {
    try {
        const redSocial = await db.redesSociales.findByPk(req.params.id);
        if (redSocial) {
            res.json(redSocial);
        } else {
            res.status(404).json({ error: 'Red social no encontrada' });
        }
    } catch (error) {
        console.error("Error al obtener la red social:", error);
        res.status(500).json({ error: 'Error al obtener la red social' });
    }
});

// Crear una nueva red social
router.post('/api/redes-sociales', async (req, res) => {
    const { IdRedSocial, ...datosRedSocial } = req.body;
    try {
        const nuevaRedSocial = await db.redesSociales.create(datosRedSocial);
        res.status(201).json(nuevaRedSocial);
    } catch (error) {
        console.error("Error al crear la red social:", error);
        res.status(400).json({ error: error.message });
    }
});

// Actualizar una red social existente
router.put('/api/redes-sociales/:id', async (req, res) => {
    console.log(req.params.id)
    try {
        const [numFilasActualizadas, redSocialActualizada] = await db.redesSociales.update(req.body, {
            where: { IdRedSocial: req.params.id },
            returning: true,
        });
        if (redSocialActualizada > 0) {
            res.json(redSocialActualizada[0]);
        } else {
            res.status(404).json({ error: 'Red social no encontrada' });
        }
    } catch (error) {
        console.error("Error al actualizar la red social:", error);
        res.status(400).json({ error: error.message });
    }
});

// Eliminar una red social existente
router.delete('/api/redes-sociales/:id', async (req, res) => {
    try {
        const numFilasEliminadas = await db.redesSociales.destroy({
            where: { IdRedSocial: req.params.id },
        });
        if (numFilasEliminadas > 0) {
            res.json({ message: 'Red social eliminada correctamente' });
        } else {
            res.status(404).json({ error: 'Red social no encontrada' });
        }
    } catch (error) {
        console.error("Error al eliminar la red social:", error);
        res.status(500).json({ error: 'Error al eliminar la red social' });
    }
});

module.exports = router;
