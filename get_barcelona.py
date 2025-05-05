import urllib.request
import json

def obtener_datos_clima(latitud, longitud):
    url = f"https://api.open-meteo.com/v1/forecast?latitude={latitud}&longitude={longitud}&current=temperature_2m,relative_humidity_2m,wind_speed_10m&hourly=temperature_2m,relative_humidity_2m,wind_speed_10m"

    with urllib.request.urlopen(url) as respuesta:
        datos = json.load(respuesta)

        # Extraer los datos actuales
        temperatura = datos["current"]["temperature_2m"]
        velocidad_viento = datos["current"]["wind_speed_10m"]

        # Tomar la humedad relativa de la primera hora disponible
        humedad = datos["hourly"]["relative_humidity_2m"][0]

        return temperatura, velocidad_viento, humedad

# Diccionario de ciudades con sus coordenadas (latitud, longitud)
ciudades = {
    1: {"nombre": "Barcelona", "latitud": 41.38879, "longitud": 2.15899},
    2: {"nombre": "Madrid", "latitud": 40.4168, "longitud": -3.7038},
    3: {"nombre": "Reus", "latitud": 41.1500, "longitud": 1.1167}
}

# Mostrar el menú de opciones
print("\n=== INFORMACIÓN DEL CLIMA ===")
print("Seleccione una ciudad:")
print("1. Barcelona, España")
print("2. Madrid, España")
print("3. Reus, España")

# Pedir al usuario que elija una opción
opcion = int(input("\nElija una opción (1-3): "))

# Procesar la opción seleccionada
ciudad = ciudades[opcion]
print(f"\nObteniendo datos para {ciudad['nombre']}...")

# Obtener los datos climáticos
temperatura, velocidad_viento, humedad = obtener_datos_clima(
    ciudad["latitud"],
    ciudad["longitud"]
)

# Mostrar los resultados
print(f"\nDatos climáticos para {ciudad['nombre']}:")
print(f"Temperatura actual: {temperatura} °C")
print(f"Velocidad del viento: {velocidad_viento} km/h")
print(f"Humedad relativa: {humedad}%")
