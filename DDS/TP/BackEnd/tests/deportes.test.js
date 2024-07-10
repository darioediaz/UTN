const request = require('supertest');
const express = require('express');
const router = require('../routes/deportes');
const app = express();

app.use(express.json());
app.use(router);

describe('Endpoints de Deportes', () => {
  // Test para GET /api/deportes
  it('Debería manejar errores en obtener todos los deportes', async () => {
    const response = await request(app).get('/api/deportes');
    expect(response.status).toBe(500);
    expect(response.body).toEqual({ error: 'Error al obtener los deportes' });
  });

  // Test para GET /api/deportes/:id
  it('Debería manejar errores en obtener un deporte por su ID', async () => {
    const response = await request(app).get('/api/deportes/999'); // ID que no existe
    expect(response.status).toBe(500);
    expect(response.body).toEqual({ error: 'Error al obtener el deporte' });
  });

  // Test para POST /api/deportes
  it('Debería manejar errores en crear un nuevo deporte', async () => {
    const nuevoDeporte = {
      Nombre: 'Nuevo Deporte',
      CantidadJugadores: 22,
      FechaFundacion: '2000-01-01',
      PaisOrigen: 'Argentina'
    };
    const response = await request(app)
      .post('/api/deportes')
      .send(nuevoDeporte);
    expect(response.status).toBe(400);
    expect(response.body).toHaveProperty('error');
  });

  // Test para PUT /api/deportes/:id
  it('Debería manejar errores en actualizar un deporte', async () => {
    const response = await request(app)
      .put('/api/deportes/8888') // ID que no existe
      .send({ Nombre: 'Nombre Actualizado' });
    expect(response.status).toBe(400);
  });

  // Test para DELETE /api/deportes/:id
  it('Debería manejar errores en eliminar un deporte', async () => {
    const response = await request(app).delete('/api/deportes/a'); // ID que no existe
    expect(response.status).toBe(500);
    expect(response.body).toEqual({ error: 'Error al eliminar el deporte' });
  });
});
