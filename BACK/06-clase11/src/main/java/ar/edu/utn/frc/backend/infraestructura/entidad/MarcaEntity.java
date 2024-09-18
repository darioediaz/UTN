package ar.edu.utn.frc.backend.infraestructura.entidad;

import jakarta.persistence.*;

@Entity
@Table(name = "marca")
public class MarcaEntity {
	@Id
	@GeneratedValue(strategy = GenerationType.AUTO)
	private Integer id;
	private String nombre;

	public Integer getId() {
		return id;
	}

	public String getNombre() {
		return nombre;
	}
}
