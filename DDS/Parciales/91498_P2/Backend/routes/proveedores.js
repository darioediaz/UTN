const express = require('express');
const { Op, ValidationError } = require("sequelize");
const router = express.Router();
const db = require("../base-orm/sequelize-init");

// Obtener todos los Proveedores
router.get('/api/proveedores', async (req, res) => {
  try {
    const { count, rows } = await db.proveedores.findAndCountAll({
        attributes: [
          "IdProveedor",
          "RazonSocial",
          "Telefono",
          "FechaAlta"
        ],
        order: [["RazonSocial", "ASC"]],
      });
    
      return res.json({ Items: rows, RegistrosTotal: count });  } catch (error) {
    res.status(500).json({ error: 'Error al obtener los Proveedores' });
  }
});

// Crear un nuevo empleado
router.post('/api/proveedores', async (req, res) => {
  try {
    const nuevoProveedor = await db.proveedores.create(
      {
        RazonSocial: req.body.RazonSocial,
        Telefono: req.body.Telefono,
        FechaAlta: req.body.FechaAlta
      });
    res.status(200).json(nuevoProveedor);
  } catch (error) {
    res.status(400).json({ error: error.message });
  }
});

module.exports = router;