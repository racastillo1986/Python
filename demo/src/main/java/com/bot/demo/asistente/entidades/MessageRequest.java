package com.bot.demo.asistente.entidades;

import lombok.Data;

@Data
public class MessageRequest {
    private String sender;
    private String message;
}
