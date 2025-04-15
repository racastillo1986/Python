package com.bot.demo.logicabase.entidades;

import lombok.Data;

@Data
public class CuentaRequest {
    private String numeroCuenta;
    private String fechaDesde;
    private String fechaHasta;
}
