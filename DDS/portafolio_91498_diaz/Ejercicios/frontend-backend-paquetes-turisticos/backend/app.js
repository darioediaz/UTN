const express = require("express");
const { Sequelize, DataTypes, Op } = require("sequelize");
const cors = require("cors");

// Configura la aplicación Express
const app = express();
app.use(express.json());
app.use(cors());

// Configura la conexión Sequelize (base de datos SQLite en memoria)
const sequelize = new Sequelize("sqlite::memory:");

// Define el modelo Paquete
const Paquete = sequelize.define(
  "Paquete",
  {
    destino: DataTypes.STRING,
    duracion: DataTypes.STRING,
    precio: DataTypes.INTEGER,
    descripcion: DataTypes.STRING,
  },
  { timestamps: false }
);

// Inicializa la base de datos e inserta datos de muestra
async function inicializarBaseDeDatos() {
  await sequelize.sync({ force: true });
  await Paquete.bulkCreate([
    {
      destino: "Cancún, México",
      duracion: "7 días",
      precio: 1200,
      descripcion: "Disfruta de playas paradisíacas y ruinas mayas.",
    },
    {
      destino: "Machu Picchu, Perú",
      duracion: "5 días",
      precio: 850,
      descripcion: "Explora la ciudad perdida de los Incas en los Andes.",
    },
    {
      destino: "Roma, Italia",
      duracion: "10 días",
      precio: 1500,
      descripcion: "Descubre la historia y cultura de la antigua Roma.",
    },
    {
      destino: "París, Francia",
      duracion: "5 días",
      precio: 1300,
      descripcion: "Romance y cultura en la ciudad de la luz.",
    },
    {
      destino: "Tokio, Japón",
      duracion: "8 días",
      precio: 2100,
      descripcion: "Experimenta la mezcla de tradición y modernidad.",
    },
    {
      destino: "Nueva York, USA",
      duracion: "6 días",
      precio: 1700,
      descripcion: "La ciudad que nunca duerme.",
    },
    {
      destino: "Londres, Inglaterra",
      duracion: "7 días",
      precio: 1450,
      descripcion: "Historia y cultura en la capital británica.",
    },
    {
      destino: "Río de Janeiro, Brasil",
      duracion: "5 días",
      precio: 900,
      descripcion: "Playas, carnaval y el Cristo Redentor.",
    },
    {
      destino: "Buenos Aires, Argentina",
      duracion: "4 días",
      precio: 550,
      descripcion: "Tango, gastronomía y cultura porteña.",
    },
    {
      destino: "Madrid, España",
      duracion: "6 días",
      precio: 1100,

      descripcion: "Arte, historia y vida nocturna.",
    },
  ]);
}

// Endpoint para obtener los paquete
app.get("/paquetes", async (req, res) => {
  try {
    const paquete = await Paquete.findAll();
    res.json(paquete);
  } catch (error) {
    res.status(500).send({ message: "Error al recuperar los paquetes" });
  }
});

// Inicia el servidor
inicializarBaseDeDatos().then(() => {
  app.listen(3000, () =>
    console.log("Servidor corriendo en http://localhost:3000")
  );
});

// Endpoint para agregar un paquete
app.post("/paquetes", async (req, res) => {
  try {
    const paquete = await Paquete.create(req.body);
    res.json(paquete);
  } catch (error) {
    res.status(500).send({ message: "Error al agregar el paquete" });
  }
});

// Endpoint para eliminar un paquete
app.delete("/paquetes/:id", async (req, res) => {
  try {
    const id = req.params.id;
    await Paquete.destroy({ where: { id } });
    res.sendStatus(204); // Sin contenido
  } catch (error) {
    res.status(500).send({ message: "Error al eliminar el paquete" });
  }
});

// Endpoint para filtrar un paquete
app.get("/paquetes", async (req, res) => {
  try {
    const descripcion = req.query.descripcion || ''; // Obtener el valor del query

    const paquetes = await Paquete.findAll({
      where: {
        descripcion: {
          [Op.like]: `%${descripcion}`
        }
      }
    });

    res.json(paquetes);
  } catch (error) {
    res.status(500).send({ message: "Error al recuperar los paquetes" });
  }
});
