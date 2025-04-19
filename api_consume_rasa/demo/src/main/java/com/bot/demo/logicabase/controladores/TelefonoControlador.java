package com.bot.demo.logicabase.controladores;

import com.bot.demo.logicabase.entidades.DireccionResponse;
import com.bot.demo.logicabase.entidades.TelefonoResponse;
import com.bot.demo.logicabase.servicios.DireccionServicio;
import com.bot.demo.logicabase.servicios.TelefonoServicio;
import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.PathVariable;
import org.springframework.web.bind.annotation.RequestMapping;
import org.springframework.web.bind.annotation.RestController;

import java.util.List;

@RestController
@RequestMapping("/telefonos")
public class TelefonoControlador {

    private final TelefonoServicio telefonoServicio;

    public TelefonoControlador(TelefonoServicio telefonoServicio){
        this.telefonoServicio = telefonoServicio;
    }

    @GetMapping("/{identificacion}")
    public List<TelefonoResponse> getTelefonos(@PathVariable String identificacion){
        return  telefonoServicio.obtenerTelefonos(identificacion);
    }
}
