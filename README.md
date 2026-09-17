# Agente LangGraph con Gemini
## Requisitos

* Python 3.12 o superior
* API Key de Google Gemini

## Instalacion
Instalar las dependencias:

```bash
pip install -r requirements.txt
```

## Configuración

Crear un archivo `.env` en la raíz del proyecto:

```env
GOOGLE_API_KEY=tu_api_key
```

## Ejecución

Ejecutar:

```bash
python main.py
```

El programa realiza tres pruebas:

1. Consulta los pedidos de un cliente utilizando múltiples herramientas.
2. Realiza una segunda consulta utilizando el mismo `thread_id` para comprobar la persistencia de la conversación.
3. Consulta un cliente inexistente para comprobar el manejo de errores.

También genera `traza_ejecucion.json` con la traza de ejecución del agente.

## Estructura

* `main.py`: ejecución de las pruebas y persistencia con SQLite.
* `graph.py`: StateGraph, nodos y ciclo ReAct.
* `tools.py`: herramientas de consulta.
* `database.py`: datos simulados de clientes y pedidos.
* `config.py`: configuración de Gemini.
* `utils.py`: procesamiento y serialización de mensajes.
