package ar.edu.utn.frc.backend.infraestructura.entidad;

import jakarta.persistence.Column;
import jakarta.persistence.Entity;
import jakarta.persistence.Table;

@Entity
@Table(name = "modelo")
public class ModeloEntity {
	private Integer id;
	private String nombre;
	private Integer anio;
	@Column(name= "ID_MARCA")
	private Integer marcaId;

	public Integer getId() {
		return id;
	}

	public String getNombre() {
		return nombre;
	}
	public Integer getAnio() {
		return anio;
	}

	public Integer getMarcaId() {
		return marcaId;
	}
}
