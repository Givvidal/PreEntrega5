from database import CLIENTES_DB,PEDIDOS_DB
from langchain_core.tools import tool

@tool
def buscar_cliente_nombre(nombre: str) -> str:
    """Busca el ID (cliente_id) de un cliente a partir de su nombre completa.
    Usar esta herramienta SIEMPRE que el usuario mencione un cliente por su nombre
    y necesites averiguar su cliente_id antes de poder consultar sus pedidos.
    Devuelve un mensaje de ERROR si el nombre no coincide exactamente con ningun 
    cliente registrado."""
    clave = nombre.strip().lower()
    if clave not in CLIENTES_DB:
        return f"ERROR: no se encontro  ningun cliente con el nombre '{nombre}'. Verifica que el nombre este completo"
    return f"Cliente encontrado:'{nombre}' -> cliente_id ={CLIENTES_DB[clave]}"

@tool
def buscar_pedidos(cliente_id: int) -> str:
    """Busca la cantidad de pedidos y el monto total gastado por un cliente,
    dado su cliente_id NUMERICO (no su nombre - si solo tenes el nombre, primero
    usa buscar_cliente_nombre para obtener el ID).
    Devuelve un mensaje de ERROR si el cliente_id no existe en la base de datos."""
    if cliente_id not in PEDIDOS_DB:
        return f"ERROR: no existe ningun cliente con id = '{cliente_id}'."
    datos = PEDIDOS_DB[cliente_id]
    return f"pedidos:{datos['pedidos']}, total=${datos['total']}"

herramientas = [buscar_cliente_nombre,buscar_pedidos]
