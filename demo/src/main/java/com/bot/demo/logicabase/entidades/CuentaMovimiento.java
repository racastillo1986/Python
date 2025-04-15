package com.bot.demo.logicabase.entidades;

import lombok.Data;

import java.util.Date;

@Data
public class CuentaMovimiento {
    private Date fechaHora;
    private String transaccion;
    private String descripcion;
    private Float valor;
}
