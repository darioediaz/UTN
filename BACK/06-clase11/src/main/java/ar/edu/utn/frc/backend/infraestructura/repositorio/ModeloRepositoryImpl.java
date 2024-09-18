package ar.edu.utn.frc.backend.infraestructura.repositorio;

import ar.edu.utn.frc.backend.dominio.modelo.Marca;
import ar.edu.utn.frc.backend.dominio.modelo.Modelo;
import ar.edu.utn.frc.backend.dominio.repositorio.MarcaRepository;
import ar.edu.utn.frc.backend.dominio.repositorio.ModeloRepository;
import ar.edu.utn.frc.backend.infraestructura.dao.ModeloDao;

import java.util.Collections;
import java.util.List;

public class ModeloRepositoryImpl implements ModeloRepository {
    ModeloDao modeloDao;
    MarcaRepository marcaRepository;

    public ModeloRepositoryImpl(ModeloDao modeloDao) {
        this.modeloDao = modeloDao;
    }

    @Override
    public Modelo get(Integer id) {
        return modeloDao.getModelo(id)
                .map((entity)->
                        new Modelo(entity.getId(),
                        entity.getNombre(),
                        entity.getAnio(),
                        null,
                        Collections.emptyList()))
                .orElseThrow();
    }
}
