package com.bot.demo.logicabase.controladores;

import com.bot.demo.logicabase.entidades.CuentaMovimiento;
import com.bot.demo.logicabase.entidades.CuentaRequest;
import com.bot.demo.logicabase.servicios.CuentaServicio;
import lombok.extern.slf4j.Slf4j;
import org.springframework.web.bind.annotation.*;

import java.util.List;

@RestController
@RequestMapping("/cuenta")
@Slf4j
public class CuentaControlador {

    private final CuentaServicio cuentaServicio;

    public CuentaControlador(CuentaServicio cuentaServicio) {
        this.cuentaServicio = cuentaServicio;
    }

    @GetMapping("/saldo/{numeroCuenta}")
    public Float getSaldo(@PathVariable String numeroCuenta){
        log.info("Consultando saldo de cuenta: {}", numeroCuenta);
        log.info("3");
        return cuentaServicio.saldoDisponible(numeroCuenta);
    }

    @PostMapping("/movimientos")
    public List<CuentaMovimiento> getMovimientos(@RequestBody CuentaRequest request){
        log.info("EndPoint Movimientos");
        log.info("3");
        return cuentaServicio.movimientos(request.getNumeroCuenta(), request.getFechaDesde(), request.getFechaHasta());
    }
}
