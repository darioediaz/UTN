package ar.edu.utn.frc.backend.infraestructura.repositorio;

import ar.edu.utn.frc.backend.dominio.modelo.Marca;
import ar.edu.utn.frc.backend.dominio.repositorio.MarcaRepository;
import ar.edu.utn.frc.backend.infraestructura.dao.MarcaDao;

import java.util.List;

public class MarcaRepositoryImpl implements MarcaRepository {
    MarcaDao marcaDao;

    public MarcaRepositoryImpl(MarcaDao marcaDao) {
        this.marcaDao = marcaDao;
    }

    @Override
    public List<Marca> getAll() {
        return marcaDao.findAll()
                        .stream()
                        .map((entity)-> new Marca(entity.getId(), entity.getNombre()))
                        .toList();
    }
}
