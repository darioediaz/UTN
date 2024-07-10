const { Sequelize, DataTypes } = require("sequelize");

// Reutilizamos la instancia de Sequelize
// const sequelize = require("./sequelize").sequelize;
const sequelize = new Sequelize("sqlite:" + "./.data/tpdds.db");

// Modelo para libros
const libros = sequelize.define("libros", {
  IdLibro: {
    type: DataTypes.INTEGER,
    primaryKey: true,
    autoIncrement: true,
  },
  Titulo: {
    type: DataTypes.STRING(100),
    allowNull: false,
    validate: {
      notEmpty: {
        args: true,
        msg: "Título es requerido",
      },
      len: {
        args: [1, 100],
        msg: "Título debe tener entre 1 y 100 caracteres",
      },
    },
  },
  Precio: {
    type: DataTypes.DECIMAL(10, 2),
    allowNull: false,
    validate: {
      notNull: {
        args: true,
        msg: "Precio es requerido",
      },
    },
  },
  FechaPublicacion: {
    type: DataTypes.DATEONLY,
    allowNull: false,
    validate: {
      notNull: {
        args: true,
        msg: "Fecha de publicación es requerida",
      },
      isDate: {
        args: true,
        msg: "Fecha de publicación debe ser una fecha válida",
      },
    },
  },
}, { timestamps: false });

// Modelo para películas
const peliculas = sequelize.define("peliculas", {
  IdPelicula: {
    type: DataTypes.INTEGER,
    primaryKey: true,
    autoIncrement: true,
  },
  Titulo: {
    type: DataTypes.STRING(100),
    allowNull: false,
    validate: {
      notEmpty: {
        args: true,
        msg: "Título es requerido",
      },
      len: {
        args: [1, 100],
        msg: "Título debe tener entre 1 y 100 caracteres",
      },
    },
  },
  Precio: {
    type: DataTypes.DECIMAL(10, 2),
    allowNull: false,
    validate: {
      notNull: {
        args: true,
        msg: "Precio es requerido",
      },
    },
  },
  FechaEstreno: {
    type: DataTypes.DATEONLY,
    allowNull: false,
    validate: {
      notNull: {
        args: true,
        msg: "Fecha de estreno es requerida",
      },
      isDate: {
        args: true,
        msg: "Fecha de estreno debe ser una fecha válida",
      },
    },
  },
}, { timestamps: false });

// Modelo para canciones
const canciones = sequelize.define("canciones", {
  IdCancion: {
    type: DataTypes.INTEGER,
    primaryKey: true,
    autoIncrement: true,
  },
  Titulo: {
    type: DataTypes.STRING(100),
    allowNull: false,
    validate: {
      notEmpty: {
        args: true,
        msg: "Título es requerido",
      },
      len: {
        args: [1, 100],
        msg: "Título debe tener entre 1 y 100 caracteres",
      },
    },
  },
  DuracionSegundos: {
    type: DataTypes.INTEGER,
    allowNull: false,
    validate: {
      notNull: {
        args: true,
        msg: "Duración en segundos es requerida",
      },
    },
  },
  FechaLanzamiento: {
    type: DataTypes.DATEONLY,
    allowNull: false,
    validate: {
      notNull: {
        args: true,
        msg: "Fecha de lanzamiento es requerida",
      },
      isDate: {
        args: true,
        msg: "Fecha de lanzamiento debe ser una fecha válida",
      },
    },
  },
}, { timestamps: false });

// Modelo para juegos
const juegos = sequelize.define("juegos", {
  IdJuego: {
    type: DataTypes.INTEGER,
    primaryKey: true,
    autoIncrement: true,
  },
  Titulo: {
    type: DataTypes.STRING(100),
    allowNull: false,
    validate: {
      notEmpty: {
        args: true,
        msg: "Título es requerido",
      },
      len: {
        args: [1, 100],
        msg: "Título debe tener entre 1 y 100 caracteres",
      },
    },
  },
  Puntuacion: {
    type: DataTypes.INTEGER,
    allowNull: false,
    validate: {
      notNull: {
        args: true,
        msg: "Puntuación es requerida",
      },
    },
  },
  FechaLanzamiento: {
    type: DataTypes.DATEONLY,
    allowNull: false,
    validate: {
      notNull: {
        args: true,
        msg: "Fecha de lanzamiento es requerida",
      },
      isDate: {
        args: true,
        msg: "Fecha de lanzamiento debe ser una fecha válida",
      },
    },
  },
}, { timestamps: false });


// Definir el modelo para la tabla 'artistas'
const artistas = sequelize.define('artista', {
  IdArtista: {
    type: DataTypes.INTEGER,
    primaryKey: true,
    autoIncrement: true
  },
  Nombre: {
    type: DataTypes.STRING(100),
    allowNull: false,
    validate: {
      notEmpty: {
        args: true,
        msg: 'Nombre es requerido'
      },
      len: {
        args: [1, 100],
        msg: 'Nombre debe tener entre 1 y 100 caracteres'
      }
    }
  },
  FechaNacimiento: {
    type: DataTypes.DATEONLY,
    allowNull: false,
    validate: {
      notNull: {
        args: true,
        msg: 'Fecha de nacimiento es requerida'
      },
      isDate: {
        args: true,
        msg: 'Fecha de nacimiento debe ser una fecha válida'
      }
    }
  },
  Nacionalidad: {
    type: DataTypes.STRING(50),
    allowNull: false,
    validate: {
      notEmpty: {
        args: true,
        msg: 'Nacionalidad es requerida'
      },
      len: {
        args: [1, 50],
        msg: 'Nacionalidad debe tener entre 1 y 50 caracteres'
      }
    }
  },
  Descripcion: {
    type: DataTypes.TEXT,
    allowNull: true
  }
}, {
  timestamps: false,
  tableName: 'artistas'
});


