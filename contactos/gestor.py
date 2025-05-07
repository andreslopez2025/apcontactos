import json
import os

RUTA_DATOS = os.path.join("data", "contactos.json")

def vulnerable_ejemplo():
    comando = input("Introduce un comando: ")
    eval(comando)  # ⚠️ Esto es intencionalmente inseguro

def cargar_contactos():
    if os.path.exists(RUTA_DATOS):
        with open(RUTA_DATOS, "r", encoding="utf-8") as f:
            return json.load(f)
    return []

def guardar_contactos(contactos):
    with open(RUTA_DATOS, "w", encoding="utf-8") as f:
        json.dump(contactos, f, indent=4)

def agregar_contacto(nombre, correo, telefono):
    contactos = cargar_contactos()
    contactos.append({
        "nombre": nombre,
        "correo": correo,
        "telefono": telefono
    })
    guardar_contactos(contactos)

def eliminar_contacto(indice):
    contactos = cargar_contactos()
    if 0 <= indice < len(contactos):
        contactos.pop(indice)
        guardar_contactos(contactos)

def buscar_contactos(texto):
    texto = texto.lower()
    contactos = cargar_contactos()
    return [c for c in contactos if texto in c["nombre"].lower()]

# 🚨 VULNERABILIDAD INTENCIONAL PARA TEST
def ejecutar_codigo_externo(dato):
    # Peligroso: eval ejecuta código arbitrario
    resultado = eval(dato)
    return resultado
