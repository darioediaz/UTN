const request = require('supertest');
const express = require('express');
const router = require('../routes/redesSociales');
const app = express();

app.use(express.json());
app.use(router);

describe('Endpoints de Redes Sociales', () => {
    // Test para GET /api/redes-sociales
    it('Debería manejar errores al obtener todas las redes sociales', async () => {
        const response = await request(app).get('/api/redes-sociales');
        expect(response.status).toBe(500);
        expect(response.body).toEqual({ error: 'Error al obtener las redes sociales' });
    });

    // Test para GET /api/redes-sociales/:id
    it('Debería manejar errores al obtener una red social por su ID', async () => {
        const response = await request(app).get('/api/redes-sociales/999'); // ID que no existe
        expect(response.status).toBe(500);
        expect(response.body).toEqual({ error: 'Error al obtener la red social' });
    });

    // Test para POST /api/redes-sociales
    it('Debería manejar errores al crear una nueva red social', async () => {
        const nuevaRedSocial = {
            Nombre: 'Nueva Red Social',
            UsuariosActivos: 1000,
            FechaCreacion: '2024-01-01'
        };
        const response = await request(app)
            .post('/api/redes-sociales')
            .send(nuevaRedSocial);
        expect(response.status).toBe(400);
        expect(response.body).toHaveProperty('error');
    });

    // Test para PUT /api/redes-sociales/:id
    it('Debería manejar errores al actualizar una red social', async () => {
        const response = await request(app)
            .put('/api/redes-sociales/8888') // ID que no existe
            .send({ Nombre: 'Nombre Actualizado' });
        expect(response.status).toBe(400);
    });

    // Test para DELETE /api/redes-sociales/:id
    it('Debería manejar errores al eliminar una red social', async () => {
        const response = await request(app).delete('/api/redes-sociales/a'); // ID que no existe
        expect(response.status).toBe(500);
        expect(response.body).toEqual({ error: 'Error al eliminar la red social' });
    });
});
