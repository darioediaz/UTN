const request = require('supertest');
const express = require('express');
const jwt = require('jsonwebtoken');
const authRouter = require('../routes/seguridad'); // Asegúrate de que esta ruta sea correcta
const auth = require('../seguridad/auth'); // Asegúrate de que esta ruta sea correcta

const app = express();

app.use(express.json());
app.use(authRouter);

describe('Endpoints de Autenticación', () => {
    let refreshToken = '';

    // Test para POST /api/login
    it('Debería autenticar a un usuario y generar tokens de acceso y refresh', async () => {
        const response = await request(app)
            .post('/api/login')
            .send({ usuario: 'admin', clave: '123' }); // Usuario y clave correctos
        expect(response.status).toBe(200);
        expect(response.body).toHaveProperty('accessToken');
        expect(response.body).toHaveProperty('refreshToken');
    });

    // Test para POST /api/logout
    it('Debería desloguear a un usuario con un refresh token válido', async () => {
        const loginResponse = await request(app)
            .post('/api/login')
            .send({ usuario: 'juan', clave: '123' }); // Usuario y clave correctos
        refreshToken = loginResponse.body.refreshToken;

        const response = await request(app)
            .post('/api/logout')
            .send({ token: refreshToken });
        expect(response.status).toBe(200);
        expect(response.body.message).toBe('Usuario deslogueado correctamente!');
    });

    // Test para POST /api/token (sin refreshToken)
    it('Debería devolver un estado 401 cuando no se proporciona refreshToken', async () => {
        const response = await request(app)
            .post('/api/token')
            .send({});
        expect(response.status).toBe(401);
    });

    // Test para POST /api/token (refreshToken inválido)
    it('Debería devolver un estado 403 cuando se proporciona un refreshToken inválido', async () => {
        const response = await request(app)
            .post('/api/token')
            .send({ refreshToken: 'token_invalido' });
        expect(response.status).toBe(403);
    });

    // Limpiar el refreshToken después de las pruebas
    afterEach(() => {
        refreshToken = '';
    });
});
