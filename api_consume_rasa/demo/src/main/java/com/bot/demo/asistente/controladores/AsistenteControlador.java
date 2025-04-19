package com.bot.demo.asistente.controladores;

import com.bot.demo.asistente.entidades.MessageRequest;
import com.bot.demo.asistente.entidades.RasaResponse;
import com.bot.demo.asistente.servicios.AsistenteServicio;
import com.fasterxml.jackson.core.JsonProcessingException;
import lombok.extern.slf4j.Slf4j;
import org.springframework.web.bind.annotation.*;

@RestController
@RequestMapping("/asistente")
@CrossOrigin("*")
@Slf4j
public class AsistenteControlador {

    private final AsistenteServicio asistenteServicio;

    public AsistenteControlador(AsistenteServicio asistenteServicio){
        this.asistenteServicio = asistenteServicio;
    }

    @PostMapping("/mensaje")
    public RasaResponse[] enviarMensaje(@RequestBody MessageRequest request) throws JsonProcessingException {
        log.info("1");
        return asistenteServicio.enviarMensajeRasa(request.getSender(), request.getMessage());
    }
}