package ar.edu.utn.frc.backend;

import static org.junit.jupiter.api.Assertions.assertEquals;

import ar.edu.utn.frc.backend.infraestructura.dao.MarcaDao;
import ar.edu.utn.frc.backend.infraestructura.h2.dao.H2MarcaDao;
import ar.edu.utn.frc.backend.infraestructura.repositorio.MarcaRepositoryImpl;
import org.junit.jupiter.api.Test;

import ar.edu.utn.frc.backend.dominio.modelo.Marca;
import ar.edu.utn.frc.backend.dominio.repositorio.MarcaRepository;

public class MarcaTest {
	private final MarcaRepository marcaRepository = new MarcaRepositoryImpl(new H2MarcaDao());

	@Test
	public void obtieneLaCantidadMarcasCorrectamente() {
		assertEquals(9, marcaRepository.getAll().size());
	}

	@Test
	public void laMarcaAudiEsCorrecta() {
		final Marca marcaEsperada = new Marca(6, "Audi");
		final Marca marca = marcaRepository
			.getAll()
			.stream()
			.filter(tipo -> tipo.getNombre().equalsIgnoreCase("Audi"))
			.findFirst()
			.orElseThrow();
		assertEquals(marcaEsperada, marca);
	}
}
