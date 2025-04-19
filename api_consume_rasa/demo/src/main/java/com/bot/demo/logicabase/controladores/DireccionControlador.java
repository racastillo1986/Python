package com.bot.demo.logicabase.controladores;

import com.bot.demo.logicabase.entidades.DireccionResponse;
import com.bot.demo.logicabase.servicios.DireccionServicio;
import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.PathVariable;
import org.springframework.web.bind.annotation.RequestMapping;
import org.springframework.web.bind.annotation.RestController;

import java.util.List;

@RestController
@RequestMapping("/direcciones")
public class DireccionControlador {

    private final DireccionServicio direccionServicio;

    public DireccionControlador(DireccionServicio direccionServicio){
        this.direccionServicio = direccionServicio;
    }

    @GetMapping("/all/{identificacion}")
    public List<DireccionResponse> getDirecciones(@PathVariable String identificacion){
        return  direccionServicio.obtenerDirecciones(identificacion);
    }
}
