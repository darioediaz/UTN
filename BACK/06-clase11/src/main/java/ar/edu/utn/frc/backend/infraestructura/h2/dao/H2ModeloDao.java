package ar.edu.utn.frc.backend.infraestructura.h2.dao;

import ar.edu.utn.frc.backend.infraestructura.dao.ModeloDao;
import ar.edu.utn.frc.backend.infraestructura.entidad.MarcaEntity;
import ar.edu.utn.frc.backend.infraestructura.entidad.ModeloEntity;
import jakarta.persistence.EntityManager;
import jakarta.persistence.EntityManagerFactory;
import jakarta.persistence.Persistence;

import java.util.Optional;

public class H2ModeloDao implements ModeloDao {
    @Override
    public Optional<ModeloEntity> getModelo(Integer id) {
        try(EntityManagerFactory entityManagerFactory =
                    Persistence.createEntityManagerFactory("autos-db");
            EntityManager entityManager = entityManagerFactory.createEntityManager()) {

            ModeloEntity modelo = entityManager.find(ModeloEntity.class, id);

            return Optional.ofNullable(modelo);
        }
    }
}
