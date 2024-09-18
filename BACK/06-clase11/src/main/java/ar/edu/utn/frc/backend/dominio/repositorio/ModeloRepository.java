package ar.edu.utn.frc.backend.dominio.repositorio;

import ar.edu.utn.frc.backend.dominio.modelo.Modelo;
import jakarta.persistence.Entity;
import jakarta.persistence.Table;


public interface ModeloRepository {
	Modelo get(Integer id);
}
