package com.bot.demo.logicabase.repositorios;

import com.bot.demo.logicabase.entidades.DireccionResponse;
import lombok.extern.slf4j.Slf4j;
import org.springframework.jdbc.core.JdbcTemplate;
import org.springframework.jdbc.core.RowMapper;
import org.springframework.stereotype.Repository;

import java.sql.ResultSet;
import java.sql.SQLException;
import java.util.List;

@Repository
@Slf4j
public class DireccionRepositorio {

    private final JdbcTemplate jdbc;

    public DireccionRepositorio(JdbcTemplate jdbc) {
        this.jdbc = jdbc;
    }

    public List<DireccionResponse> obtenerDirecciones(String identifiacion) {
        String query = "select b.descripcion tipo_direccion, a.calle, a.nomenclatura\n" +
                "  from mg_direcciones a, mg_tipo_direccion b\n" +
                " where codigo_cliente =\n" +
                "       (select codigo_cliente\n" +
                "          from mg_clientes\n" +
                "         where numero_identificacion = ?)\n" +
                "   and a.codigo_tipo_direccion = b.codigo_tipo_direccion";

        @SuppressWarnings("deprecation")
        List<DireccionResponse> resultado = jdbc.query(query,
                new Object[]{identifiacion},
                new RowMapper<DireccionResponse>() {
                    public DireccionResponse mapRow(ResultSet rs, int i)
                            throws SQLException {
                        DireccionResponse direccion = new DireccionResponse();
                        direccion.setTipoDireccion(rs.getString("tipo_direccion"));
                        direccion.setCalle(rs.getString("calle"));
                        direccion.setNomenclatura(rs.getString("nomenclatura"));
                        return direccion;
                    }
                });
        return resultado;
    }
}
