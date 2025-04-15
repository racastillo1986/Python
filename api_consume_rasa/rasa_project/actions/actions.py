from typing import Any, Text, Dict, List
from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher
from rasa_sdk.events import SlotSet, EventType
import requests

class ActionConsultarSaldo(Action):
    def name(self) -> Text:
        return "action_consultar_saldo"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        numero_cuenta = tracker.get_slot("numero_cuenta")

        if not numero_cuenta:
            dispatcher.utter_message(text="No encontré el número de cuenta.")
            return []

        try:
            response = requests.get(f"http://localhost:8080/cuenta/saldo/{numero_cuenta}")
            if response.status_code == 200:
                saldo = response.text
                dispatcher.utter_message(text=f"El saldo de la cuenta {numero_cuenta} es ${saldo}")
            else:
                dispatcher.utter_message(text="No pude obtener el saldo. Verifica si el número de cuenta es correcto.")
        except Exception as e:
            dispatcher.utter_message(text="Ocurrió un error al consultar el saldo.")

        return []

class ActionConsultarMovimientos(Action):
    def name(self) -> Text:
        return "action_consultar_movimientos"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[EventType]:

        numero_cuenta = tracker.get_slot("numero_cuenta")
        fecha_desde = tracker.get_slot("fechaDesde")
        fecha_hasta = tracker.get_slot("fechaHasta")
        
        print("🔍 Slots recibidos desde Rasa:")
        print("Número de cuenta:", numero_cuenta)
        print("Fecha desde:", fecha_desde)
        print("Fecha hasta:", fecha_hasta)

        if not numero_cuenta:
            dispatcher.utter_message(text="¿Podrías indicarme el número de tu cuenta?")
            return []
        if not fecha_desde:
            dispatcher.utter_message(text="¿Desde qué fecha deseas ver los movimientos?")
            return []
        if not fecha_hasta:
            dispatcher.utter_message(text="¿Hasta qué fecha deseas ver los movimientos?")
            return []

        url = "http://localhost:8080/cuenta/movimientos"

        payload = {
            "numeroCuenta": numero_cuenta,
            "fechaDesde": fecha_desde,
            "fechaHasta": fecha_hasta
        }

        try:
            response = requests.post(url, json=payload)
            if response.status_code == 200:
                movimientos = response.json()
                if movimientos:
                    mensaje = "Aquí tienes los últimos movimientos:\n"
                    for m in movimientos:
                        mensaje += f"- {m['fechaHora']} | {m['descripcion']} | ${m['valor']}\n"
                    dispatcher.utter_message(text=mensaje)
                else:
                    dispatcher.utter_message(text="No se encontraron movimientos para ese período.")
            else:
                dispatcher.utter_message(text="Ocurrió un error al consultar los movimientos.")
        except Exception as e:
            dispatcher.utter_message(text=f"No se pudo conectar al servidor. Detalles: {str(e)}")

        return []
