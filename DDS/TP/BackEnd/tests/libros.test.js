const request = require('supertest');
const express = require('express');
const router = require('../routes/libros'); 
const app = express();

app.use(express.json());
app.use(router);

describe('Endpoints de Libros', () => {
  // Test para GET /api/libros
  it('Debería manejar errores en obtener todos los libros', async () => {
    const response = await request(app).get('/api/libros');
    expect(response.status).toBe(500);
    expect(response.body).toEqual({ error: 'Error al obtener los libros' });
  });

  // Test para GET /api/libros/:id
  it('Debería manejar errores en obtener un libro por su ID', async () => {
    const response = await request(app).get('/api/libros/999'); // ID que no existe
    expect(response.status).toBe(500);
    expect(response.body).toEqual({ error: 'Error al obtener el libro' });
  });

  // Test para POST /api/libros
  it('Debería manejar errores en crear un nuevo libro', async () => {
    const nuevoLibro = {
      Titulo: 'Nuevo Libro',
      Precio: 29.99,
      FechaPublicacion: '2023-01-01',
      // Agrega solo campos válidos para evitar errores de validación
    };
    const response = await request(app)
      .post('/api/libros')
      .send(nuevoLibro);
    expect(response.status).toBe(400);
    expect(response.body).toHaveProperty('error');
  });

  // Test para PUT /api/libros/:id
  it('Debería manejar errores en actualizar un libro', async () => {
    const response = await request(app)
      .put('/api/libros/8888') // ID que no existe
      .send({ Titulo: 'Título Actualizado' });
    expect(response.status).toBe(400);
  });

  // Test para DELETE /api/libros/:id
  it('Debería manejar errores en eliminar un libro', async () => {
    const response = await request(app).delete('/api/libros/a'); // ID que no existe
    expect(response.status).toBe(500);
    expect(response.body).toEqual({ error: 'Error al eliminar el libro' });
  });
});
