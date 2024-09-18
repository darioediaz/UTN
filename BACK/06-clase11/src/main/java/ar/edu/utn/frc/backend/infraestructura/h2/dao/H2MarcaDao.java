package ar.edu.utn.frc.backend.infraestructura.h2.dao;

import java.util.Collections;
import java.util.List;
import java.util.Optional;


import ar.edu.utn.frc.backend.infraestructura.dao.MarcaDao;
import ar.edu.utn.frc.backend.infraestructura.entidad.MarcaEntity;
import jakarta.persistence.EntityManager;
import jakarta.persistence.EntityManagerFactory;
import jakarta.persistence.Persistence;

public final class H2MarcaDao implements MarcaDao {

	@Override
	public Optional<MarcaEntity> getMarca(Integer id) {
		try(EntityManagerFactory entityManagerFactory =
					Persistence.createEntityManagerFactory("autos-db");
			EntityManager entityManager = entityManagerFactory.createEntityManager()) {

			MarcaEntity marca = entityManager.find(MarcaEntity.class, id);

			return Optional.ofNullable(marca);
		}
	}

	@Override public List<MarcaEntity> findAll() {
		try(EntityManagerFactory entityManagerFactory =
					Persistence.createEntityManagerFactory("autos-db");
			EntityManager entityManager = entityManagerFactory.createEntityManager()) {

		return entityManager.createQuery("SELECT m from MarcaEntity m",
				MarcaEntity.class).getResultList();
		}

	}
}
