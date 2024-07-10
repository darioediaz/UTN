const request = require('supertest');
const express = require('express');
const router = require('../routes/artistas'); 
const app = express();

app.use(express.json());
app.use(router);

describe('Endpoints de Artistas', () => {
  // Test para GET /api/artistas
  it('Debería manejar errores en obtener todos los artistas', async () => {
    const response = await request(app).get('/api/artistas');
    expect(response.status).toBe(500);
    expect(response.body).toEqual({ error: 'Error al obtener los artistas' });
  });

  // Test para GET /api/artistas/:id
  it('Debería manejar errores en obtener un artista por su ID', async () => {
    const response = await request(app).get('/api/artistas/999'); // ID que no existe
    expect(response.status).toBe(500);
    expect(response.body).toEqual({ error: 'Error al obtener el artista' });
  });

  // Test para POST /api/artistas
  it('Debería manejar errores en crear un nuevo artista', async () => {
    const nuevoArtista = {
      Nombre: 'Nuevo Artista',
      FechaNacimiento: '1990-01-01',
      Nacionalidad: 'Desconocida'
    };
    const response = await request(app)
      .post('/api/artistas')
      .send(nuevoArtista);
    expect(response.status).toBe(400);
    expect(response.body).toHaveProperty('error');
  });

  // Test para PUT /api/artistas/:id
  it('Debería manejar errores en actualizar un artista', async () => {
    const response = await request(app)
      .put('/api/artistas/8888') // ID que no existe
      .send({ Nombre: 'Nombre Actualizado' });
    expect(response.status).toBe(400);
  });

  // Test para DELETE /api/artistas/:id
  it('Debería manejar errores en eliminar un artista', async () => {
    const response = await request(app).delete('/api/artistas/a'); // ID que no existe
    expect(response.status).toBe(500);
    expect(response.body).toEqual({ error: 'Error al eliminar el artista' });
  });
});
