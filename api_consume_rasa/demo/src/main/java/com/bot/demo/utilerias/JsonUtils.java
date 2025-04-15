package com.bot.demo.utilerias;

import com.fasterxml.jackson.databind.ObjectMapper;
import com.fasterxml.jackson.databind.SerializationFeature;

public class JsonUtils {

    // Imprime cualquier objeto como JSON indentado (bonito) en consola
    public static void printJson(Object obj) {
        try {
            ObjectMapper mapper = new ObjectMapper();
            mapper.enable(SerializationFeature.INDENT_OUTPUT); // Activa indentado
            String json = mapper.writeValueAsString(obj);
            System.out.println("🧾 Objeto como JSON:\n" + json);
        } catch (Exception e) {
            System.out.println("❌ Error convirtiendo a JSON: " + e.getMessage());
        }
    }

    // Devuelve el JSON en forma de String por si lo quieres usar en otro lado
    public static String toJsonString(Object obj) {
        try {
            ObjectMapper mapper = new ObjectMapper();
            mapper.enable(SerializationFeature.INDENT_OUTPUT);
            return mapper.writeValueAsString(obj);
        } catch (Exception e) {
            return "❌ Error convirtiendo a JSON: " + e.getMessage();
        }
    }
}
