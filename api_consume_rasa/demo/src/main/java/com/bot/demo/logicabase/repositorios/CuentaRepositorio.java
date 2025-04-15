package com.bot.demo.logicabase.repositorios;

import com.bot.demo.logicabase.entidades.CuentaMovimiento;
import lombok.extern.slf4j.Slf4j;
import org.springframework.jdbc.core.JdbcTemplate;
import org.springframework.jdbc.core.RowMapper;
import org.springframework.stereotype.Repository;

import java.sql.ResultSet;
import java.sql.SQLException;
import java.util.List;

@Repository
@Slf4j
public class CuentaRepositorio {

    private final JdbcTemplate jdbc;

    public CuentaRepositorio(JdbcTemplate jdbc) {
        this.jdbc = jdbc;
    }

    public Float saldoDisponible(String numeroCuenta) {
        log.info("5");
        String query = "select a.saldo_total_en_linea -\n" +
                "       (a.saldo_reserva_en_linea + a.saldo_pignorado_en_linea +\n" +
                "       a.saldo_embargado_en_linea) saldo_disponible\n" +
                "  from ca_cuentas_de_ahorro a\n" +
                " where a.numero_cuenta = ?";

        return jdbc.queryForObject(query, Float.class, numeroCuenta);
    }

    public List<CuentaMovimiento> obtenerMovimientos(String numeroCuenta, String fechaDesde, String fechaHasta) {
        log.info("5");
        String query = "SELECT *\n" +
                "  FROM (SELECT a.hora        fecha_hora,\n" +
                "               b.descripcion transaccion,\n" +
                "               a.descripcion,\n" +
                "               a.valor\n" +
                "          FROM ca_movimientos_mensuales a, mg_tipos_de_transacciones b\n" +
                "         WHERE a.numero_cuenta = ?\n" +
                "           AND a.fecha_valida BETWEEN TO_DATE(?, 'DD-MM-YYYY') AND TO_DATE(?, 'DD-MM-YYYY')\n" +
                "           AND a.codigo_tipo_transaccion = b.codigo_tipo_transaccion\n" +
                "         ORDER BY a.hora DESC)\n" +
                " WHERE ROWNUM <= 20";

        @SuppressWarnings("deprecation")
        List<CuentaMovimiento> resultado = jdbc.query(query,
                new Object[]{numeroCuenta, fechaDesde, fechaHasta},
                new RowMapper<CuentaMovimiento>() {
                    public CuentaMovimiento mapRow(ResultSet rs, int i)
                            throws SQLException {
                        CuentaMovimiento ctaMovimiento = new CuentaMovimiento();
                        ctaMovimiento.setFechaHora(rs.getDate("fecha_hora"));
                        ctaMovimiento.setTransaccion(rs.getString("transaccion"));
                        ctaMovimiento.setDescripcion(rs.getString("descripcion"));
                        ctaMovimiento.setValor(rs.getFloat("valor"));
                        return ctaMovimiento;
                    }
                });
        return resultado;
    }
}
