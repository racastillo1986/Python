package com.bot.demo.asistente.entidades;

import com.fasterxml.jackson.annotation.JsonProperty;
import lombok.Data;

@Data
public class RasaResponse {
    @JsonProperty("recipient_id")
    private String recipientId;
    private String text;
}
