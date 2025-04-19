package com.bot.demo.logicabase.repositorios;

import com.bot.demo.logicabase.entidades.DireccionResponse;
import com.bot.demo.logicabase.entidades.TelefonoResponse;
import lombok.extern.slf4j.Slf4j;
import org.springframework.jdbc.core.JdbcTemplate;
import org.springframework.jdbc.core.RowMapper;
import org.springframework.stereotype.Repository;

import java.sql.ResultSet;
import java.sql.SQLException;
import java.util.List;

@Repository
@Slf4j
public class TelefonoRepositorio {

    private final JdbcTemplate jdbc;

    public TelefonoRepositorio(JdbcTemplate jdbc) {
        this.jdbc = jdbc;
    }

    public List<TelefonoResponse> obtenerTelefonos(String identifiacion) {
        String query = "select a.numero, b.descripcion tipo, c.descripcion operadora\n" +
                "  from MG_TELEFONOS_X_CLTE       a,\n" +
                "       mg_tipo_telefono          b,\n" +
                "       mg_operadoras_telefonicas c\n" +
                " where codigo_cliente =\n" +
                "       (select codigo_cliente\n" +
                "          from mg_clientes\n" +
                "         where numero_identificacion = ?)\n" +
                "   and a.tipo_telefono = b.codigo_tipo_telefono\n" +
                "   and a.operadora = c.codigo_tipo_operadora";

        @SuppressWarnings("deprecation")
        List<TelefonoResponse> resultado = jdbc.query(query,
                new Object[]{identifiacion},
                new RowMapper<TelefonoResponse>() {
                    public TelefonoResponse mapRow(ResultSet rs, int i)
                            throws SQLException {
                        TelefonoResponse telefono = new TelefonoResponse();
                        telefono.setNumero(rs.getString("numero"));
                        telefono.setTipo(rs.getString("tipo"));
                        telefono.setOperadora(rs.getString("operadora"));
                        return telefono;
                    }
                });
        return resultado;
    }
}
