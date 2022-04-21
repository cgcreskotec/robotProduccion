# # buscarClikear('Producción',imagen)
#
def buscarClikear(ruta, imagen):
    try:
        coordenadas = pa.locateCenterOnScreen(imagen, confidence=tasaConfidence)
        print(ruta + ' - Ubicación: X: '+ str(coordenadas.x) + ' - Y: ' + str(coordenadas.y))
        pa.moveTo(coordenadas, duration=1)
        pa.click()
    except:
        print("No se pudo encontrar el boton")