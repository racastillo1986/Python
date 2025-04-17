from typing import Any, Text, Dict, List
from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher
from rasa_sdk.events import SlotSet, EventType
import requests
import json

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
                    # Convertimos la lista de movimientos a JSON plano
                    texto_json = json.dumps(movimientos)
                    dispatcher.utter_message(text=f"MOVIMIENTOS_JSON: {texto_json}")
                else:
                    dispatcher.utter_message(text="No se encontraron movimientos para ese período.")
            else:
                dispatcher.utter_message(text="Ocurrió un error al consultar los movimientos.")
        except Exception as e:
            dispatcher.utter_message(text=f"No se pudo conectar al servidor. Detalles: {str(e)}")

        return []
    
class ActionConsultarDireccion(Action):
    def name(self) -> Text:
        return "action_consultar_direccion" 
    
    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[EventType]:
        
        identificacion = tracker.get_slot("identificacion")
        print(f"Identificacion a consultar: {identificacion}")
        
        if not identificacion:
            dispatcher.utter_message(text="Podrias indicarme el numero de identificacion???")
            return []
        
        url = f"http://localhost:8080/direcciones/all/{identificacion}"
        
        try:
            response = requests.get(url)
            if response.status_code == 200:
                direcciones = response.json()
                if direcciones:
                    # Convertimos la lista de direcciones a JSON plano
                    texto_json = json.dumps(direcciones)
                    dispatcher.utter_message(text=f"DIRECCIONES_JSON: {texto_json}")
                else:
                    dispatcher.utter_message(text="No se encontraron direcciones para esa identificacion.")
            else:
                dispatcher.utter_message(text="Ocurrió un error al consultar las direcciones.")
                
        except Exception as e:
            dispatcher.utter_message(text="Ocurrió un error al consultar direcciones.")
        
        return []
    
class ActionConsultarTelefono(Action):
    def name(self) -> Text:
        return "action_consultar_telefono"
    
    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[EventType]:

        identificacion = tracker.get_slot("identificacion")
        print("Identificacion", identificacion)

        if not identificacion:
            dispatcher.utter_message(text="¿Podrías indicarme el número de identificación?")
            return []

        url = f"http://localhost:8080/telefonos/{identificacion}"

        try:
            response = requests.get(url)
            if response.status_code == 200:
                telefonos = response.json()
                if telefonos:
                    # Convertimos la lista de teléfonos a JSON plano
                    texto_json = json.dumps(telefonos)
                    dispatcher.utter_message(text=f"TELEFONOS_JSON: {texto_json}")
                else:
                    dispatcher.utter_message(text="No se encontraron teléfonos para esa identificación.")
            else:
                dispatcher.utter_message(text="Ocurrió un error al consultar los teléfonos.")

        except Exception as e:
            print("Error en action_consultar_telefono:", e)
            dispatcher.utter_message(text="Ocurrió un error al consultar teléfonos.")

        return []