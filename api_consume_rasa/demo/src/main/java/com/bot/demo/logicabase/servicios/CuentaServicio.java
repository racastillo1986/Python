package com.bot.demo.logicabase.servicios;

import com.bot.demo.logicabase.entidades.CuentaMovimiento;
import com.bot.demo.logicabase.repositorios.CuentaRepositorio;
import lombok.extern.slf4j.Slf4j;
import org.springframework.stereotype.Service;

import java.util.List;

@Service
@Slf4j
public class CuentaServicio {

    private final CuentaRepositorio cuentaRepositorio;

    public CuentaServicio(CuentaRepositorio cuentaRepositorio) {
        this.cuentaRepositorio = cuentaRepositorio;
    }

    public Float saldoDisponible(String numeroCuenta) {
        log.info("4");
        return cuentaRepositorio.saldoDisponible(numeroCuenta);
    }

    public List<CuentaMovimiento> movimientos(String numeroCuenta, String fechaDesde, String fechaHasta) {
        log.info("4");
        return cuentaRepositorio.obtenerMovimientos(numeroCuenta, fechaDesde, fechaHasta);
    }
}
