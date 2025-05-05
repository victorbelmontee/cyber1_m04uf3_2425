# cyber1_m04uf3_2425

# Explicación detallada del código

El código que he escrito es un programa en Python que permite consultar información meteorológica en tiempo real para tres ciudades españolas: Barcelona, Madrid y Reus.

## 1. Importación de bibliotecas

```python
import urllib.request
import json
```

- `urllib.request`: Esta biblioteca se utiliza para realizar peticiones HTTP, lo que nos permite conectarnos a APIs web. En este caso, la usamos para acceder a la API de Open-Meteo.
- `json`: Esta biblioteca nos permite manejar datos en formato JSON, que es el formato en el que la API de Open-Meteo devuelve sus datos.

## 2. Función para obtener datos climáticos

```python
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
```

- **Definición de función**: `obtener_datos_clima` es una función que acepta dos parámetros: `latitud` y `longitud`, que son las coordenadas geográficas de la ciudad para la que queremos obtener los datos meteorológicos.

- **f-strings**: He utilizado f-strings para construir la URL de la API. Los f-strings permiten insertar variables directamente en una cadena de texto usando la sintaxis `{variable}`. Esto hace que el código sea más legible y menos propenso a errores. La URL incluye parámetros para:
  - Las coordenadas geográficas (`latitude` y `longitude`)
  - Los datos actuales que queremos obtener (`temperature_2m` y `wind_speed_10m`)
  - Los datos horarios (`temperature_2m`, `relative_humidity_2m` y `wind_speed_10m`)

- **Contexto `with`**: El bloque `with urllib.request.urlopen(url) as respuesta:` asegura que los recursos se liberen correctamente después de usarlos, incluso si ocurre un error.
  
- **Procesamiento de JSON**: `json.load(respuesta)` convierte la respuesta JSON de la API en un diccionario de Python que podemos manipular fácilmente.

- **Extracción de datos**: He extraído tres valores específicos del diccionario:
  - La temperatura actual (`temperatura = datos["current"]["temperature_2m"]`)
  - La velocidad del viento actual (`velocidad_viento = datos["current"]["wind_speed_10m"]`)
  - La humedad relativa de la primera hora disponible (`humedad = datos["hourly"]["relative_humidity_2m"][0]`). Aquí uso el índice `[0]` para obtener el primer valor del array.

- **Retorno de valores**: La función devuelve tres valores (temperatura, velocidad del viento y humedad) que luego se pueden desempaquetar.

## 3. Diccionario de ciudades

```python
ciudades = {
    1: {"nombre": "Barcelona", "latitud": 41.38879, "longitud": 2.15899},
    2: {"nombre": "Madrid", "latitud": 40.4168, "longitud": -3.7038},
    3: {"nombre": "Reus", "latitud": 41.1500, "longitud": 1.1167}
}
```

- **Estructura de datos**: He utilizado un diccionario donde las claves son los números de opción (1, 2, 3) y los valores son diccionarios con la información de cada ciudad:
  - `nombre`: El nombre de la ciudad
  - `latitud`: La coordenada de latitud de la ciudad
  - `longitud`: La coordenada de longitud de la ciudad

## 4. Menú de opciones

```python
print("\n=== INFORMACIÓN DEL CLIMA ===")
print("Seleccione una ciudad:")
print("1. Barcelona, España")
print("2. Madrid, España")
print("3. Reus, España")
```

- **Interfaz de usuario**: He mostrado un menú para que el usuario sepa qué opciones tiene disponibles.
- El `\n` al principio crea una salto de línea antes del título para mejorar la legibilidad.

## 5. Entrada del usuario

```python
opcion = int(input("\nElija una opción (1-3): "))
```

- **Función `input()`**: Recoge la entrada del usuario como texto.
- **Conversión con `int()`**: He convertido la entrada de texto a un número entero para poder usarla como clave en el diccionario `ciudades`.
  
## 6. Procesamiento de la opción

```python
ciudad = ciudades[opcion]
print(f"\nObteniendo datos para {ciudad['nombre']}...")
```

- **Selección de ciudad**: He usado la opción ingresada por el usuario para obtener el diccionario correspondiente a la ciudad seleccionada.
- **f-string para mensaje**: He utilizado otro f-string para mostrar un mensaje informativo que incluye el nombre de la ciudad seleccionada.

## 7. Obtención de datos climáticos

```python
temperatura, velocidad_viento, humedad = obtener_datos_clima(
    ciudad["latitud"],
    ciudad["longitud"]
)
```

- **Llamada a función**: He llamado a la función `obtener_datos_clima` pasándole las coordenadas de la ciudad seleccionada.
- **Asignación de varios valores**: Los tres valores devueltos por la función se asignan directamente a tres variables distintas.
- **Parámetros en varias líneas**: He separado los parámetros en líneas diferentes para mejorar la legibilidad del código.

## 8. Presentación de resultados

```python
print(f"\nDatos climáticos para {ciudad['nombre']}:")
print(f"Temperatura actual: {temperatura} °C")
print(f"Velocidad del viento: {velocidad_viento} km/h")
print(f"Humedad relativa: {humedad}%")
```

- **f-strings para la salida**: Nuevamente, he usado f-strings para mostrar los resultados de manera clara y formateada.
- **Unidades de medida**: He incluido las unidades adecuadas para cada valor (°C para temperatura, km/h para velocidad del viento, % para humedad relativa).

## Decisiones de diseño y justificación

1. **Uso de f-strings**: He elegido usar f-strings porque hacen que el código sea más legible y menos propenso a errores. Son más eficientes que otras formas de formateo de cadenas en Python.

2. **Estructura modular**: He separado la obtención de datos en una función para mantener el código organizado y facilitar la reutilización.

3. **Estructura de datos**: He utilizado un diccionario para almacenar los datos de las ciudades, lo que permite acceder fácilmente a todos los datos necesarios de una ciudad cuando el usuario selecciona una opción.

4. **Selección de ciudades**: He elegido Barcelona, Madrid y Reus como ejemplos representativos de diferentes regiones de España.

5. **API de Open-Meteo**: He elegido esta API porque es gratuita, no requiere autenticación y proporciona datos meteorológicos precisos y actualizados.

6. **Extracción selectiva de datos**: Solo he extraído los datos que son relevantes para el usuario (temperatura, velocidad del viento y humedad), evitando sobrecargar al usuario con información innecesaria.
