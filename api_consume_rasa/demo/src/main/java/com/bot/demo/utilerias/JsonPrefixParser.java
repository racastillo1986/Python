package com.bot.demo.utilerias;

import com.bot.demo.logicabase.entidades.CuentaMovimiento;
import com.bot.demo.logicabase.entidades.DireccionResponse;
import com.bot.demo.logicabase.entidades.TelefonoResponse;
import com.fasterxml.jackson.databind.ObjectMapper;
import com.fasterxml.jackson.databind.type.CollectionType;
import lombok.extern.slf4j.Slf4j;

import java.util.HashMap;
import java.util.List;
import java.util.Map;
import java.util.function.Function;

@Slf4j
public class JsonPrefixParser {
    private static final ObjectMapper mapper = new ObjectMapper();

    // Mapa que relaciona prefijos con las clases destino
    private static final Map<String, Function<String, String>> prefixParsers = new HashMap<>();

    static {
        register("TELEFONOS_JSON:", TelefonoResponse.class);
        register("DIRECCIONES_JSON:", DireccionResponse.class);
        register("MOVIMIENTOS_JSON:", CuentaMovimiento.class);
    }

    private static <T> void register(String prefix, Class<T> clazz) {
        prefixParsers.put(prefix, json -> {
            try {
                CollectionType listType = mapper.getTypeFactory().constructCollectionType(List.class, clazz);
                List<T> dataList = mapper.readValue(json, listType);
                return JsonUtils.toJsonString(dataList);
            } catch (Exception e) {
                log.error("❌ Error al parsear " + prefix + ": " + json, e);
                return "❌ Error procesando la información para " + prefix;
            }
        });
    }

    public static String parse(String prefixedText) {
        for (Map.Entry<String, Function<String, String>> entry : prefixParsers.entrySet()) {
            if (prefixedText.startsWith(entry.getKey())) {
                String json = prefixedText.substring(entry.getKey().length()).trim();
                return entry.getValue().apply(json);
            }
        }
        // Si no tiene prefijo conocido, devolver el texto original
        return prefixedText;
    }
}
