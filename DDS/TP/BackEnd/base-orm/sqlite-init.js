const db = require("aa-sqlite");
// const { sequelize } = require("./sequelize-init");

async function CrearBaseSiNoExiste() {
  // Abrir base, si no existe el archivo/base lo crea
  await db.open("./.data/tpdds.db");

  let existe = false;
  let res = null;

  // Verificar si existen las tablas de películas, libros, canciones y juegos
  res = await db.get(
    "SELECT count(*) as contar FROM sqlite_schema WHERE type = 'table' and name= 'peliculas'",
    []
  );
  if (res.contar > 0) existe = true;
  if (!existe) {
    // Crear tabla de películas
    await db.run(
      `CREATE TABLE peliculas (
          IdPelicula INTEGER PRIMARY KEY AUTOINCREMENT,
          Titulo TEXT NOT NULL,
          Precio REAL NOT NULL,
          FechaEstreno DATE NOT NULL
        );`
    );
    console.log("Tabla peliculas creada!");

    // Insertar datos en la tabla de películas
    await db.run(
      `INSERT INTO peliculas (Titulo, Precio, FechaEstreno)
      VALUES
        ('Titanic', 10.99, '1997-12-19'),
        ('Avatar', 12.99, '2009-12-18'),
        ('Jurassic Park', 9.99, '1993-06-11'),
        ('Inception', 11.99, '2010-07-16'),
        ('The Dark Knight', 12.99, '2008-07-18'),
        ('Forrest Gump', 9.99, '1994-07-06'),
        ('The Shawshank Redemption', 10.99, '1994-10-14'),
        ('The Lord of the Rings: The Fellowship of the Ring', 11.99, '2001-12-19'),
        ('The Godfather', 11.99, '1972-03-24'),
        ('Interstellar', 12.99, '2014-11-07');`
    );
    console.log("Datos de películas insertados!");
  }

  // Verificar si existen las tablas de libros, canciones y juegos
  res = await db.get(
    "SELECT count(*) as contar FROM sqlite_schema WHERE type = 'table' and name= 'libros'",
    []
  );
  if (res.contar > 0) existe = true;
  if (!existe) {
    // Crear tabla de libros
    await db.run(
      `CREATE TABLE libros (
          IdLibro INTEGER PRIMARY KEY AUTOINCREMENT,
          Titulo TEXT NOT NULL,
          Precio REAL NOT NULL,
          FechaPublicacion DATE NOT NULL
        );`
    );
    console.log("Tabla libros creada!");

    // Insertar datos en la tabla de libros
    await db.run(
      `INSERT INTO libros (Titulo, Precio, FechaPublicacion)
      VALUES
        ('Harry Potter y la Piedra Filosofal', 15.99, '1997-06-26'),
        ('El Señor de los Anillos: La Comunidad del Anillo', 18.99, '1954-07-29'),
        ('Cien años de soledad', 12.99, '1967-05-30'),
        ('El código Da Vinci', 14.99, '2003-03-18'),
        ('1984', 11.99, '1949-06-08'),
        ('Orgullo y prejuicio', 10.99, '1813-01-28'),
        ('El Alquimista', 13.99, '1988-01-01'),
        ('La sombra del viento', 12.99, '2001-04-01'),
        ('El Principito', 9.99, '1943-04-06'),
        ('La Odisea', 14.99, '800 a.C.');`
    );
    console.log("Datos de libros insertados!");
  }

  // Verificar si existen las tablas de canciones
  res = await db.get(
    "SELECT count(*) as contar FROM sqlite_schema WHERE type = 'table' and name= 'canciones'",
    []
  );
  if (res.contar > 0) existe = true;
  if (!existe) {
    // Crear tabla de canciones
    await db.run(
      `CREATE TABLE canciones (
          IdCancion INTEGER PRIMARY KEY AUTOINCREMENT,
          Titulo TEXT NOT NULL,
          DuracionSegundos INTEGER NOT NULL,
          FechaLanzamiento DATE NOT NULL
        );`
    );
    console.log("Tabla canciones creada!");

    // Insertar datos en la tabla de canciones
    await db.run(
      `INSERT INTO canciones (Titulo, DuracionSegundos, FechaLanzamiento)
      VALUES
        ('Bohemian Rhapsody', 354, '1975-10-31'),
        ('Hotel California', 391, '1976-12-08'),
        ('Smells Like Teen Spirit', 302, '1991-09-10'),
        ('Imagine', 185, '1971-10-11'),
        ('Stairway to Heaven', 482, '1971-11-08'),
        ('Yesterday', 123, '1965-08-06'),
        ('Like a Rolling Stone', 369, '1965-07-20'),
        ('Hey Jude', 431, '1968-08-26'),
        ('My Way', 264, '1969-03-14'),
        ('Thunderstruck', 292, '1990-09-10');`
    );
    console.log("Datos de canciones insertados!");
  }

  // Verificar si existen las tablas de juegos
  res = await db.get(
    "SELECT count(*) as contar FROM sqlite_schema WHERE type = 'table' and name= 'juegos'",
    []
  );
  if (res.contar > 0) existe = true;
  if (!existe) {
    // Crear tabla de juegos
    await db.run(
      `CREATE TABLE juegos (
          IdJuego INTEGER PRIMARY KEY AUTOINCREMENT,
          Titulo TEXT NOT NULL,
          Puntuacion INTEGER NOT NULL,
          FechaLanzamiento DATE NOT NULL
        );`
    );
    console.log("Tabla juegos creada!");

    // Insertar datos en la tabla de juegos
    await db.run(
      `INSERT INTO juegos (Titulo, Puntuacion, FechaLanzamiento)
      VALUES
        ('The Legend of Zelda: Breath of the Wild', 95, '2017-03-03'),
        ('Super Mario Odyssey', 97, '2017-10-27'),
        ('The Witcher 3: Wild Hunt', 93, '2015-05-19'),
        ('Red Dead Redemption 2', 97, '2018-10-26'),
        ('Grand Theft Auto V', 96, '2013-09-17'),
        ('God of War', 94, '2018-04-20'),
        ('The Elder Scrolls V: Skyrim', 94, '2011-11-11'),
        ('Dark Souls III', 89, '2016-04-12'),
        ('Bloodborne', 92, '2015-03-24'),
        ('Persona 5', 93, '2016-09-15');`
    );
    console.log("Datos de juegos insertados!");
  }

  // Verificar si existen las tablas de series
  res = await db.get(
    "SELECT count(*) as contar FROM sqlite_schema WHERE type = 'table' and name= 'series'",
    []
  );
  if (res.contar > 0) existe = true;
  if (!existe) {
    // Crear tabla de series
    await db.run(
      `CREATE TABLE series (
        IdSerie INTEGER PRIMARY KEY AUTOINCREMENT,
        Titulo TEXT NOT NULL,
        NumTemporadas INTEGER NOT NULL,
        FechaEstreno DATE NOT NULL
      );`
    );
    console.log("Tabla series creada!");

    // Insertar datos en la tabla de series
    await db.run(
      `INSERT INTO series (Titulo, NumTemporadas, FechaEstreno)
    VALUES
      ('Breaking Bad', 5, '2008-01-20'),
      ('Game of Thrones', 8, '2011-04-17'),
      ('Stranger Things', 4, '2016-07-15'),
      ('The Witcher', 3, '2019-12-20'),
      ('The Mandalorian', 2, '2019-11-12'),
      ('Friends', 10, '1994-09-22'),
      ('The Office', 9, '2005-03-24'),
      ('Sherlock', 4, '2010-07-25'),
      ('Westworld', 3, '2016-10-02'),
      ('The Crown', 4, '2016-11-04');`
    );
    console.log("Datos de series insertados!");
  }

// Verificar si existen las tablas de artistas
res = await db.get(
  "SELECT count(*) as contar FROM sqlite_schema WHERE type = 'table' and name= 'artistas'",
  []
);
if (res.contar > 0) existe = true;
if (!existe) {
  // Crear tabla de artistas
  await db.run(
    `CREATE TABLE artistas (
        IdArtista INTEGER PRIMARY KEY AUTOINCREMENT,
        Nombre TEXT NOT NULL,
        FechaNacimiento DATE NOT NULL,
        Nacionalidad TEXT NOT NULL,
        Descripcion TEXT NOT NULL
      );`
  );
  console.log("Tabla artistas creada!");

  // Insertar datos en la tabla de artistas
  await db.run(
    `INSERT INTO artistas (Nombre, FechaNacimiento, Nacionalidad, Descripcion)
    VALUES
      ('Luis Alberto Spinetta', '1950-01-23', 'Argentino', 'Músico, cantautor y poeta, uno de los más importantes del rock argentino.'),
      ('Charly García', '1951-10-23', 'Argentino', 'Cantante, compositor y músico, ícono del rock en español.'),
      ('Gustavo Cerati', '1959-08-11', 'Argentino', 'Cantante, compositor y productor, líder de la banda Soda Stereo.'),
      ('Fito Páez', '1963-03-13', 'Argentino', 'Cantante, compositor y pianista, conocido por su influencia en el rock latino.'),
      ('Andrés Calamaro', '1961-08-22', 'Argentino', 'Cantante, compositor y productor, ex miembro de Los Abuelos de la Nada.'),
      ('Carlos "Indio" Solari', '1949-01-17', 'Argentino', 'Cantante y compositor, conocido por su trabajo con Patricio Rey y sus Redonditos de Ricota.'),
      ('Ricardo Mollo', '1957-08-17', 'Argentino', 'Guitarrista y cantante, miembro de Sumo y líder de Divididos.'),
      ('Fabiana Cantilo', '1959-03-03', 'Argentino', 'Cantante y compositora, conocida por su carrera en solitario y colaboraciones con otros músicos de rock.'),
      ('Pedro Aznar', '1959-07-23', 'Argentino', 'Músico, compositor y cantante, miembro de Serú Girán y colaborador de músicos internacionales.'),
      ('Luca Prodan', '1953-05-17', 'Argentino', 'Cantante y líder de la banda Sumo, influyente en el rock argentino.');`
  );
  console.log("Datos de artistas insertados!");
}

// Verificar si existen las tablas de deportes
res = await db.get(
  "SELECT count(*) as contar FROM sqlite_schema WHERE type = 'table' and name= 'deportes'",
  []
);
if (res.contar > 0) existe = true;
if (!existe) {
  // Crear tabla de deportes
  await db.run(
    `CREATE TABLE deportes (
        IdDeporte INTEGER PRIMARY KEY AUTOINCREMENT,
        Nombre TEXT NOT NULL,
        CantidadJugadores INTEGER NOT NULL,
        FechaFundacion DATE NOT NULL,
        PaisOrigen TEXT NOT NULL
      );`
  );
  console.log("Tabla deportes creada!");

  // Insertar datos en la tabla de deportes
  await db.run(
    `INSERT INTO deportes (Nombre, CantidadJugadores, FechaFundacion, PaisOrigen)
    VALUES
      ('Fútbol', 11, '1863-10-26', 'Inglaterra'),
      ('Básquetbol', 5, '1891-12-21', 'Estados Unidos'),
      ('Béisbol', 9, '1839-06-19', 'Estados Unidos'),
      ('Hockey sobre césped', 11, '1875-01-01', 'Inglaterra'),
      ('Rugby', 15, '1823-01-01', 'Inglaterra'),
      ('Tenis', 1, '1873-02-23', 'Francia'),
      ('Voleibol', 6, '1895-02-09', 'Estados Unidos'),
      ('Críquet', 11, '1598-05-01', 'Inglaterra'),
      ('Golf', 1, '1552-03-15', 'Escocia'),
      ('Boxeo', 1, '1681-01-06', 'Inglaterra');`
  );
  console.log("Datos de deportes insertados!");
}

// Verificar si existen las tablas de redes sociales
res = await db.get(
  "SELECT count(*) as contar FROM sqlite_schema WHERE type = 'table' and name= 'redes_sociales'",
  []
);
if (res.contar > 0) existe = true;
if (!existe) {
  // Crear tabla de redes sociales
  await db.run(
    `CREATE TABLE redes_sociales (
        IdRedSocial INTEGER PRIMARY KEY AUTOINCREMENT,
        Nombre TEXT NOT NULL,
        UsuariosActivos INTEGER NOT NULL,
        FechaCreacion DATE NOT NULL
      );`
  );
  console.log("Tabla redes sociales creada!");

  // Insertar datos en la tabla de redes sociales
  await db.run(
    `INSERT INTO redes_sociales (Nombre, UsuariosActivos, FechaCreacion)
    VALUES
      ('Facebook', 2900000000, '2004-02-04'),
      ('Instagram', 1000000000, '2010-10-06'),
      ('Twitter', 330000000, '2006-03-21'),
      ('LinkedIn', 830000000, '2003-05-05'),
      ('Snapchat', 530000000, '2011-09-16'),
      ('TikTok', 1000000000, '2016-09-20'),
      ('Pinterest', 450000000, '2010-03-10'),
      ('Reddit', 430000000, '2005-06-23'),
      ('WhatsApp', 2000000000, '2009-01-24'),
      ('YouTube', 2000000000, '2005-02-14');`
  );
  console.log("Datos de redes sociales insertados!");
}

  // Cerrar la base
  db.close();
}

CrearBaseSiNoExiste();

module.exports = CrearBaseSiNoExiste;
