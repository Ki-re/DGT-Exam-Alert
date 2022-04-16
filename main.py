from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium import webdriver

import config

from telegram_bot import iniciado, resultado_msg, resultado_imagen, fin, update_funcionando

from datetime import datetime
import time

opciones = Options()
url = "https://sedeclave.dgt.gob.es/WEB_NOTP_CONSULTA/consultaNota.faces"

hora_inicio = float(datetime.today().strftime('%H.%M'))

exit = False
introduccion_datos = False
resultado_encontrado = False

datos = [config.nif, config.fecha_examen, config.carnet, config.fecha_nacimiento]
ids = ["formularioBusquedaNotas:nifnie", "formularioBusquedaNotas:fechaExamen", "formularioBusquedaNotas:clasepermiso", "formularioBusquedaNotas:fechaNacimiento"]

opciones.add_argument("--log-level=3")
opciones.headless = True
opciones.add_argument("--incognito")
opciones.add_argument('--window-size=1920,1080')
navegador = webdriver.Chrome(options=opciones)
navegador.implicitly_wait(2)

time.sleep(3)

iniciado(hora_inicio) # Iniciamos el bot de telegram

while not exit:
    try: # Creamos un primer bloque de try-except para controlar un posible fallo de selenium no esperado

        navegador.get(url) # Iniciamos el navegador de selenium
        contador_intentos = 0

        while not introduccion_datos and contador_intentos < 5: # Introducimos los datos en el formulario
            datos_cont = 0
            for i in range(len(datos)):
                try:
                    navegador.find_element(By.ID, f"{ids[i]}").send_keys(datos[i]) # Buscamos los elementos según su ID e introducimos el dato ubicado en la posición de la lista
                except:
                    print(f"\nError al introducir {ids[i]}")
                else:
                    datos_cont += 1
                time.sleep(3)
                
            if datos_cont == len(datos):
                introduccion_datos = True # En caso de que todos los datos se introduzcan correctamente la variable introduccion_datos queda como True de forma que no se vuelven a introducir dichos datos
            else:
                datos_cont = 0
                navegador.find_element(By.XPATH, "//input[@title='Limpiar']").click() # Limpiamos los datos
                print("\nNo se han podido introducir todos los datos") # En caso de que alguno de los datos no pueda ser introducido se vuelve a intentar

            contador_intentos += 1

        try:
            hora_actual = datetime.today().strftime('%H:%M')
            navegador.find_element(By.XPATH, "//input[@title='Buscar']").click() # Hacemos click en la búsqueda
        except:
            print("No se ha podido buscar el resultado del examen")
        else:
            while not resultado_encontrado:
                
                time.sleep(5)

                try:
                    navegador.find_element(By.CLASS_NAME, "msgError") # Buscamos el mensaje de error qué se muestra al no encontrar resultado
                except: # En caso de no encontrar dicho mensaje de error, se asume que se ha encontrado un resultado
                    time.sleep(5)
                    navegador.save_screenshot("resultado.png")
                    time.sleep(3)
                    aprobado_suspenso = navegador.find_element(By.ID, "formularioResultadoNotas:j_id38:0:j_id70").text # Obtenemos el elemento referente al resultados
                    print(aprobado_suspenso)
                    resultado_msg() # Notificamos que un resultado ha sido encontrado
                    resultado_imagen(aprobado_suspenso) # Enviamos una imagen con el resultado y el resultado
                    resultado_encontrado = True
                    exit = True
                else:
                    print("\nNo hay resultado - "+hora_actual)
                    update_funcionando(hora_actual)
                    time.sleep(config.update_time)
                    continue
    except:
        exit = False
        introduccion_datos = False
        resultado_encontrado = False
        continue

fin()
