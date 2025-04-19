package com.bot.demo.logicabase.servicios;

import com.bot.demo.logicabase.entidades.DireccionResponse;
import com.bot.demo.logicabase.repositorios.DireccionRepositorio;
import lombok.extern.slf4j.Slf4j;
import org.springframework.stereotype.Service;

import java.util.List;

@Service
@Slf4j
public class DireccionServicio {

    private final DireccionRepositorio direccionRepositorio;

    public DireccionServicio(DireccionRepositorio direccionRepositorio){
        this.direccionRepositorio = direccionRepositorio;
    }

    public List<DireccionResponse> obtenerDirecciones(String identificacion){
        return direccionRepositorio.obtenerDirecciones(identificacion);
    }
}
