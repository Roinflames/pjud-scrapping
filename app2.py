from selenium import webdriver
from selenium.webdriver.firefox.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.firefox.options import Options
from webdriver_manager.firefox import GeckoDriverManager
import time

# Configurar Firefox
options = Options()
options.add_argument("--start-maximized")
options.set_preference("general.useragent.override", "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Firefox/112.0 Chrome/91.0.4472.124 Safari/537.36")

# Desactivar la verificación de certificados SSL
options.set_preference('webdriver_accept_untrusted_certs', True)
options.set_preference('webdriver_assume_untrusted_issuer', True)

options.set_preference("security.ssl.enable_ocsp_stapling", False)
options.set_preference("security.insecure_field_warning.contextual.enabled", False)
options.set_preference("security.ssl.errorReporting.automatic", False)

# Si Firefox no está en su ubicación predeterminada, puedes especificar su ruta
options.binary_location = r"C:\\Program Files\\Mozilla Firefox\\firefox.exe"  # Cambia esto si es necesario

# Iniciar navegador Firefox
driver = webdriver.Firefox(service=Service(GeckoDriverManager().install()), options=options)

# Ir al sitio del PJUD
driver.get("https://civil.pjud.cl/CIVILPORWEB/")

# Esperar a que cargue
time.sleep(3)

# Aceptar los términos (si aparece)
try:
    aceptar = driver.find_element(By.ID, "splashBtnIngresar")
    aceptar.click()
    time.sleep(2)
except:
    pass

# Ir a la búsqueda por RUT
try:
    busqueda_por_rut = driver.find_element(By.ID, "BuscarPorRUT")
    busqueda_por_rut.click()
    time.sleep(2)

    # Ingresar RUT (sin puntos, con guion)
    rut_input = driver.find_element(By.ID, "RUTConsulta")
    rut_input.send_keys("17064957-5")  # <-- Cambia esto por el RUT deseado

    # Hacer clic en Buscar
    buscar_btn = driver.find_element(By.ID, "BtnConsultar")
    buscar_btn.click()
    time.sleep(5)

    # Extraer resultados
    causas = driver.find_elements(By.CLASS_NAME, "resultados")
    for causa in causas:
        print(causa.text)
except Exception as e:
    print("Error en búsqueda:", e)

# Cerrar el navegador
driver.quit()
