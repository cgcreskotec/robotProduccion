import pyautogui as pa
import time

#Si existe algún error se puede abortar el proceso llevando el mouse arriba a la izquierda.
pa.FAILSAFE = True

# Resolución de Pantalla
screenWidth, screenHeight = pa.size()
#print('Ancho de Pantalla: '+screenWidth + 'Alto de Pantalla: '+screenHeight)

tasaConfidence = 0.9
#imagen = '.\\printsProcesos\\produccion.png'

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

### Inicio de la carga de Datos para hacer una nueva ficha técnica desde 0
pa.confirm(text='Se inicia la carga de Datos', title='Inicio de Proceso', buttons=['Confirmar','Cancelar'])

# Buscar menú producción y hacer click
buscarClikear('Producción','.\\printsProcesos\\produccion.png')
time.sleep(2)

# Buscar opción Ficha técnica y hacer click
buscarClikear('Ficha Técnica','.\\printsProcesos\\fichasTecnicas.png')
time.sleep(3)

# Buscar opción agregar ficha técnica y hacer click
buscarClikear('Agregar Ficha Técnica','.\\printsProcesos\\agregarFichaTecnica.PNG')
time.sleep(8)

# Una vez ingresado al panel de Nueva FT

# Ingresar colección
print('Campo Colección: X: '+ str(pa.locateCenterOnScreen('.\\printsProcesos\\coleccion.PNG', confidence=0.9)[0]) + ' - Y: '+str(pa.locateCenterOnScreen('.\\printsProcesos\\coleccion.PNG', confidence=0.9)[1]))
pa.moveTo(pa.locateCenterOnScreen('.\\printsProcesos\\coleccion.PNG', confidence=0.9), duration=1)
pa.click()
pa.typewrite('INVIERNO 22 M0')
pa.press('tab')

# Producto
pa.typewrite('A6UK00')
pa.press('enter')
time.sleep(2)
pa.press('tab')


#Click en agregar Proceso
print('Botón Agregar Proceso: X: '+ str(pa.locateCenterOnScreen('.\\printsProcesos\\agregarProceso.PNG', confidence=0.9)[0]) + ' - Y: '+str(pa.locateCenterOnScreen('.\\printsProcesos\\agregarProceso.PNG', confidence=0.9)[1]))
pa.moveTo(pa.locateCenterOnScreen('.\\printsProcesos\\agregarProceso.PNG', confidence=0.9), duration=1)
pa.click()







"""
pa.confirm(text='Abrir Google Chrome y BF, ingresa usuario y contraseña.', title='Inicio', buttons=['OK','Cancelar'])

#Click en titulo producción
pa.moveTo(1200, 170, duration=3)
pa.click()
#time.sleep(1)

#Click en titulo producción
pa.moveTo(1200, 295, duration=3)
pa.click()

#pa.typewrite('probando como funciona')

pa.alert('Proceso Finalizado.')
"""

