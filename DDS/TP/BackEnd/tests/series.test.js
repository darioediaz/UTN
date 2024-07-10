const request = require('supertest');
const express = require('express');
const router = require('../routes/series');
const app = express();

app.use(express.json());
app.use(router);

describe('Endpoints de Series', () => {
    // Test para GET /api/series
    it('Debería manejar errores al obtener todas las series', async () => {
        const response = await request(app).get('/api/series');
        expect(response.status).toBe(500);
        expect(response.body).toEqual({ error: 'Error al obtener las series' });
    });

    // Test para GET /api/series/:id
    it('Debería manejar errores al obtener una serie por su ID', async () => {
        const response = await request(app).get('/api/series/999'); // ID que no existe
        expect(response.status).toBe(500);
        expect(response.body).toEqual({ error: 'Error al obtener la serie' });
    });

    // Test para POST /api/series
    it('Debería manejar errores al crear una nueva serie', async () => {
        const nuevaSerie = {
            Titulo: 'Nueva Serie',
            NumTemporadas: 5,
            FechaEstreno: '2024-01-01'
        };
        const response = await request(app)
            .post('/api/series')
            .send(nuevaSerie);
        expect(response.status).toBe(400);
        expect(response.body).toHaveProperty('error');
    });

    // Test para PUT /api/series/:id
    it('Debería manejar errores al actualizar una serie', async () => {
        const response = await request(app)
            .put('/api/series/8888') // ID que no existe
            .send({ Titulo: 'Nuevo Título' });
        expect(response.status).toBe(400);
    });

    // Test para DELETE /api/series/:id
    it('Debería manejar errores al eliminar una serie', async () => {
        const response = await request(app).delete('/api/series/abc'); // ID que no existe
        expect(response.status).toBe(500);
        expect(response.body).toEqual({ error: 'Error al eliminar la serie' });
    });
});
