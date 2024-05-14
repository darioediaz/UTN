const express = require('express');
const app = express();
const port = 3000;

app.get('/', (req, res) => {
  res.redirect('/acercade');
});
app.get('/acercade', (req, res) => {
  res.send(
    '<html><head></head><body><h1>Bienvenido a desarrollo de apirest con express</h1><body>'
  );
});
app.listen(port, () => {
  console.log(`Aplicacion con express escuchando en el puerto ${port}`);
});

let autosAgencia = [
  { marca: 'Renault', modelo: 'Sandero', anio: 2022, precio: 19000000 },
  { marca: 'Chevrolet', modelo: 'Cruze', anio: 2019, precio: 23000000 },
  { marca: 'Citroen', modelo: 'C 3', anio: 2021, precio: 17000000 },
];

app.get('/autos', (req, res) => {
  let autosAgencia = [
    { marca: 'Renault', modelo: 'Sandero', anio: 2022, precio: 19000000 },
    { marca: 'Chevrolet', modelo: 'Cruze', anio: 2019, precio: 23000000 },
    { marca: 'Citroen', modelo: 'C 3', anio: 2021, precio: 17000000 },
  ];
  res.json(autosAgencia);
});

app.get('/paises', (req, res) => {
  fetch('https://restcountries.com/v3.1/all')
    .then((response) => {
      if (!response.ok) {
        throw new Error('Error al obtener los países');
      }
      return response.json();
    })
    .then((data) => {
      res.json(data);
    })
    .catch((error) => {
      console.error('Error:', error);
    });
});

app.use('', (req, res) => {
  res.send(
    '<!doctype html><html><head></head><body><h1>Ruta desconocida</h1><body></html>'
  );
});
