const express = require("express");
const router = express.Router();
const db = require("../base-orm/sequelize-init");
const { Op } = require("sequelize");

router.get("/api/socios", async function (req, res) {
  let where = {};
  if (req.query.ApeNomSocio != undefined && req.query.ApeNomSocio !== "") {
    where.ApeNomSocio = {
      [Op.like]: "%" + req.query.ApeNomSocio + "%",
    };
  }

  try {
    let items = await db.socios.findAll({
      attributes: [
        "IdSocio",
        "ApeNomSocio",
        "NroSocio"
      ],
      order: [["ApeNomSocio", "ASC"]],
      where,
    });
    res.json(items);
  } catch (error) {
    console.error('Error al obtener los socios:', error);
    res.status(500).json({ error: 'Ocurrió un error al obtener los socios' });
  }
});

module.exports = router;

