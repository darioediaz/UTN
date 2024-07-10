const request = require('supertest');
const express = require('express');
const router = require('../routes/juegos');
const app = express();

app.use(express.json());
app.use(router);

describe('Endpoints de Juegos', () => {
  // Test para GET /api/juegos
  it('Debería manejar errores en obtener todos los juegos', async () => {
    const response = await request(app).get('/api/juegos');
    expect(response.status).toBe(500);
    expect(response.body).toEqual({ error: 'Error al obtener los juegos' });
  });

  // Test para GET /api/juegos/:id
  it('Debería manejar errores en obtener un juego por su ID', async () => {
    const response = await request(app).get('/api/juegos/999'); // ID que no existe
    expect(response.status).toBe(500);
    expect(response.body).toEqual({ error: 'Error al obtener el juego' });
  });

  // Test para POST /api/juegos
  it('Debería manejar errores en crear un nuevo juego', async () => {
    const nuevoJuego = {
      Titulo: 'Nuevo Juego',
      Puntuacion: 9.5,
      FechaLanzamiento: '2023-01-01',
    };
    const response = await request(app)
      .post('/api/juegos')
      .send(nuevoJuego);
    expect(response.status).toBe(400);
    expect(response.body).toHaveProperty('error');
  });

  // Test para PUT /api/juegos/:id
  it('Debería manejar errores en actualizar un juego', async () => {
    const response = await request(app)
      .put('/api/juegos/8888') // ID que no existe
      .send({ Titulo: 'Título Actualizado' });
    expect(response.status).toBe(400);
  });

  // Test para DELETE /api/juegos/:id
  it('Debería manejar errores en eliminar un juego', async () => {
    const response = await request(app).delete('/api/juegos/a'); // ID que no existe
    expect(response.status).toBe(500);
    expect(response.body).toEqual({ error: 'Error al eliminar el juego' });
  });
});
