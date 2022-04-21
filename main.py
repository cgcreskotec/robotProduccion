import pyautogui as pa
import time

#Si existe algún error se puede abortar el proceso llevando el mouse arriba a la izquierda.
from funcionesRobot import buscarClikear

pa.FAILSAFE = True

# Resolución de Pantalla
#screenWidth, screenHeight = pa.size()
#print('Ancho de Pantalla: '+screenWidth + 'Alto de Pantalla: '+screenHeight)

tasaConfidence = 0.9


### Inicio de la carga de Datos para hacer una nueva ficha técnica desde 0
pa.confirm(text='Se inicia la carga de Datos', title='Inicio de Proceso', buttons=['Confirmar','Cancelar'])

# Buscar menú producción y hacer click
buscarClikear('Producción','.\\printsProcesos\\produccion.png')
time.sleep(1)

# Buscar opción Ficha técnica y hacer click
buscarClikear('Ficha Técnica','.\\printsProcesos\\fichasTecnicas.png')
time.sleep(1)

# Buscar opción agregar ficha técnica y hacer click
buscarClikear('Agregar Ficha Técnica','.\\printsProcesos\\agregarFichaTecnica.PNG')
time.sleep(8)

# Una vez ingresado al panel de Nueva FT

# Buscar Campo Colección y Clickear
buscarClikear('Campo Colección','.\\printsProcesos\\coleccion.PNG')
time.sleep(1)

pa.typewrite('INVIERNO 22 M0')
pa.press('tab')

# Producto
pa.typewrite('A6UK00')
pa.press('enter')
time.sleep(2)
pa.press('tab')


# Buscar opción agregar proceso y hacer click
buscarClikear('Agregar Ficha Técnica','.\\printsProcesos\\agregarProceso.PNG')
time.sleep(2)