// Modelo para series
const series = sequelize.define("series", {
  IdSerie: {
    type: DataTypes.INTEGER,
    primaryKey: true,
    autoIncrement: true,
  },
  Titulo: {
    type: DataTypes.STRING(100),
    allowNull: false,
    validate: {
      notEmpty: {
        args: true,
        msg: "Título es requerido",
      },
      len: {
        args: [1, 100],
        msg: "Título debe tener entre 1 y 100 caracteres",
      },
    },
  },
  NumTemporadas: {
    type: DataTypes.INTEGER,
    allowNull: false,
    validate: {
      notNull: {
        args: true,
        msg: "Número de temporadas es requerido",
      },
      isInt: {
        args: true,
        msg: "Número de temporadas debe ser un número entero",
      },
      min: {
        args: 1,
        msg: "Número de temporadas debe ser mayor o igual a 1",
      },
    },
  },
  FechaEstreno: {
    type: DataTypes.DATEONLY,
    allowNull: false,
    validate: {
      notNull: {
        args: true,
        msg: "Fecha de estreno es requerida",
      },
      isDate: {
        args: true,
        msg: "Fecha de estreno debe ser una fecha válida",
      },
    },
  },
}, {
  timestamps: false,
});


// Modelo para deportes
const deportes = sequelize.define("deporte", {
  IdDeporte: {
    type: DataTypes.INTEGER,
    primaryKey: true,
    autoIncrement: true,
  },
  Nombre: {
    type: DataTypes.STRING(100),
    allowNull: false,
    validate: {
      notEmpty: {
        args: true,
        msg: "Nombre es requerido",
      },
      len: {
        args: [1, 100],
        msg: "Nombre debe tener entre 1 y 100 caracteres",
      },
    },
  },
  CantidadJugadores: {
    type: DataTypes.INTEGER,
    validate: {
      isInt: {
        args: true,
        msg: "Cantidad de jugadores debe ser un número entero",
      },
      min: {
        args: 1,
        msg: "Cantidad de jugadores debe ser mayor o igual a 1",
      },
    },
  },
  FechaFundacion: {
    type: DataTypes.DATEONLY,
    validate: {
      isDate: {
        args: true,
        msg: "Fecha de fundación debe ser una fecha válida",
      },
    },
  },
  PaisOrigen: {
    type: DataTypes.STRING(100),
    allowNull: false,
    validate: {
      notEmpty: {
        args: true,
        msg: "País de origen es requerido",
      },
      len: {
        args: [1, 100],
        msg: "País de origen debe tener entre 1 y 100 caracteres",
      },
    },
  },
}, {
  timestamps: false,
});


const redesSociales = sequelize.define("redes_sociales", {
  IdRedSocial: {
    type: DataTypes.INTEGER,
    primaryKey: true,
    autoIncrement: true,
  },
  Nombre: {
    type: DataTypes.STRING(100),
    allowNull: false,
    validate: {
      notEmpty: {
        args: true,
        msg: "El nombre es requerido",
      },
      len: {
        args: [1, 100],
        msg: "El nombre debe tener entre 1 y 100 caracteres",
      },
    },
  },
  UsuariosActivos: {
    type: DataTypes.INTEGER,
    validate: {
      isInt: {
        args: true,
        msg: "La cantidad de usuarios activos debe ser un número entero",
      },
    },
  },
  FechaCreacion: {
    type: DataTypes.DATEONLY,
    validate: {
      isDate: {
        args: true,
        msg: "La fecha de creación debe ser una fecha válida",
      },
    },
  },
}, {
  timestamps: false, // Para deshabilitar los timestamps automáticos (createdAt, updatedAt)
});


const Series = sequelize.define("series", {
  IdSerie: {
    type: DataTypes.INTEGER,
    primaryKey: true,
    autoIncrement: true,
  },
  Titulo: {
    type: DataTypes.STRING(100),
    allowNull: false,
    validate: {
      notEmpty: {
        args: true,
        msg: "El título es requerido",
      },
      len: {
        args: [1, 100],
        msg: "El título debe tener entre 1 y 100 caracteres",
      },
    },
  },
  NumTemporadas: {
    type: DataTypes.INTEGER,
    validate: {
      isInt: {
        args: true,
        msg: "El número de temporadas debe ser un número entero",
      },
      min: {
        args: 0,
        msg: "El número de temporadas no puede ser negativo",
      },
    },
  },
  FechaEstreno: {
    type: DataTypes.DATEONLY,
    validate: {
      isDate: {
        args: true,
        msg: "La fecha de estreno debe ser una fecha válida",
      },
    },
  },
}, {
  timestamps: false, // Para deshabilitar los timestamps automáticos (createdAt, updatedAt)
});

module.exports = Series;

module.exports = {
  sequelize,
  libros,
  peliculas,
  canciones,
  juegos,
  artistas,
  series,
  deportes,
  redesSociales
};
