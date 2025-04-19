package com.bot.demo.logicabase.servicios;

import com.bot.demo.logicabase.entidades.DireccionResponse;
import com.bot.demo.logicabase.entidades.TelefonoResponse;
import com.bot.demo.logicabase.repositorios.DireccionRepositorio;
import com.bot.demo.logicabase.repositorios.TelefonoRepositorio;
import lombok.extern.slf4j.Slf4j;
import org.springframework.stereotype.Service;

import java.util.List;

@Service
@Slf4j
public class TelefonoServicio {
    private final TelefonoRepositorio telefonoRepositorio;

    public TelefonoServicio(TelefonoRepositorio telefonoRepositorio){
        this.telefonoRepositorio = telefonoRepositorio;
    }

    public List<TelefonoResponse> obtenerTelefonos(String identificacion){
        return telefonoRepositorio.obtenerTelefonos(identificacion);
    }
}
