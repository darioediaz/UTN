const request = require('supertest');
const express = require('express');
const router = require('../routes/peliculas')
const app = express();

app.use(express.json());
app.use(router);

describe('Endpoints de Películas', () => {
  // Test para GET /api/peliculas
  it('Debería manejar errores en obtener todas las películas', async () => {
    const response = await request(app).get('/api/peliculas');
    expect(response.status).toBe(500);
    expect(response.body).toEqual({ error: 'Error al obtener las peliculas' });
  });

  // Test para GET /api/peliculas/:id
  it('Debería manejar errores en obtener una película por su ID', async () => {
    const response = await request(app).get('/api/peliculas/999'); // ID que no existe
    expect(response.status).toBe(500);
    expect(response.body).toEqual({ error: 'Error al obtener la pelicula' });
  });

  // Test para POST /api/peliculas
  it('Debería manejar errores en crear una nueva película', async () => {
    const nuevaPelicula = {
      Titulo: 'Nueva Película',
      Precio: 12.99,
      FechaEstreno: '2023-01-01',
    };
    const response = await request(app)
      .post('/api/peliculas')
      .send(nuevaPelicula);
    expect(response.status).toBe(400);
    expect(response.body).toHaveProperty('error');
  });

  // Test para PUT /api/peliculas/:id
  it('Debería manejar errores en actualizar una película', async () => {
    const response = await request(app)
      .put('/api/peliculas/8888') // ID que no existe
      .send({ Titulo: 'Título Actualizado' });
    expect(response.status).toBe(400);
  });

  // Test para DELETE /api/peliculas/:id
  it('Debería manejar errores en eliminar una película', async () => {
    const response = await request(app).delete('/api/peliculas/a'); // ID que no existe
    expect(response.status).toBe(500);
    expect(response.body).toEqual({ error: 'Error al eliminar la pelicula' });
  });
});
