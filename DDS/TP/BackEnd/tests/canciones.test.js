const request = require('supertest');
const express = require('express');
const router = require('../routes/canciones');
const app = express();

app.use(express.json());
app.use(router);

describe('Endpoints de Canciones', () => {
  // Test para GET /api/canciones
  it('Debería manejar errores en obtener todas las canciones', async () => {
    const response = await request(app).get('/api/canciones');
    expect(response.status).toBe(500);
    expect(response.body).toEqual({ error: 'Error al obtener las canciones' });
  });

  // Test para GET /api/canciones/:id
  it('Debería manejar errores en obtener una canción por su ID', async () => {
    const response = await request(app).get('/api/canciones/999'); // ID que no existe
    expect(response.status).toBe(500);
    expect(response.body).toEqual({ error: 'Error al obtener la cancion' });
  });

  // Test para POST /api/canciones
  it('Debería manejar errores en crear una nueva canción', async () => {
    const nuevaCancion = {
      Titulo: 'Nueva Canción',
      DuracionSegundos: 180,
      FechaLanzamiento: '2023-01-01',
    };
    const response = await request(app)
      .post('/api/canciones')
      .send(nuevaCancion);
    expect(response.status).toBe(400);
    expect(response.body).toHaveProperty('error');
  });

  // Test para PUT /api/canciones/:id
  it('Debería manejar errores en actualizar una canción', async () => {
    const response = await request(app)
      .put('/api/canciones/8888') // ID que no existe
      .send({ Titulo: 'Título Actualizado' });
    expect(response.status).toBe(400);
  });

  // Test para DELETE /api/canciones/:id
  it('Debería manejar errores en eliminar una canción', async () => {
    const response = await request(app).delete('/api/canciones/a'); // ID que no existe
    expect(response.status).toBe(500);
    expect(response.body).toEqual({ error: 'Error al eliminar la cancion' });
  });
});
