package com.bot.demo.asistente.servicios;

import com.bot.demo.asistente.entidades.MessageRequest;
import com.bot.demo.asistente.entidades.RasaResponse;
import com.bot.demo.utilerias.JsonPrefixParser;
import com.bot.demo.utilerias.JsonUtils;
import com.fasterxml.jackson.core.JsonProcessingException;
import lombok.extern.slf4j.Slf4j;
import org.springframework.http.*;
import org.springframework.stereotype.Service;
import org.springframework.web.client.RestTemplate;

@Service
@Slf4j
public class AsistenteServicio {

    public RasaResponse[] enviarMensajeRasa(String sender, String mensaje) throws JsonProcessingException {
        log.info("2");
        RestTemplate restTemplate = new RestTemplate();

        String url = "http://localhost:5005/webhooks/rest/webhook";

        MessageRequest request = new MessageRequest();
        request.setSender(sender);
        request.setMessage(mensaje);

        HttpHeaders headers = new HttpHeaders();
        headers.setContentType(MediaType.APPLICATION_JSON);

        HttpEntity<MessageRequest> entity = new HttpEntity<>(request, headers);

        ResponseEntity<RasaResponse[]> response = restTemplate.exchange(
                url,
                HttpMethod.POST,
                entity,
                RasaResponse[].class
        );
        RasaResponse[] respuestas = response.getBody();
        if (respuestas != null) {
            for (RasaResponse r : respuestas) {
                if (r.getText() != null) {
                    String nuevoTexto = JsonPrefixParser.parse(r.getText());
                    r.setText(nuevoTexto);
                }
            }
        }
        JsonUtils.printJson(respuestas);
        return respuestas;
    }
}